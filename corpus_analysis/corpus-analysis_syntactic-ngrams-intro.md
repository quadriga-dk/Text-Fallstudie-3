## Von linearen zu syntaktischen n-Grammen

Klassische [lineare n-Gramme](corpus-analysis_ngrams-intro.md) definieren mehrwortige Muster ausschließlich auf der Grundlage von Oberflächenadjazenz. Dieser Ansatz ist einfach und oft effektiv, weist jedoch eine zentrale Einschränkung auf: Er reagiert sehr empfindlich auf Wortstellung und auf die Einschübe von Modifikatoren. Dadurch werden semantisch und funktional ähnliche Ausdrücke häufig in viele unterschiedliche Oberflächenvarianten aufgespalten.

Betrachten wir den folgenden Satz:

> *Ich roch eine üble, von den Schloten der neuen Fabriken schwer geschwängerte Luft.*

Eine lineare n-Gramm-Analyse extrahiert daraus benachbarte Sequenzen (2-Gramme) wie:

* *Ich roch*
* *roch eine*
* *eine üble*
* *üble von*
* *von den*
* *den Schloten*
* *Schloten der*
* *der neuen*
* *neuen Fabriken*
* *Fabriken schwer*
* *schwer geschwängerte*
* *geschwängerte Luft*

Diese Muster spiegeln jeweils nur lokale Oberflächenadjazenz wider. Besonders auffällig ist, dass das Adjektiv *üble* zwar semantisch klar die *Luft* charakterisiert, in der linearen Struktur jedoch durch eine längere attributive Erweiterung (*von den Schloten der neuen Fabriken schwer geschwängerte*) vom Substantiv getrennt ist. Eine lineare n-Gramm-Analyse kann diese übergreifende Einheit nicht als zusammenhängendes Muster erfassen.

Diese Einschränkung ist besonders relevant für das Deutsche {cite:p}`andresen_benefit_2017`, da hier die Wortstellung vergleichsweise flexibel ist und viele häufige Konstruktionen — etwa Partizipialattribute (wie in unsere Beispiel oben), Verbklammern oder Passivkonstruktionen — auf der Textoberfläche diskontinuierlich realisiert werden. Für eine linguistisch orientierte Analyse bedeutet dies, dass lineare n-Gramme gerade diejenigen Muster fragmentieren, die interpretativ besonders interessant sind.

*Syntaktische n-Gramme* setzen genau hier an. Sie redefinieren, was als Sequenz gilt, indem sie nicht der linearen Tokenfolge folgen, sondern Relationen in einer syntaktischen Analyse, typischerweise in einem <a href="https://de.wikipedia.org/wiki/Dependenzgrammatik" target="_blank">Dependenzbaum</a>. Wortfolgen werden somit nicht als Oberflächenstrings, sondern als **Pfade in der syntaktischen Struktur** modelliert. In einer syntaktischen n-Gramm-Analyse ist *üble* unmittelbar als Attribut von *Luft* analysiert – unabhängig davon, wie viele weitere Modifikatoren dazwischenstehen. 

```{figure} ../assets/images/dep_tree_ueble_luft_part_demo.png
---
height:
name: Ngrams Example
---
 Teil des syntaktischen Dependenzbaum für dasselbe Beispiel.
```

Alle Wortpaare in einem solchen Baum, die eine direkte Abhängigkeitsverbindung aufweisen, können als syntaktische Bigramme behandelt werden: 

* *Ich  ← roch*
* *roch  → Luft*
* **übel ← Luft**
* *ein ← Luft*
* *übel → geschwängerte* 
* *von ← geschwängerte*

usw.

Der vollständige syntaktische Baum, projiziert auf die lineare Struktur des Satzes und erzeugt mit dem deutschen spacy-Modell de_core_news_sm, sieht folgendermaßen aus:

```{figure} ../assets/images/dep_tree_ueble_luft.png
---
height:
name: Ngrams Example
---
 Vollständiger syntaktischer Dependenzbaum für dasselbe Beispiel, projiziert auf die lineare Struktur des Satzes. Die direkte syntaktische Dependenzbeziehung von *Luft* zu *üble* ist rot hervorgehoben.
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