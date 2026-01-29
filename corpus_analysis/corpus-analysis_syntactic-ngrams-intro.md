# Von Wörtern zu Mustern: n-Gramme

Das [vorangehende Notebook](corpus-analysis_semantic-field-analysis.ipynb) konzentriert sich auf **einzelne Wörter und ihre Häufigkeiten**, etwa um semantische Felder rund um Luft, Verschmutzung oder Umwelt zu identifizieren. Solche Analysen sind ein zentraler erster Schritt, bleiben jedoch auf *isolierte lexikalische Einheiten* beschränkt. Viele inhaltlich relevante Bedeutungen werden jedoch nicht durch einzelne Wörter ausgedrückt, sondern durch **wiederkehrende Wortkombinationen**.

Ein verbreiteter Ansatz, um über Einzelwörter hinauszugehen, ist die Analyse von **n-Grammen**. N-Gramme modellieren Sprache als Sequenzen von *n* aufeinanderfolgenden Tokens und erlauben es, wiederkehrende mehrwortige Muster sichtbar zu machen, etwa Kollokationen, feste Wendungen oder kurze Konstruktionen. So lassen sich statt der getrennten Betrachtung von *Rauch* und *Luft* beispielsweise Muster wie *dichter Rauch*, *schlechte Luft* oder *Luft und Wasser* identifizieren. Hier ist ein Beispiel für die Aufteilung einer Phrase aus einem der vielen Texte dieser Fallstudie (Hinzelmeier von Theodor Storm) in N-Gramme der Länge 1, 2 und 3 (d. h. Unigramme, 2-Gramme und 3-Gramme).

```{figure} ../assets/images/ngrams_simple.png
---
height:
name: Ngrams Example
---
Beispiel für die Aufteilung einer Phrase in N-Gramme der Länge 1, 2 und 3.
```

In diesem Sinne stellen n-Gramme eine natürliche methodische Erweiterung wortbasierter Frequenzanalysen dar: Der Fokus verschiebt sich von der Frage, *welche Wörter vorkommen*, hin zu der Frage, *wie Wörter regelmäßig gemeinsam auftreten*.

Seit längerem ist bekannt, dass Häufigkeiten von n-Grammen ein wirkungsvolles Instrument für die quantitative Untersuchung kultureller Trends, für die Analyse der kulturellen Verarbeitung historischer Ereignisse sowie für die Erforschung der Ideengeschichte darstellen. Bereits in der 2011 erschienenen Arbeit, mit der der Google Books Ngram Viewer eingeführt wurde (Michel, 2011), wiesen die Autor:innen auf die kultur- und geschichtswissenschaftliche Aussagekraft gemeinsamer Frequenzverläufe bestimmter n-Gramme hin. Als Beispiele nennen sie unter anderem die zeitliche Dynamik der englischen 3-Gramme "the Great War", "World War I" und "World War II" sowie die Entwicklung des n-Gramms "天安門" (Tiananmen Square) im chinesischen Korpus.

Inzwischen lassen sich zahlreiche weitere Beispiele finden, die zeigen, wie aufschlussreich n-Gramm-Analysen sein können. Betrachtet man etwa im englischen Google-Books-Korpus alle 2-Gramme, die mit dem Verb "to hate" (hassen) beginnen und mit einem Substantiv enden, so gehört 2-Gramme "**hate war**" (den Krieg hassen) zu den häufigsten Treffern. Auffällig sind dabei zwei sehr ausgeprägte Häufigkeitsspitzen, die zeitlich mit dem Ersten und dem Zweiten Weltkrieg zusammenfallen. 

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

Diese Einschränkung ist besonders relevant für **das Deutsche**, da hier die Wortstellung vergleichsweise flexibel ist und viele häufige Konstruktionen — etwa Partizipialattribute, Verbklammern oder Passivkonstruktionen — auf der Textoberfläche diskontinuierlich realisiert werden. Für eine linguistisch orientierte Analyse bedeutet dies, dass lineare n-Gramme gerade diejenigen Muster fragmentieren, die interpretativ besonders interessant sind.

*Syntaktische n-Gramme* setzen genau hier an. Sie redefinieren, was als Sequenz gilt, indem sie nicht der linearen Tokenfolge folgen, sondern **Relationen in einer syntaktischen Analyse**, typischerweise in einem Dependenzbaum. Wortfolgen werden somit nicht als Oberflächenstrings, sondern als **Pfade in der syntaktischen Struktur** modelliert. Dieser Ansatz wurde als Alternative zu linearen n-Grammen vorgeschlagen und hat sich insbesondere für die sprachliche Beschreibung des Deutschen als nützlich erwiesen, da hier syntaktische Relationen häufig aussagekräftiger sind als lineare Nachbarschaft (vgl. etwa Andresen & Zinsmeister).

---

## Ein einfaches Beispiel: Luft, Rauch und Syntax

Betrachten wir den folgenden Satz:

> *Die von dichtem Rauch erfüllte Luft war kaum atembar.*

Eine lineare n-Gramm-Analyse extrahiert daraus benachbarte Sequenzen wie:

* *dichtem Rauch*
* *Rauch erfüllte*
* *erfüllte Luft*

Diese Muster hängen stark von der konkreten Oberflächenrealisierung ab. Bereits kleine Veränderungen der Wortstellung oder zusätzliche Modifikatoren führen zu anderen linearen n-Grammen, obwohl die zugrunde liegende Beschreibung dieselbe bleibt.

Eine syntaktische n-Gramm-Analyse kann hingegen direkt die syntaktische Beziehung zwischen *Rauch* und *Luft* erfassen, etwa über einen Dependenzpfad der Form:

* *Rauch → erfüllen → Luft*

Dieses syntaktische Muster repräsentiert eine stabile Art der Beschreibung verschmutzter Luft („Luft, die mit Rauch gefüllt ist“) und lässt sich auch in verschiedenen Oberflächenvarianten wiederfinden, etwa in:

* *durch Rauch erfüllte Luft*
* *die Luft war von Rauch erfüllt*
* *Luft, die mit Rauch erfüllt war*

Für die Analyse historischer Diskurse über Luftqualität ermöglichen syntaktische n-Gramme damit den Übergang von einzelnen Schlüsselwörtern zu **wiederkehrenden relationalen Mustern**, mit denen Luftverschmutzung sprachlich beschrieben wird.

---

Das folgende Notebook knüpft an diese Überlegungen an und untersucht, wie syntaktische n-Gramme aus dem Korpus extrahiert werden können und wie sie sich als exploratives Analyseinstrument neben wortbasierten und linearen n-Gramm-Ansätzen einsetzen lassen.