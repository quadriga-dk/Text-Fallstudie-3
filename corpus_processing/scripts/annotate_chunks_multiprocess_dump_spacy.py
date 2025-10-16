#!/usr/bin/env python3

import argparse
from time import time
from pathlib import Path
import multiprocessing as mp
import pandas as pd
import spacy
from spacy.tokens import DocBin
import psutil
import gc

def init_worker(nlp_model_name, disable_components):
    """Initialize each worker with its own spaCy model"""
    global nlp, disabled
    nlp = spacy.load(nlp_model_name)
    disabled = disable_components
    #nlp.max_length = 2500000

def process_single_file(filepath):
    """Process a single file - no existence check needed as we pre-filter"""
    try:
        text = filepath.read_text(encoding="utf-8")
        
        # Split by lines for memory efficiency
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            return filepath, None, "Empty file"
        
        # Process in smaller batches to control memory
        batch_size = 30
       
        doc_bin = DocBin()
        for doc in nlp.pipe(lines, disable=disabled, batch_size=batch_size):
            doc_bin.add(doc)
        
        return filepath, doc_bin, None
        
    except Exception as e:
        return filepath, None, str(e)

def monitor_memory():
    """Monitor current memory usage"""
    process = psutil.Process()
    mem = process.memory_info().rss / (1024**3)  # GB
    available = psutil.virtual_memory().available / (1024**3)
    return mem, available

def get_files_to_process(corpus_dir: Path, output_dir: Path, force: bool = False):
    """Get list of files that need processing"""
    corpus_filepaths = sorted(corpus_dir.glob("*.txt"))
    
    if force:
        return corpus_filepaths, []
    
    files_to_process = []
    already_processed = []
    
    for filepath in corpus_filepaths:
        output_path = output_dir / f"{filepath.stem}.csv"
        if output_path.exists():
            already_processed.append(filepath)
        else:
            files_to_process.append(filepath)
    
    return files_to_process, already_processed


def process_corpus(args):
    """Main processing function"""
    
    # Validate paths
    if not args.corpus_dir.exists():
        print(f"Error: Corpus directory '{args.corpus_dir}' does not exist")
        return 1
    
    if not args.corpus_dir.is_dir():
        print(f"Error: '{args.corpus_dir}' is not a directory")
        return 1
    
    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all corpus files
    all_files = sorted(args.corpus_dir.glob("*.txt"))
    print(f"Total files in corpus: {len(all_files)}")
    
    if not all_files:
        print("No .txt files found in corpus directory!")
        return 0
    
    # Filter to only files needing processing
    files_to_process, already_processed = get_files_to_process(
        args.corpus_dir, args.output_dir, args.force
    )
    
    print(f"Already processed: {len(already_processed)} files")
    print(f"To be processed: {len(files_to_process)} files")
    
    
    if not files_to_process:
        print("\nAll files already processed! Nothing to do.")
        if not args.force:
            print("Use --force flag to reprocess all files.")
        return 0
    
    # Model configuration
    nlp_model_name = args.model
    disable_components = ['ner', 'attribute_ruler', 'sentencizer']
    
    # Get optimal number of workers
    n_workers = args.workers
    available_ram_gb = psutil.virtual_memory().available / (1024**3)
    
    print(f"\nProcessing configuration:")
    print(f"  Model: {nlp_model_name}")
    print(f"  Workers: {n_workers}")
    print(f"  Available RAM: {available_ram_gb:.1f}GB")
    if args.force:
        print(f"  Mode: Force reprocess all files")
    print(f"\nStarting processing...\n")
    
    start = time()
    completed = 0
    errors = 0
    processed = 0
    
    # Calculate chunk size for load balancing
    chunksize = max(10, len(files_to_process) // (n_workers * 20))
    
    # Process files in parallel
    with mp.Pool(
        processes=n_workers,
        initializer=init_worker,
        initargs=(nlp_model_name, disable_components)
    ) as pool:
        
        for filepath, data, error in pool.imap_unordered(
            process_single_file, 
            files_to_process,
            chunksize=chunksize
        ):
            completed += 1
            
            if error:
                errors += 1
                print(f"  ERROR: {filepath.name} - {error}")
            else:

                # Save the processed data
                output_path = args.output_dir / filepath.with_suffix(".spacy")
                data.to_disk(output_path)
                processed += 1
                
                if args.verbose and processed <= 5:
                    print(f"  Processed: {filepath.name}")
            
            # Progress monitoring
            if completed % 100 == 0 or completed == len(files_to_process):
                elapsed = time() - start
                rate = completed / elapsed if elapsed > 0 else 0
                eta = (len(files_to_process) - completed) / rate if rate > 0 else 0
                mem_usage, mem_available = monitor_memory()
                
                print(f"  [{completed}/{len(files_to_process)}] "
                      f"Processed: {processed} | "
                      f"Errors: {errors} | "
                      f"Rate: {rate:.1f} files/sec | "
                      f"ETA: {eta/60:.1f} min | "
                      f"Memory: {mem_usage:.1f}GB used, {mem_available:.1f}GB free")
                
                # Garbage collection periodically
                if completed % 500 == 0:
                    gc.collect()
    
    end = time()
    total_time = end - start
    
    # Final summary
    print(f"""
    ========================================
    Processing Complete!
    ========================================
    Total files in corpus: {len(all_files)}
    Previously processed: {len(already_processed)}
    Newly processed: {processed}
    Errors: {errors}
    
    Processing time: {total_time/60:.1f} minutes
    Processing rate: {processed/total_time:.1f} files/second
    Average per file: {total_time/processed:.2f} seconds
    Workers used: {n_workers}
    """)
    
    if errors > 0:
        print(f"\n⚠ Warning: {errors} files had errors during processing")
        return 1
    
    return 0

def main():
    """Main entry point with argument parsing"""
    
    parser = argparse.ArgumentParser(
        description='Process text corpus with spaCy NLP pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/corpus /path/to/output
    Process all .txt files that don't already have output
    
  %(prog)s /path/to/corpus /path/to/output --force
    Reprocess all files, overwriting existing output
    
  %(prog)s /path/to/corpus /path/to/output --workers 4
    Use exactly 4 parallel workers
    
  %(prog)s /path/to/corpus /path/to/output --model de_core_news_lg
    Use a different spaCy model
        """
    )
    
    # Required arguments
    parser.add_argument(
        'corpus_dir',
        type=Path,
        help='Directory containing .txt files to process'
    )
    parser.add_argument(
        'output_dir',
        type=Path,
        help='Directory where .csv output files will be saved'
    )
    
    # Optional arguments
    parser.add_argument(
        '--force',
        action='store_true',
        help='Reprocess all files even if output already exists'
    )
    parser.add_argument(
        '--workers',
        type=int,
        default=4,
        metavar='N',
        help='Number of parallel workers (default: auto-detect based on RAM/CPU)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='de_core_news_sm',
        help='spaCy model to use (default: de_core_news_sm)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed progress information'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0'
    )
    
    args = parser.parse_args()
    
    # Validate workers argument
    if args.workers is not None:
        if args.workers < 1:
            parser.error("Number of workers must be at least 1")
        if args.workers > mp.cpu_count():
            print(f"Warning: {args.workers} workers requested but only {mp.cpu_count()} CPUs available")
    
    # Run processing
    try:
        return process_corpus(args)
    except KeyboardInterrupt:
        print("\n\nProcessing interrupted by user")
        return 130
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
