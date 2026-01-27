(corpus-analysis_analysis)=
# Semantische Felder, Häufigkeitsanalyse und Visualisierung

## Forschungsfrage und Operationalisierung
In der Korpusanalyse kehren wir wieder zu unserer Fragestellung und auf die Operationalisierung der Fragestellung zurück. Unsere Fragestellung lautet:

`````{admonition} Forschungsfrage
:class: keypoint
Wie diskursivieren deutschsprachige literarische Texte des 19. Jahrhunderts die abnehmende Luftqualität und wie verändern sich dabei die Häufigkeiten und Kontexte des semantischen Feldes „Luft“ im Zeitverlauf?
`````

Gemäß der Operationalisierung ist die Analyse zweigeteilt. Zum einen wird untersucht, ob es eine Entwicklung in der Häufigkeit gibt, mit der die literarischen Texte in den Korpora über Luft sprechen. Zum anderen wird untersucht, auf welche Art und Weise Luft semantisiert wird. Auf die zweite Analyse wird näher in den Kapiteln ... eingegangen.

## Das semantische Feld "Luft"
### Erläuterung: Semantisches Feld
Die Grundlage unserer Analyse besteht darin, die Textstellen zu identifizieren, in denen Luft eine Rolle spielt, wie es zum Beispiel bei der bloßen Erwähnung von Luft der Fall ist. Uns interessiert jedoch nicht Luft als Einzelwort, sondern als Themenkomplex, weswegen wir eine Liste von Wörtern erstellen, die in semantisch-paradigmatischer Beziehung zu Luft stehen, einem **semantischen Feld**. Bei der Erstellung eines semantisches Felds ist es wichtig, dass möglichst alle und nur die Textstellen erfasst werden, in denen Luft und verwandte Worter erwähnt werden. Da die Wörter losgelöst von ihrem Kontext analysiert werden, sollten sie so gewählt sein, dass sie sich auf Luft und nur auf diese beziehen.

### Erstellung des semantischen Felds
Da <a href="https://en.wikipedia.org/wiki/Large_language_model" class="external-link" target="_blank">Large Language Models</a> sehr gut dazu in der Lage sind, semantisch ähnliche Wörter zu erzeugen, haben wir das semantische Feld mit Hilfe des Chatbots <a href="https://claude.ai/" class="external-link" target="_blank">Claude</a> erstellt.

```{admonition} Spezifikation zur Claude-Nutzung
:class: hinweis
**Verwendetes Claude Modell**: Opus 4.5

**Prompt ausgeführt am**: 26.01.2026

**Prompt**:
Du bist eine Digital Humanities-Forscherin mit Expertise im Bereich der Computerlinguistik. Du verfügst über umfassende Kenntnisse im Bereich der Semantik und des Text und Data Mining.
Bitte erstelle ein semantisches Feld zum Thema "Luft". Die Sprache ist deutsch. 
Bedingungen für die Wörter des semantischen Feldes sind. 
* die Wörter sollen Substantive sein;
* Komposita sind erlaubt;
* die Wörter sollen sich am historischen Sprachgebrauch des 19. Jahrhunderts orientieren;
* die Wörter sollen spezifisch für den Kontext "Luft" sein;
* die Wörter sollen nicht mehrdeutig sein, also noch Möglichkeit nicht in anderen semantischen Kontext vorkommen.

Bitte tue dasselbe für "gute Luft" und "schlechte Luft". 
```
Diesen Prompt haben wir zweimal in unterschiedlichen Chats ausgeführt und als Resultat eine Liste von 112 Nomen erhalten. Diese haben wir manuell gefiltert: Wörter, die rein auf den Geruch bezogen sind wie z.B. "Fäulnisgeruch" oder "Pestgeruch" wurden entfernt, genau so wie Wörter, die zu generell waren oder die keinen direkten Bezug zu "Luft" hatten wie etwa "Dumpfheit". Nach der Filterung bestand die Liste noch aus 96 Wörtern.

Zusätzlich sind wir vom Korpus ausgegangen und haben mit Hilfe von <a href="https://www.laurenceanthony.net/software/antconc/" class="external-link" target="_blank">AntConc</a>, einem Korpusanalyse-Programm, alle Komposita, die als Erstglied "Luft" haben, extrahiert. Mit dieser Methode konnten wir noch 31 Nomen hinzufügen, sodass unsere finale Liste aus insgesamt 127 Nomen besteht. Die Liste ist <a href="" class="external-link" target="_blank">hier in GitHub einsehbar</a>.  

## Häufigkeit als Analysemethode 

### Warum die Häufigkeit analysieren?
Die Analyse von Worthäufigkeiten ist sowohl in der Korpuslinguistik als auch in den Digital Humanities weit verbreitet. Für die Analyse von Inhaltswörtern (Nomen, Verben, Adjektive, Adverben) wird angenommen, dass ein hohes Vorkommen mit der Wichtigkeit der Wörter im Text korreliert. Besonders bei einem Vergleich von zwei oder mehr Texten ist die Häufigkeitsanalyse sinnvoll, da der Vergleich so quantisierbar wird und eine Aussage darüber getroffen werden kann, ob eine Veränderung zufällig oder systematisch ist.

Die Häufigkeit eines semantischen Felds wird erhoben, indem pro Text gezählt wird, wie viele Wörter Teil des semantischen Felds sind. Da die Wörter in der Grundform angegeben sind, werden sie mit den Lemmata im Text verglichen. Die Anzahl der Wörter nennt sich **absolute Häufigkeit**.

`````{admonition} Beispiel
:class: hinweis
1. **Text**: Die Luft war rein, eine klare Winterluft. Kein Nebel war zu sehen, eine leichte Brise wehte. 
2. **Lemmatisierter Text**: der Luft sein rein , ein klar Winterluft . kein Nebel sein zu sehen , ein leicht Brise wehen .  
3. **Semantisches Feld** Luft, Winterluft, Nebel, Brise
4. **Häufigkeitsanalyse**: 

```{table}
:name: Häufigkeitsanalyse
| Wort  | Häufigkeit| 
|--------|-------|
| Luft  | 1   |
| Winterluft | 1 |
| Nebel  | 1 |
| Brise  | 1 |
```

**Absolute Häufigkeit**: 4

`````

### Vergleichbarkeit von Häufigkeiten
Für die Vergleichbarkeit von Worthäufigkeiten in Texten ist wichtig, dass die Texte auch ansonsten vergleichbar sind. Stammen die Texte z. B. aus unterschiedlichen Zeiträumen müssten ggf. zeitspezifische semantische Felder erstellt werden, um für den Sprachwandel Rechnung zu tragen. Auch sollten die Texte eine ähnliche Länge haben, sodass eine erhöhte Häufigkeit tatsächlich auf eine erhöhte Wichtigkeit zurückgeführt werden kann.
Wenn Texte verschieden lang sind, sollten die Häufigkeiten **normalisiert** werden, das heißt sie werden in Bezug zur Textlänge gesetzt. Dafür wird die absolute Häufigkeit durch die Textlänge dividiert, daraus ergibt sich die **relative Häufigkeit**. Die relative Häufigkeit des semantischen Felds "Luft" kann als Anteil der Luftwörter am Gesamttext gesehen werden. 

`````{admonition} Beispiel
:class: hinweis
Der Beispieltext A besteht aus insgesamt 69 Wörtern, davon sind 4 Wörter in dem semantischen Feld "Luft" vorhanden. Daraus ergibt sich folgende Rechnung:

$ f = {4 \over 69} = {0.05797101449} $

Das heißt: Jedes zwanzigste Wort im Text steht im Zusammenhang mit Luft. 


Der Beispieltext B besteht aus insgesamt 200 Wörtern, davon sind 4 Wörter in dem semantischen Feld "Luft" vorhanden. Daraus ergibt sich folgende Rechnung:

$ f = {4 \over 200} = {0.02} $

Das heißt: Jedes fünfzigste Wort im Text steht im Zusammenhang mit Luft.

Obwohl in beiden Texten die absolute Häufigkeit gleich ist (4 Wörter des Felds), ist anzunehmen, dass Luft in Beispieltext A eine größere Rolle spielt als in Beispieltext B, da die relative Häufigkeit für A höher ist als für B. 
`````

### Analyse des gesamten Korpus 
Um den Verlauf nachzuvollziehen, wird für jeden Text im Korpus die relative Häufigkeit des semantischen Felds "Luft" berechnet und in einer Tabelle gespeichert. Die Häufigkeiten können dann über die Zeit verglichen werden, sodass sich ablesen lässt, ob im Laufe der Zeit weniger, mehr oder gleich viel über Luft gesprochen wird.  

`````{admonition} Auszug aus der Analysetabelle für Korpus I
:class: hinweis

```{table}
:name: Häufigkeitsanalyse-Korpus
| lastname | firstname | title | year | total_count_tokens | total_count_semantic_field | relative_frequency |
|----------|-----------|-------|------|-------------------|---------------------------|-------------------|
| Mörike | Eduard | Aus dem Gebiete der Seelenkunde | 1861-01-01 | 596 | 2 | 0.33557 |
| von Hofmannsthal | Hugo | Das Dorf im Gebirge | 1896-01-01 | 1270 | 4 | 0.314961 |
| Willkomm | Ernst | Erzählungen eines Wattenschiffers | 1854-01-01 | 7083 | 20 | 0.282366 |
| Seidl | Johann Gabriel | Das goldene Ringlein | 1842-01-01 | 5855 | 15 | 0.256191 |
| von Eichendorff | Joseph | Eine Meerfahrt | 1835-01-01 | 23279 | 55 | 0.236264 |
| von Sacher-Masoch | Leopold | Der Capitulant | 1875-01-01 | 20544 | 41 | 0.199572 |
```
Hinweis: Da für die Texte nur das Publikationsjahr vorliegt, für die Visualisierung aber ein Datum verwendet wird, wird das Datum in der Spalte `year` für jeden Text auf den 01.01. gesetzt.

`````

### Visuelle Darstellung als Streudiagramm 
Als Resultat haben wir pro Korpus 400 Datenpunkte, für jeden Text einen. Diese Datenpunkte lassen sich auf unterschiedliche Art und Weise darstellen. Wir sind zum einem daran interessiert, ob sich eine Entwicklung abzeichnet, dafür müssen die Datenpunkte über Zeit angeordnet werden. Zum anderen wollen wir ablesen können, in welchen Texten Luft besonders häufig thematisiert wird, da diese möglicherweise wegweisend gewesen sein könnten. Die Datenpunkte sollen also nicht pro Jahr oder Dekade aggregiert werden, sondern jeder Text soll einzeln erkennbar sein. Dies lässt sich besonders gut durch ein **Streudiagramm** darstellen. Bei einem Streudigramm wird ein Text in Abhängigkeit seines X- und Y-Wertes als ein Punkt im Koordiantenkreuz dargestellt. Der X-Wert ist in unserem Fall das Jahr der Veröffentlichung, der Y-Wert ist die relative Häufigkeit.

Auf einem Streudiagramm lassen sich allerdings nicht sofort Entwicklungen ablesen. Um diesen Nachteil beizukommen, lässt sich mittels linearer Regression eine **Regressionsgerade** oder sogenannte Trend-Linie berechnen. Die Trend-Linie soll die Datenpunkte möglichst gut beschreiben, das heißt, sie soll möglichst nah an allen Punkten vorbeilaufen. Je nachdem, ob die Gerade steigt oder fällt, ist eine Zu- oder Abnahme des semantischen Felds Luft zu erkennen.

In folgendem Beispiel wurden vier Texte aus Korpus I ausgewählt, für die die relative Häufigkeit und die Trend-Linie errechnet wurde. Diese Texte ("Eine Meerfahrt", "Die Ahnung", "Waldwinkel", "Susi") sind nicht repräsentativ und sollen einzig die visuelle Darstellung verdeutlichen.

```{figure} ../assets/images/Scatterplot-Trendlinie-Bsp.png
---
height:
name: Streudigramm mit Trend-Linie
---
Streudiagramm mit Trend-Linie berechnet auf vier Texten aus Korpus I. Jeder Punkt ist ein Text. Die Texte haben folgende Titel (von links nach rechts): "Eine Meerfahrt", "Die Ahnung", "Waldwinkel", "Susi".
```

```{admonition} Lineare Regression
:class: hinweis, dropdown
Um die Regressionsgerade zu berechnen, wird für jeden Punkt der vertikalen Abstand zur Gerade berechnet – also wie weit der tatsächliche Wert nach oben oder unten von der Linie abweicht. Diese Abweichungen nennt man "Fehler" oder "Residuen". Damit sich positive und negative Abweichungen nicht gegenseitig aufheben, werden diese Abstände quadriert (also mit sich selbst multipliziert). Die beste Linie ist dann diejenige, bei der die Summe dieser quadrierten Abstände am kleinsten ist. Diese Methode der Berechnung heißt Methode der kleinsten Quadrate.
```




### Visuelle Darstellung als Streudigramm
Alternativ, wenn es weniger wichtig ist, die Häufigkeiten einzelner Texte abzulesen, ließen sich die Häufigkeiten auch über einen bestimmten Zeitraum zummenfassen und als Liniendiagramm darstellen. Liniendiagramme eignen sich gut, um zeitliche Verläufe darzustellen, da lokale und globale Minima und Maxima leicht erkennbar sind und sie die Kontinuität der Daten unterstreichen. Um die Häufigkeiten zusammenzufassen werden sowohl die absoluten Häufigkeiten als auch die Textlängen in dem ausgewählten Zeitraum addiert, sodass auf dieser Basis die relative Häufigkeit für den Zeitraum berechnet werden kann.


`````{admonition} Durchschnitt von relativen Häufigkeiten
:class: caution
Eine zweite Möglichkeit, die Häufigkeiten über eine Zeitraum zusammenzufassen, bestünde darin, den Durchschnitt der Häufigkeiten pro Jahr zu berechnen. Allerdings haben bei dieser Methode alle Texte aus dem selben Erscheinungsjahr den gleichen Einfluss auf die Berechnung, unabhängig davon, ob ein Text nur ein zehntel so lang ist, wie ein anderer Text. 

```{table}
:name: Beispiel: Methoden des Zusammenfügens

| Jahr  | Absolute Häufigkeit| Textlänge | Relative Häufigkeit | 
|------|--------------------|------------|---------------------|
| 1823   | 20    | 500 | 0.04 |
| 1823    | 5     | 100 | 0.05 | 
| 1823    | 15    | 600  | 0.025 | 
```
1. Alle Häufigkeiten addieren und durch die Summe der Textlängen teilen: $ {{20 + 5 + 15} \over {500 + 100 + 600}} = {{40} \over {1200}} = {0.033}$
2. Die relative Häufigkeiten addieren und durch die Anzahl an Tagen teilen: $ {{{20 \over 500} + {5 \over 100} + {15 \over 600}} \over 3} = {{0.04 + 0.05 + 0.025} \over 3} = 0.038$

Mit der zweiten Methode ist die relative Häufigkeit um 0.005 Prozentpunkte höher, da der kurze Text, der die höchste relative Häufigkeit aufweist, ein größeren Einfluss auf die Berechnung hat. 
`````
