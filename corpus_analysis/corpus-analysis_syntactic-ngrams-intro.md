## Von linearen zu syntaktischen n-Grammen

Klassische [lineare n-Gramme](corpus-analysis_ngrams-intro.md) definieren solche Muster ausschließlich auf der Grundlage von Oberflächenadjazenz. Dieser Ansatz ist einfach und oft effektiv, weist jedoch eine zentrale Einschränkung auf: Er reagiert sehr empfindlich auf Wortstellung und auf die Einschübe von Modifikatoren. Dadurch werden semantisch und funktional ähnliche Ausdrücke häufig in viele unterschiedliche Oberflächenvarianten aufgespalten.

Diese Einschränkung ist besonders relevant für das Deutsche, da hier die Wortstellung vergleichsweise flexibel ist und viele häufige Konstruktionen — etwa Partizipialattribute, Verbklammern oder Passivkonstruktionen — auf der Textoberfläche diskontinuierlich realisiert werden. Für eine linguistisch orientierte Analyse bedeutet dies, dass lineare n-Gramme gerade diejenigen Muster fragmentieren, die interpretativ besonders interessant sind (vgl. etwa {cite}`andresen_benefit_2017`).

*Syntaktische n-Gramme* setzen genau hier an. Sie redefinieren, was als Sequenz gilt, indem sie nicht der linearen Tokenfolge folgen, sondern Relationen in einer syntaktischen Analyse, typischerweise in einem Dependenzbaum. Wortfolgen werden somit nicht als Oberflächenstrings, sondern als **Pfade in der syntaktischen Struktur** modelliert. 

```{figure} ../assets/images/dep_tree.png
---
height:
name: Ngrams Example
---
 Ein Beispiel für einen Dependenzbaum.
```

Dieser Ansatz wurde als Alternative zu linearen n-Grammen vorgeschlagen und hat sich insbesondere für die sprachliche Beschreibung des Deutschen {cite:p}`andresen_benefit_2017` als nützlich erwiesen, da hier syntaktische Relationen häufig aussagekräftiger sind als lineare Nachbarschaft.

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

* *Luft  → übel*

```{figure} ../assets/images/dep_tree_ueble_luft.png
---
height:
name: Ngrams Example
---
 Ein Beispiel für einen Dependenzbaum.
```

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