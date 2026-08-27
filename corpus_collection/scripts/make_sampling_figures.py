"""Erzeugt die Abbildungen zur Stichprobenziehung in Abschnitt 3.1.2.

Die Abbildungen illustrieren
1. den Unterschied zwischen einer Zufallsauswahl und einer Auswahl "nach Gefühl"
   (``corpus-collection_sampling_random-vs-biased.svg``) und
2. die geschichtete Zufallsstichprobe
   (``corpus-collection_sampling_stratified.svg``).

Das Skript benoetigt nur die Standardbibliothek und schreibt direkt nach
``assets/images/``. Der Zufallsgenerator ist fest initialisiert, damit erneute
Laeufe identische Dateien erzeugen.

Aufruf aus dem Wurzelverzeichnis des Repositoriums:

    python corpus_collection/scripts/make_sampling_figures.py
"""

import random
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[2] / "assets" / "images"

FONT = "Helvetica, Arial, sans-serif"
INK = "#1a1a1a"
FRAME = "#8a8a8a"
MUTED = "#b8b8b8"

# Kategorien: Farbe UND Form kodieren dieselbe Information, damit die
# Abbildungen auch ohne Farbwahrnehmung lesbar bleiben.
CATEGORIES = [
    ("Abenteuerroman", "#00305e", "circle"),
    ("Familienroman", "#d95f02", "square"),
    ("historischer Roman", "#1b9e77", "triangle"),
]


def marker(x, y, shape, color, size=5.0, opacity=1.0):
    """Ein Datenpunkt als Kreis, Quadrat oder Dreieck."""
    if shape == "circle":
        return (
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" '
            f'fill="{color}" fill-opacity="{opacity}"/>'
        )
    if shape == "square":
        a = size * 1.75
        return (
            f'<rect x="{x - a / 2:.1f}" y="{y - a / 2:.1f}" '
            f'width="{a:.1f}" height="{a:.1f}" '
            f'fill="{color}" fill-opacity="{opacity}"/>'
        )
    h = size * 1.9
    pts = f"{x:.1f},{y - h * 0.6:.1f} {x - h * 0.58:.1f},{y + h * 0.42:.1f} {x + h * 0.58:.1f},{y + h * 0.42:.1f}"
    return f'<polygon points="{pts}" fill="{color}" fill-opacity="{opacity}"/>'


def text(x, y, s, size=14, weight="normal", anchor="start", color=INK, style="normal"):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}" '
        f'fill="{color}">{s}</text>'
    )


def box(x, y, w, h):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
        f'fill="#ffffff" stroke="{FRAME}" stroke-width="1.5"/>'
    )


def jittered_grid(x, y, w, h, cols, rows, rng, pad=14, jitter=0.28):
    """Gleichmaessig verteilte, leicht verwackelte Punkte innerhalb eines Kastens."""
    cw = (w - 2 * pad) / cols
    ch = (h - 2 * pad) / rows
    spots = []
    for r in range(rows):
        for c in range(cols):
            cx = x + pad + cw * (c + 0.5) + rng.uniform(-jitter, jitter) * cw
            cy = y + pad + ch * (r + 0.5) + rng.uniform(-jitter, jitter) * ch
            spots.append((cx, cy))
    rng.shuffle(spots)
    return spots


def draw_points(spots, counts, rng):
    """Verteilt die Kategorien gemaess ``counts`` auf die Positionen."""
    bag = []
    for (label, color, shape), n in zip(CATEGORIES, counts):
        bag.extend([(color, shape)] * n)
    rng.shuffle(bag)
    return "".join(
        marker(px, py, shape, color) for (px, py), (color, shape) in zip(spots, bag)
    )


def arrow(x1, y1, x2, y2, color=INK):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
        f'stroke-width="2" marker-end="url(#arrowhead)"/>'
    )


DEFS = (
    '<defs><marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" '
    'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker></defs>'
)


def svg(width, height, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">{DEFS}'
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>{body}</svg>\n'
    )


def figure_random_vs_biased():
    rng = random.Random(20260827)
    p = []

    # Grundgesamtheit
    p.append(text(30, 68, "Grundgesamtheit", size=16, weight="bold"))
    p.append(text(30, 88, "alle Romane des 19. Jahrhunderts", size=13, color="#555555"))
    p.append(box(30, 100, 310, 340))
    p.append(draw_points(jittered_grid(30, 100, 310, 340, 10, 12, rng), [45, 40, 35], rng))

    # Zufallsstichprobe
    p.append(arrow(352, 180, 546, 180))
    p.append(text(449, 168, "zufällig ziehen", size=13, anchor="middle"))
    p.append(text(560, 88, "Zufallsstichprobe", size=16, weight="bold"))
    p.append(box(560, 100, 310, 160))
    p.append(draw_points(jittered_grid(560, 100, 310, 160, 6, 2, rng), [5, 4, 3], rng))
    p.append(
        text(560, 284, "Die Mischung der Grundgesamtheit bleibt erhalten.", size=13, color="#555555")
    )

    # Auswahl nach Vorlieben
    p.append(arrow(352, 380, 546, 380))
    p.append(text(449, 368, "„nach Gefühl“ auswählen", size=13, anchor="middle"))
    p.append(text(560, 340, "Auswahl nach Vorlieben", size=16, weight="bold"))
    p.append(box(560, 352, 310, 160))
    p.append(draw_points(jittered_grid(560, 352, 310, 160, 6, 2, rng), [1, 2, 9], rng))
    p.append(
        text(560, 536, "Verzerrt: eine Untergattung dominiert.", size=13, color="#555555")
    )

    # Legende
    lx = 30
    for label, color, shape in CATEGORIES:
        p.append(marker(lx + 8, 566, shape, color))
        p.append(text(lx + 22, 571, label, size=13))
        lx += 22 + 8.2 * len(label) + 26

    return svg(900, 590, "".join(p))


def figure_stratified():
    rng = random.Random(11071850)
    decades = ["1820er", "1830er", "1840er", "1850er", "1860er", "1870er", "1880er", "1890er"]
    sizes = [4, 6, 9, 12, 15, 18, 21, 24]
    per_stratum = 3

    blue = CATEGORIES[0][1]
    p = []
    p.append(text(30, 40, "Grundgesamtheit: ungleich über die Jahrzehnte verteilt", size=16, weight="bold"))

    baseline_top = 300
    drawn_per_column = []
    for i, (label, n) in enumerate(zip(decades, sizes)):
        cx = 95 + i * 101
        picked = set(rng.sample(range(n), per_stratum))
        drawn_per_column.append(picked)
        for j in range(n):
            cy = baseline_top - j * 10
            if j in picked:
                p.append(marker(cx, cy, "circle", blue, size=4.5))
            else:
                p.append(marker(cx, cy, "circle", MUTED, size=4.5))
        p.append(text(cx, 324, label, size=13, anchor="middle"))
    p.append(
        f'<line x1="60" y1="{baseline_top + 10}" x2="850" y2="{baseline_top + 10}" '
        f'stroke="{FRAME}" stroke-width="1"/>'
    )

    p.append(arrow(455, 342, 455, 386))
    p.append(
        text(
            470,
            370,
            "aus jeder Schicht gleich viele Texte zufällig ziehen",
            size=13,
        )
    )

    p.append(text(30, 424, "Geschichtete Zufallsstichprobe: jedes Jahrzehnt gleich stark vertreten", size=16, weight="bold"))
    baseline_bottom = 486
    for i, label in enumerate(decades):
        cx = 95 + i * 101
        for j in range(per_stratum):
            p.append(marker(cx, baseline_bottom - j * 12, "circle", blue, size=4.5))
        p.append(text(cx, 512, label, size=13, anchor="middle"))
    p.append(
        f'<line x1="60" y1="{baseline_bottom + 12}" x2="850" y2="{baseline_bottom + 12}" '
        f'stroke="{FRAME}" stroke-width="1"/>'
    )

    p.append(marker(38, 542, "circle", blue, size=4.5))
    p.append(text(52, 547, "gezogen", size=13))
    p.append(marker(148, 542, "circle", MUTED, size=4.5))
    p.append(text(162, 547, "nicht gezogen", size=13))

    return svg(900, 566, "".join(p))


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets = {
        "corpus-collection_sampling_random-vs-biased.svg": figure_random_vs_biased(),
        "corpus-collection_sampling_stratified.svg": figure_stratified(),
    }
    for name, content in targets.items():
        (OUT_DIR / name).write_text(content, encoding="utf-8")
        print(f"geschrieben: {OUT_DIR / name}")


if __name__ == "__main__":
    main()
