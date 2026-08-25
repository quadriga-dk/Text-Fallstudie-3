(corpus-collection_corpora-as-research-objects)=
# Korpora als Forschungsobjekte der Digital Humanities

Für die Forschung in den textbasierten Digital Humanities hat sich das Korpus als das wichtigste *epistemische Objekt* herauskristallisiert – also als der zentrale Gegenstand, an dem und über den wissenschaftliche Erkenntnis gewonnen wird. Korpora lassen sich dabei vereinfacht verstehen als 

- Sammlungen von maschinenlesbaren (d.h. vom Computer automatisch verarbeitbaren) Textdokumenten, 
- die nach bestimmten Kriterien zusammengestellt wurden – etwa nach Entstehungszeitraum, Sprache, Textsorte, Publikationsort oder dem Vorkommen bestimmter Wörter (in unserer Fallstudie z.B. "Luft").

Eine besondere Variante von Korpora sind **Referenzkorpora**; sie sind so zusammengestellt, dass sie für einen bestimmten Bereich – eine sogenannte *Domäne*, etwa die deutsche Gegenwartssprache – möglichst repräsentativ sind, und dienen als allgemeine Vergleichsgrundlage, an der sich einzelne Texte oder kleinere Korpora messen lassen (ein Beispiel ist das *Deutsche Referenzkorpus, DeReKo*). 

In welchen **Datei- und Datenformaten** die Texte eines Korpus vorliegen, hängt davon ab, für welche Zwecke das Korpus aufgebaut wird (siehe zu Formaten auch den nächsten Abschnitt [Texte als digitale Objekte](corpus-collection_text_as_digital_objects)). 

Ein Korpus ist ein besonderer Typus einer **Datensammlung**: einer Menge von Datenobjekten – etwa Texten, Bildern oder Messwerten –, die für einen bestimmten (Forschungs-)Zweck zusammengestellt wird. Ausgewählt wird dabei nicht das Korpus als Ganzes, sondern seine Elemente. Für diese Auswahl hat {cite:t}`schoech2017` vier Strategien unterschieden, die für Datensammlungen allgemein und damit auch für Korpora gelten: 

## Vollständiges Korpus
Ein vollständiges Korpus umfasst alle verfügbaren Textobjekte zu einem spezifischen Gegenstandsbereich.

- **Voraussetzung:** klar begrenzte und gut dokumentierte Untersuchungsbereiche
- **Anwendung:** in der Regel nur für kleine Untersuchungsbereiche
- **Beispiel:** alle Gedichte von Friederike Mayröcker, alle Ausgaben der Berliner Morgenpost aus dem Jahr 1918
	
## Repräsentative Stichprobe
Die <a href="https://de.wikipedia.org/wiki/Grundgesamtheit" class="external-link" target="_blank">**Grundgesamtheit**</a> ist die Menge aller Texte, über die wir eine Aussage treffen wollen (z.B. alle deutschsprachigen Romane des 19. Jahrhunderts); eine **Stichprobe** ist eine daraus gezogene Teilmenge. **Repräsentativ** ist eine Stichprobe dann, wenn sie die **Variabilität** der Grundgesamtheit abbildet – also die ganze Bandbreite der Unterschiede zwischen den Texten, etwa nach Entstehungsjahrzehnt, Untergattung oder Autor:in. Ergebnisse, die an einer repräsentativen Stichprobe gewonnen werden, gelten dann auch für die Grundgesamtheit. Ob das gelingt, ist keine Frage des Fingerspitzengefühls, sondern das Ergebnis statistischer Operationen – allen voran der **Zufallsauswahl**.

Auf den ersten Blick wirkt es widersprüchlich, dass eine *zufällige* Auswahl *repräsentativ* sein soll. Tatsächlich ist die Zufallsauswahl aber gerade der Weg zur Repräsentativität: Würden wir die Texte gezielt "nach Gefühl" auswählen, flössen unweigerlich unsere eigenen Erwartungen und Vorlieben ein und verzerrten die Auswahl. Bei einer echten Zufallsstichprobe hat dagegen jeder Text der Grundgesamtheit dieselbe Chance, gezogen zu werden. Dadurch werden systematische Verzerrungen vermieden, und bei hinreichend großem Stichprobenumfang bildet die Stichprobe die Verteilung und Vielfalt der Grundgesamtheit mit hoher Wahrscheinlichkeit zuverlässig ab. Voraussetzung dafür ist, dass die Grundgesamtheit bekannt und vollständig dokumentiert ist – dass wir also überhaupt eine Liste aller infrage kommenden Texte besitzen, aus der gezogen werden kann. In der Praxis wird die reine Zufallsauswahl zudem oft verfeinert, indem man die Grundgesamtheit zunächst in Gruppen unterteilt (z.B. nach Jahrzehnten) und aus jeder Gruppe zufällig zieht – eine sogenannte *geschichtete Zufallsstichprobe* –, um sicherzustellen, dass alle relevanten Teilbereiche angemessen vertreten sind.

- **Voraussetzung:** bekannte und gut dokumentierte Grundgesamtheit; Zufallsauswahl der Texte
- **Anwendung:** für gültige Aussagen über die Grundgesamtheit; dient anderen Studien als Referenz
- **Beispiel:** 100 zufällig gezogene Romane aus dem 19. Jahrhundert, um die Vielfalt dieser Epoche zu untersuchen; siehe die Korpora der <a href="https://www.distant-reading.net/eltec/" class="external-link" target="_blank">European Literary Text Collection (ELTeC)</a>

## Balanciertes Korpus
Eine Auswahl, die die wesentlichen Merkmale des Gegenstandsbereichs möglichst **gleichmäßig** abdeckt. Nach Kriterien zusammengestellt sind alle Korpora – das Besondere ist hier, dass die verschiedenen Ausprägungen der gewählten Kriterien im Korpus in einem möglichst ausgewogenen Verhältnis vertreten sind (z.B. etwa gleich viele Texte pro Jahrzehnt).

- **Voraussetzung:** klar definierte Kriterien und gezielte Auswahl, um **statistische Korrelationen** zu vermeiden – also um zu verhindern, dass zwei Merkmale im Korpus immer gemeinsam auftreten und sich in der Analyse nicht mehr auseinanderhalten lassen (stammten z.B. alle frühen Texte von Männern und alle späten von Frauen, ließe sich ein beobachteter Unterschied nicht mehr eindeutig der *Zeit* oder dem *Geschlecht* zuschreiben)
- **Anwendung:** Untersuchung von Unterschieden und Entwicklungen, z.B. der literarischen Untergattungen des Romans
- **Beispiel:** Sammlung von Romanen verschiedener Jahrzehnte und Untergattungen; breite Variation von Erscheinungsjahrzehnt, Autor:in, Erzählperspektive und Handlungsort
	
## Opportunistisches Korpus
Die Auswahl wird durch die Verfügbarkeit der Daten geleitet: Aufgenommen wird, was bereits – etwa in digitaler Form – vorliegt.
 
- **Voraussetzung:** Verfügbarkeit der Daten, in der Regel in digitaler Form
- **Anwendung:** wenig erschlossene Forschungsbereiche, erste Explorationen
- **Grenze:** Es lässt sich nicht bestimmen, welchen Ausschnitt des Gegenstandsbereichs die Sammlung abbildet.
- **Beispiel:** Das <a href="https://github.com/tnhaider/DLK" class="external-link" target="_blank">"Deutsche Lyrik Korpus (DLK)"</a>, das alle verfügbaren Gedichte in deutscher Sprache zu aggregieren versucht, oder das <a href="https://dracor.org/ger" class="external-link" target="_blank">German Drama Corpus (GerDraCor)</a>, das sukzessive digital verfügbare deutschsprachige Dramen sammelt.

## Zusammenfassung 
Mit welcher Strategie und nach welchen Kriterien ein Korpus aufgebaut wird, entscheidet darüber, welche Forschungsfragen sich mit ihm überhaupt sinnvoll und belastbar beantworten lassen. Mit dem Korpusaufbau stellen wir also nicht nur Material zusammen, sondern schaffen den Gegenstand, über den unsere Forschung überhaupt Aussagen machen kann – eben das *epistemische Objekt*. Entsprechend umsichtig sollten wir bei diesem Vorgang vorgehen. Darüber hinaus ist eine Reflexion über die korpusbedingten Grenzen der Analyseergebnisse unabdingbarer Bestandteil von Digital Humanities-Forschungsprojekten.


`````{admonition} Weiterführende Links
:class: seealso
- <a href="https://fortext.net/routinen/methoden/korpusbildung" class="external-link" target="_blank">forTextArtikel "Korpusbildung"</a>,  mit Fokus auf literaturwissenschafliche Korpora. {cite:p}`fortext-2020-id-203`
`````

## Bibliographie
```{bibliography}
:filter: docname in docnames
```
