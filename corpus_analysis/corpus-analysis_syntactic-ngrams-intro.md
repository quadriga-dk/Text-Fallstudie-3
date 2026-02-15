# Von Wörtern zu Mustern: n-Gramme

Das [vorangehende Notebook](corpus-analysis_semantic-field-analysis.ipynb) konzentriert sich auf einzelne Wörter und ihre Häufigkeiten, etwa um semantische Felder rund um Luft, Verschmutzung oder Umwelt zu identifizieren. Solche Analysen sind ein zentraler erster Schritt, bleiben jedoch auf *isolierte lexikalische Einheiten* beschränkt. Viele inhaltlich relevante Bedeutungen werden jedoch nicht durch einzelne Wörter ausgedrückt, sondern durch **wiederkehrende Wortkombinationen**.

Ein verbreiteter Ansatz, um über Einzelwörter hinauszugehen, ist die Analyse von **n-Grammen**. N-Gramme modellieren Sprache als Sequenzen von *n* aufeinanderfolgenden Tokens und erlauben es, wiederkehrende mehrwortige Muster sichtbar zu machen, etwa Kollokationen, feste Wendungen oder kurze Konstruktionen. So lassen sich statt der getrennten Betrachtung von *Rauch* und *Luft* beispielsweise Muster wie *dichter Rauch*, *schlechte Luft* oder *Luft und Wasser* identifizieren. Hier ist ein Beispiel für die Aufteilung einer Phrase aus einem der vielen Texte dieser Fallstudie (Eine Nacht im Jägerhause, Friedrich Hebbel) in N-Gramme der Länge 1, 2 und 3 (d. h. Unigramme, 2-Gramme und 3-Gramme):

```{figure} ../assets/images/ngrams_simple.png
---
height:
name: Ngrams Example
---
Beispiel für die Aufteilung einer Phrase in N-Gramme der Länge 1, 2 und 3.
```

In diesem Sinne stellen n-Gramme eine natürliche methodische Erweiterung wortbasierter Frequenzanalysen dar: Der Fokus verschiebt sich von der Frage, *welche Wörter vorkommen*, hin zu der Frage, *wie Wörter regelmäßig gemeinsam auftreten*.

Seit längerem ist bekannt, dass Häufigkeiten von n-Grammen ein wirkungsvolles Instrument für die quantitative Untersuchung kultureller Trends, für die Analyse der kulturellen Verarbeitung historischer Ereignisse sowie für die Erforschung der Ideengeschichte darstellen. Bereits in der 2011 erschienenen Arbeit, mit der der Google Books Ngram Viewer eingeführt wurde {cite:p}`michel_et_al_2011`, wiesen die Autor:innen auf die kultur- und geschichtswissenschaftliche Aussagekraft gemeinsamer Frequenzverläufe bestimmter n-Gramme hin. Als Beispiele nennen sie unter anderem die zeitliche Dynamik der englischen 3-Gramme "the Great War", "World War I" und "World War II" sowie die Entwicklung des n-Gramms "天安門" (Tiananmen Square) im chinesischen Korpus.

Inzwischen lassen sich zahlreiche weitere Beispiele finden, die zeigen, wie aufschlussreich n-Gramm-Analysen sein können. Betrachtet man etwa im englischen Google-Books-Korpus alle 2-Gramme, die mit dem Verb "to hate" (hassen) beginnen und mit einem Substantiv enden, so gehört 2-Gramme "**hate war**" (den Krieg hassen) zu den <a href="https://books.google.com/ngrams/graph?content=hate_VERB+*_NOUN&year_start=1901&year_end=2000&corpus=en&smoothing=3" target="_blank">häufigsten Treffern</a>. Auffällig sind dabei zwei sehr ausgeprägte Häufigkeitsspitzen, die zeitlich mit dem Ersten und dem Zweiten Weltkrieg zusammenfallen. 

```{figure} ../assets/images/ngrams_hate_war.png
---
height:
name: Ngrams Example
---
Ngram Viewer Beispiel.
```

Solche Befunde verdeutlichen, dass n-Gramme nicht nur lexikalische Muster erfassen, sondern auch als Indikatoren für historische Zäsuren und kollektive Deutungsprozesse gelesen werden können.

---

## Von linearen zu syntaktischen n-Grammen

Klassische **lineare n-Gramme** definieren solche Muster ausschließlich auf der Grundlage von Oberflächenadjazenz. Dieser Ansatz ist einfach und oft effektiv, weist jedoch eine zentrale Einschränkung auf: Er reagiert sehr empfindlich auf Wortstellung und auf die Einschübe von Modifikatoren. Dadurch werden semantisch und funktional ähnliche Ausdrücke häufig in viele unterschiedliche Oberflächenvarianten aufgespalten.

Diese Einschränkung ist besonders relevant für das Deutsche, da hier die Wortstellung vergleichsweise flexibel ist und viele häufige Konstruktionen — etwa Partizipialattribute, Verbklammern oder Passivkonstruktionen — auf der Textoberfläche diskontinuierlich realisiert werden. Für eine linguistisch orientierte Analyse bedeutet dies, dass lineare n-Gramme gerade diejenigen Muster fragmentieren, die interpretativ besonders interessant sind (vgl. etwa {cite}`andresen_benefit_2017`).

*Syntaktische n-Gramme* setzen genau hier an. Sie redefinieren, was als Sequenz gilt, indem sie nicht der linearen Tokenfolge folgen, sondern **Relationen in einer syntaktischen Analyse**, typischerweise in einem Dependenzbaum. Wortfolgen werden somit nicht als Oberflächenstrings, sondern als **Pfade in der syntaktischen Struktur** modelliert. 

```{figure} ../assets/images/dep_tree.png
---
height:
name: Ngrams Example
---
 Ein Beispiel für einen Dependenzbaum.
```

Dieser Ansatz wurde als Alternative zu linearen n-Grammen vorgeschlagen und hat sich insbesondere für die sprachliche Beschreibung des Deutschen als nützlich erwiesen, da hier syntaktische Relationen häufig aussagekräftiger sind als lineare Nachbarschaft.

## Ein einfaches Beispiel: Fabrikrauch und verdorbene Luft

Betrachten wir den folgenden Satz:

> *Ich roch eine üble, von den Schloten der neuen Fabriken schwer geschwängerte Luft.*

Eine lineare n-Gramm-Analyse extrahiert daraus benachbarte Sequenzen (2-Gramme) wie:

* *üble von*
* *neuen Fabriken*
* *schwer geschwängerte*
* *geschwängerte Luft*

Diese Muster spiegeln jeweils nur lokale Oberflächenadjazenz wider. Besonders auffällig ist, dass das Adjektiv *üble* zwar semantisch klar die *Luft* charakterisiert, in der linearen Struktur jedoch durch eine längere attributive Erweiterung (*von den Schloten der neuen Fabriken schwer geschwängerte*) vom Substantiv getrennt ist. Eine lineare n-Gramm-Analyse kann diese übergreifende Einheit nicht als zusammenhängendes Muster erfassen.

Eine syntaktische n-Gramm-Analyse hingegen berücksichtigt die Struktur des Dependenzbaums. Dort ist *üble* unmittelbar als Attribut von *Luft* analysiert – unabhängig davon, wie viele weitere Modifikatoren dazwischenstehen. Ein entsprechender syntaktischer Pfad könnte etwa so modelliert werden:

* *übel → Luft*

```{figure} ../assets/images/dep_tree_ueble_luft.png
---
height:
name: Ngrams Example
---
 Ein Beispiel für einen Dependenzbaum.
```

Zugleich lässt sich auch die relationale Struktur der Verschmutzungsbeschreibung erfassen, etwa über einen Pfad wie:

* *Fabriken → schwängern → Luft*

Solche syntaktischen Muster repräsentieren stabile Weisen, Luftverschmutzung sprachlich zu beschreiben – und sie bleiben auch dann erkennbar, wenn die Oberflächenform variiert, etwa in:

* *eine von Fabrikrauch geschwängerte, üble Luft*
* *die Luft war übel und von Fabrikdünsten erfüllt*
* *übel erschien die von Rauch erfüllte Luft der Stadt*

Für die Analyse historischer Diskurse über Industrialisierung und Luftqualität ermöglichen syntaktische n-Gramme somit den Zugriff auf strukturell wiederkehrende Beschreibungsweisen, selbst wenn diese in der Textoberfläche stark variieren oder diskontinuierlich realisiert sind.

---

Das folgende Notebook knüpft an diese Überlegungen an und untersucht, wie syntaktische n-Gramme aus dem Korpus extrahiert werden können und wie sie sich als exploratives Analyseinstrument neben wortbasierten und linearen n-Gramm-Ansätzen einsetzen lassen.

## Bibliographie
```{bibliography}
:filter: docname in docnames
```