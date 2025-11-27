# NLP als Methode zur "Semantisierung" von Text

````{margin}
```{admonition} Fragen oder Feedback 
:class: frage-feedback

<a href="https://github.com/quadriga-dk/Text-Fallstudie-1/issues/new?assignees=&labels=question&projects=&template=frage.yml" class="external-link" target="_blank">
    Stellen Sie eine Frage
</a> <br>
<a href="https://github.com/quadriga-dk/Text-Fallstudie-1/issues/new?assignees=&labels=feedback&projects=&template=feedback.yml" class="external-link" target="_blank">
    Geben Sie uns Feedback
</a>

Mit Ihren Rückmeldungen können wir unser interaktives Lehrbuch gezielt an Ihre Bedürfnisse anpassen.

```
````

## Was ist NLP und warum benutzen wir es?
Für den Computer ist ein Text eine Liste von Zeichen, die nicht aus semantischen Einheiten wie z.B. Wörtern oder Sätzen besteht. Sobald die Operationalisierung einer Forschungsfrage von diesen semantischen Einheiten ausgeht, z.B. auf der Häufigkeit eines Wortes aufbaut, ist es sinnvoll Methoden des <a href="https://en.wikipedia.org/wiki/Natural_language_processing" class="external-link" target="_blank">Natural Language Processing (NLP)</a>  anzuwenden, um den Text mit zusätzlichen linguistischen Informationen anzureichern.  
NLP ist ein interdisziplinäres Feld, das sich zwischen der Linguistik und der Informatik ansiedelt und verschiedene Methoden (regelbasiert, statistisch, <a href="https://en.wikipedia.org/wiki/Machine_learning" class="external-link" target="_blank">maschinelles Lernen</a>) zur automatischen Verarbeitung natürlicher Sprache umfasst. Diese reichen von der Aufteilung eines Texts in Wörter (<a href="https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization" class="external-link" target="_blank">Tokenisierung</a>) über die Analyse von Emotionen in Texten (<a href="https://en.wikipedia.org/wiki/Sentiment_analysis" class="external-link" target="_blank">Emotion / Sentiment Analysis</a>) bis hin zu der Erstellung von Chatbots (<a href="https://en.wikipedia.org/wiki/Dialogue_system" class="external-link" target="_blank">Dialogue Systems</a>). 

## Voraussetzungen
Zur Analyse der Luftqualität soll zum einen das semantische Feld "Luft" untersucht werden, zum anderen sollen Adjektive extrahiert werden, die der Luft attribuiert sind, um die Veränderungen in den Eingenschaften, die Luft zugeschrieben werden, untersuchen zu können.

Für die Untersuchung des semantischen Felds sollen alle Wörter in dem Feld automatisch extrahiert und dann gezählt werden. Die Extraktion der Wörter soll folgende Bedingungen erfüllen:
1. Es sollen **nur** die Wörter des semantischen Felds gefunden werden. Wenn wir nach "Luft" suchen, wollen wir nicht auch "Luftfahrt" finden. 
2. Unterschiedliche Wortformen sollen auf **eine Wortform** abgebildet werden. Wenn wir nach "Dunst" suchen, wollen wir auch "Dünste" finden.

Für die Untersuchung der Adjektiv-Nomen-Paare sollen alle Adjektive extrahiert werden, die den häufigsten Nomen des semantischen Felds "Luft" Eigenschaften zuschreiben. Dafür müssen wir zum einen wissen, welche Wörter Adjektive und Nomen sind und zum anderen welche Adjektive in Beziehung zu welchen Nomen stehen.

(corpus-processing-intro-2)=
## Verwendete NLP-Methoden
Um diese Analysen durchführen zu können, müssen mehrere Vorverarbeitungsschritte durchgeführt werden:
Zuerst muss das Korpus mittels **Tokenisierung** in Wörter, sogenannte Token aufgeteilt, werden. Um verschieden Wortformen auf Grundform, ihr Lemma, abzubilden, wird das Korpus **lemmatisiert** werden.

```{admonition} Zum Begriff des Token
:class: hinweis, dropdown
In der Linguistik wird zwischen einem Wort (Type) und der Verwendung eines Wortes (Token) unterschieden. Der Satz "Die Luft ist gut, die Luft ist rein" hat neun Token (das Komma wird auch als Token gezählt) und 6 Types: "die", "Luft", "ist", "gut", ",", "rein".
```

Um die Adjektive zu extrahieren, muss jedem Wort die Wortart zugewiesen werden. Dies kann automatisch mittels **Part-of-Speech (POS)-Tagging** durchgeführt werden. Im POS-Tagging werden Tagsets verwendet, in denen jeder Wortart eine Abkürzung zugewiesen wird. Die Tagsets können unterschiedlich granular sein, so finden sich im <a href="https://homepage.ruhr-uni-bochum.de/stephen.berman/Korpuslinguistik/Tagsets-STTS.html" class="external-link" target="_blank">Stuttgart-Tübingen-Tagset (STTS)</a> 54 Tags, in denen z.B. das Tempus und der Modus von Verben unterschieden wird. Das <a href="https://universaldependencies.org/u/pos/" class="external-link" target="_blank"> Universal POS Tagset</a> hingegen besteht nur aus 17 Tags, die keinerlei morphologische Informationen liefern. Für die Extraktion der Adjektive ist das Universal POS Tagset ausreichend. 

Die einfachste Methode, um die Beziehung von Adjektive zu Nomen zu extrahieren, ist, diejenigen Adjektiv-Nomen-Paare zu extrahieren, die den geringsten Abstand voneinander haben. Dass diese Methode schnell zu Fehlern führen kann, lässt sich an folgendem Satz zeigen:
`````{admonition} Beispiel
:class: hinweis
Beispielsatz: Die wunderschöne, von einem Nachbarn geklaute Rose ist rot. 

Schwierigkeit: Das Nomen, das mit geringsten Abstand zu dem Adjektiv "wunderschön" steht, ist "Nachbar" und nicht "Rose", worauf sich das Adjektiv tatsächlich bezieht. 
`````

Es wird deshalb auf **Dependenzgrammatik** zurückgegriffen, in der "die syntaktische Struktur eines Satzes ausschließlich anhand gerichteter binärer grammatikalischer Beziehungen zwischen den Wörtern beschrieben wird" (vgl. {cite}`jurafsky2025`, S. 427.). Die grammatikalischen Beziehungen sind durch ein geschlossenen Vokabular beschrieben. In der Linguistik gibt es verschiedene anerkannte Vokabulare z.B. das Universal Dependencies Annotationsschema {citep}`universalDependencies`(s.o.), das für die englische Sprache oder das TIGER-Annotationsschema {citep}`tiger`, das für Deutsch entwickelt wurde.

```{admonition} Unterschiede in den linguistischen Ansätze zu Dependenzgrammatik
:class: hinweis, dropdown
In der Linguistik existieren unterschiedliche Ansätze, um die Beziehung zwischen den Wörtern zu strukturen. Zwei Richtungen sind dabei maßgeblich:
* Dependenzgrammatik: Sätze werden in Wörter unterteilt, die Wörter stehen in einer Eins-zu-eins-Beziehung zueinander. 
* Konstituentengrammatik: Sätze werden in Konstituenten (oder auch Phrasen) unterteilt, die wiederum aus Wörtern bestehen. Sowohl die Wörter in den Konstituenten als auch auch die Konstituenten untereinander sind hierarchisch gegliedert. 

Das Universal Dependencies Annotationsschema folgt der Dependenzgrammatik, während das TIGER-Annotationsschema dem Konstituentenmodell folgt. 
```

Automatische Annotationen mit Dependenzinformationen können mittels **Dependency Parsing** erzeugt werden. In der folgenden Abbildung sind die automatisch erzeugten Dependenzannotationen für den Beispielsatz dargestellt, anhand derer die Adjektiv-Nomen-Paare automatisch extrahiert werden können.

```{figure} ../assets/images/dependency_plot.svg
---
height:
name: Dependenzannotation des Satze "Die wunderschöne, von einem Nachbarn geklaute Rose ist rot".
---
Dependenzannotation erstellt mit der Python-Bibliothek spaCy; model: "de_core_news_sm".
```
Die Dependenzannotation sind durch die beschrifteten Bögen in der oberen Bildhälfte dargestellt. Die Beschriftungen sind die Dependenz-Tags, die Abkürzungen werden in Python-Bibliothek spaCy (s.u.) wie folgt aufgelöst:
* nk: noun kernel element
* sb: subject
* sbp: passivized subject 
* cj: conjunction
* pd: predicate

Die Pfeile drücken die Übergeordnetheit eines Wortes in Beziehung zu einem anderen aus, z.B. ist das Wort "Rose" dem Wort "wunderschöne" übergeordnet und zwar mit der Beziehung "noun kernel element". Das übergeordnete Wort wird **Kopf** genannt.

```{admonition} Fehler in der automatischen Annotation
:class: caution
In der automatischen Annotation lassen sich bereits Fehler feststellen: Das partizipiale Adjektiv "geklaute" ist dem Adjektiv "wunderschöne" in Form einer Konjunktion untergeordnet, allerdings sind die Adjektive nicht durch eine Konjunktion wie "und" verbunden und sind deshalb gleichrangige "noun kernel elements", die von dem Nomen "Rose" abhängen. Um zusätzlich zu den attributive Adjektive auch prädikative Adjektive wie in diesem Beispiel "rot" zu extrahieren, kann das Tag "pd" verwendet werden.
```

Die Abbildung zeigt unter dem Satz zusätzlich die POS-Tags, also die Wortarten, die die Grundlage für das Depedency Parsing bilden. Die folgende Tabelle gibt eine Übersicht über die Annotationen, auf denen die Textanalyse aufbaut.


`````{admonition} Beispiel der Annotationen im Tabellen-Format
:class: hinweis
Ursprünglicher Satz: "Die wunderschöne, von einem Nachbarn geklaute Rose ist rot." \
In tokenisierter und lemmatisierter Form mit POS-Tags und Dependenz-Tags sowie Dependenz-Kopf:

```{table}
:name: Tokenisierung, Lemmatisierung und POS-Tagging (Universal Tags)
| Token   | Lemma| POS-Tag | Dependenz-Tag | Dependenz-Kopf |
|--------|-------|---------|---------------| ---------------| 
| Die | der | DET | nk| Rose| 
| wunderschöne | wunderschön | ADJ | nk| Rose| 
| , | -- | PUNCT | punct| wunderschöne| 
| von | von | ADP | sbp| geklaute| 
| einem | ein | DET | nk| Nachbarn| 
| Nachbarn | Nachbar | NOUN | nk| von| 
| geklaute | geklaut | ADJ | cj| wunderschöne| 
| Rose | Rose | NOUN | sb| ist| 
| ist | sein | AUX | ROOT| ist| 
| rot | rot | ADV | pd| ist| 
| . | -- | PUNCT | punct| ist|
```
`````

## NLP mit Python 

### nltk und spaCy 
In Programmiersprachen gibt es Bibliotheken, die Methoden z.B. zur Textverarbeitung, bündeln. Die Bibliotheken können installiert, in den Programmcode geladen und dann angewendet werden.
Für Python gibt es verschiedene Bibliotheken, mit denen die Verarbeitung von Texten mittels NLP möglich ist. Am weitesten vebreitet sind die Bibliotheken <a href="https://spacy.io" class="external-link" target="_blank">spaCy</a> und <a href="https://www.nltk.org/" class="external-link" target="_blank">nltk</a>, die in Tabelle {ref}`cmp-spacy-nltk` verglichen werden.

```{table} Vergleich von spaCy und nltk
:name: cmp-spacy-nltk
| Bibliothek | Vorteile | Nachteile | 
|------|----------|-----------|
| spaCy| <ul><li>kurze Verarbeitungsdauer</li><li>leichte Benutzbarkeit durch komplette Pipeline</li><li>Visualisierungsmöglichkeiten</li></ul> | <ul><li>Weniger flexibel in der Anpassung an spezielle Anwendungsfälle</li></ul> | 
| nltk | <ul><li>flexibel in der Anpassung an spezielle Anwendungsfälle</li><li>Transparenz einzelner Schritte in einer Pipeline</li></ul> | <ul><li>Lange Verarbeitungsdauer</li><li>Höhere Einstiegshürde</li></ul>|
```
`````{admonition} Zum Begriff der Pipeline
:class: hinweis, dropdown
Die verschiedenen NLP-Methoden bauen teilweise aufeinander auf. Grundlegend wird ein Text zuerst tokenisiert, dann folgt PoS-Tagging und die Lemmatisierung. Diese Abfolge der einzelnen Prozess wird im NLP häufig mit der Metapher einer Pipeline beschrieben. 
`````

### NLP mit spaCy 
Da die Vorverarbeitung der Texte keinerlei spezialisierter NLP-Methoden bedarf und auf Grund der leichten Benutzbarkeit sowie der Geschwindigkeit benutzen wir spaCy für die Annotation des Textkorpus. spaCy stellt unterschiedliche Methoden für die Vorverarbeitung bereit, die meisten basieren auf maschinellem Lernen. Da die Vorverarbeitung sprachabhängig ist, stellt spaCy für die unterstützten Sprachen (über 20) verschiedene Analyse-Modelle zur Verfügung. Eine Übersicht über die von spaCy unterstützen Sprachen gibt es <a href="https://spacy.io/models" class="external-link" target="_blank">hier</a>.
Die zur Verfügung gestellte Modelle unterscheiden sich in der Geschwindigkeit und in der Akkuratheit der Annotation. Da wir auf einem verhältnismäßig großem Korpus operieren und sich die Leistung der Modelle für die Tokenisierung gar nicht und für die Lemmatisierung, das POS-Tagging nur wenig (0.01% - 0.04%) unterscheidet, verwenden wir ein Modell, das auf Geschwindigkeit ausgelegt ist (`de_core_news_sm`). Die Akkuratheit der deutschen Modelle wird auf <a href="https://spacy.io/models/de" class="external-link" target="_blank">dieser Website</a> verglichen. 
Die Dokumentation von spaCy gibt leider nicht für jede Annotation Auskunft darüber, welches Tagset benutzt wird. Für die Annotation mit POS-Tags bietet spaCy zwei Möglichkeiten, zum einen die gröbere Annotation mit dem Universal Tagset, zum anderen die Annotation mit dem STTS-Tagset. Für die Dependenz-Annotationen wird nicht das Universal-Dependency Tagset verwendet. Es gibt zwar eine Tagübersicht, allerdings ist für die Tags keine Quelle gelistet. 


`````{admonition} Leistung von spaCy auf unserem Korpus 
:class: caution
Die Modelle in spaCy sind auf zeitgenössische Zeitungs- und Medientexte ausgelegt. Historische Sprachverwendung führt zu einer geringeren Annotationsleistung.  

`````

## Zusammenfassung und nächste Schritte
Die NLP-Methoden, die für die Vorverarbeitung von Texten notwendig sind, wurden erklärt. spaCy wurde als Bibliothek festgelegt, mit der die Methoden auf die Textdaten angewendet werden. Im nächsten Schritt werden die Texte, die als txt-Dateien vorliegen, mittels spaCy annotiert und die Annotationen werden in einem spaCy-spezifischen sowie im Tebellen-Format gespeichert.  
