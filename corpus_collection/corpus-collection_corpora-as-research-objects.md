(corpus-collection_corpora-as-research-objects)=
# Korpora als Forschungsobjekte der Digital Humanities

Für die Forschung in den textbasierten Digital Humanities hat sich das Korpus als das wichtigste epistemische Objekt herauskristallisiert. Korpora lassen sich dabei vereinfacht verstehen als 

- Sammlungen von maschinenlesbaren Textdokumenten, 
- die nach bestimmten Kriterien zusammengestellt wurden.

Eine besondere Variante von Korpora sind Referenzkorpora; bei ihnen wird besonders darauf geachtet, dass sie für eine bestimmte Domäne repräsentativ sein können. 

In welchen Formaten die Texte in einem Korpus vorliegen, hängt davon ab, für welche Zwecke ein Korpus aufgebaut wird (siehe zu Formaten auch den nächsten Abschnitt [Texte als digitale Objekte](corpus-collection_text_as_digital_objects)). 

Die Elemente eines Korpus können nach unterschiedlichen Strategien mit jeweils spezifischen Kriterien ausgewählt werden. Ein Korpus ist dabei ein besonderer Typus einer **Datensammlung** – also einer Menge von Datenobjekten (etwa Texten, Bildern oder Messwerten), die gezielt für einen bestimmten (Forschungs-)Zweck zusammengestellt wird. Für Datensammlungen insgesamt – und damit auch für Korpora – hat {cite:t}`schoech2017` vier Auswahlstrategien unterschieden: 

## Vollständiges Korpus
Ein vollständiges Korpus umfasst alle verfügbaren Textobjekte zu einem spezifischen Gegenstandsbereich.

- **Voraussetzung:** Möglich bei klar begrenzten und gut dokumentierten Untersuchungsbereichen. 
- **Anwendung:** Geeignet in der Regel nur für kleine, klar definierbare Untersuchungsbereiche.
- **Beispiel:** Alle Gedichte von Friederike Mayröcker oder alle Ausgaben der Berliner Morgenpost aus dem Jahr 1918
	
## Repräsentative Stichprobe
Eine Stichprobe, die die gesamte Variabilität der <a href="https://de.wikipedia.org/wiki/Grundgesamtheit" class="external-link" target="_blank">Grundgesamtheit</a> abbildet. Repräsentativität ist dabei das Ergebnis statistischer Operationen.

Dabei ist die **Grundgesamtheit** die Menge aller Texte, über die wir eine Aussage treffen wollen (z.B. alle deutschsprachigen Romane des 19. Jahrhunderts), und die **Stichprobe** eine daraus gezogene Teilmenge. Repräsentativ ist sie, wenn sie die Vielfalt der Grundgesamtheit so gut abbildet, dass Ergebnisse aus der Stichprobe auch für die gesamte Grundgesamtheit gelten.

Auf den ersten Blick wirkt es widersprüchlich, dass eine *zufällige* Auswahl *repräsentativ* sein soll. Tatsächlich ist die Zufallsauswahl aber gerade der Weg zur Repräsentativität: Würden wir die Texte gezielt "nach Gefühl" auswählen, flössen unweigerlich unsere eigenen Erwartungen und Vorlieben ein und verzerrten die Auswahl. Bei einer echten Zufallsstichprobe hat dagegen jeder Text der Grundgesamtheit dieselbe Chance, gezogen zu werden. Dadurch werden systematische Verzerrungen vermieden, und bei hinreichend großem Stichprobenumfang bildet die Stichprobe die Verteilung und Vielfalt der Grundgesamtheit mit hoher Wahrscheinlichkeit zuverlässig ab. Voraussetzung dafür ist, dass die Grundgesamtheit bekannt und vollständig dokumentiert ist – dass wir also überhaupt eine Liste aller infrage kommenden Texte besitzen, aus der gezogen werden kann. In der Praxis wird die reine Zufallsauswahl zudem oft verfeinert, indem man die Grundgesamtheit zunächst in Gruppen unterteilt (z.B. nach Jahrzehnten) und aus jeder Gruppe zufällig zieht – eine sogenannte *geschichtete Zufallsstichprobe* –, um sicherzustellen, dass alle relevanten Teilbereiche angemessen vertreten sind.

- **Voraussetzung:** Grundgesamtheit muss bekannt und gut dokumentiert sein; Zufällige Auswahl der Datensätze ist erforderlich.
- **Anwendung:** Ermöglicht gültige Aussagen über die Grundgesamtheit und dient als Referenz für andere Studien.
- **Beispiel:** Eine repräsentative Auswahl von 100 Romanen aus dem 19. Jahrhundert, die zufällig ausgewählt wurden, um die Vielfalt dieser Epoche zu repräsentieren; siehe die Korpora der <a href="https://www.distant-reading.net/eltec/" class="external-link" target="_blank">European Literary Text Collection (ELTeC)</a>

## Balanciertes Korpus
Eine gezielt nach bestimmten Kriterien zusammengestellte Auswahl, die alle wesentlichen Merkmale des Gegenstandsbereichs möglichst gleichmäßig abdeckt.

- **Voraussetzung:** Klar definierte Kriterien und gezielte Auswahl, um statistische Korrelationen zu vermeiden – also um zu verhindern, dass zwei Merkmale im Korpus immer gemeinsam auftreten und sich in der Analyse deshalb nicht mehr auseinanderhalten lassen. (Stammten z.B. alle frühen Texte von Männern und alle späten von Frauen, ließe sich ein beobachteter Unterschied nicht mehr eindeutig der *Zeit* oder dem *Geschlecht* zuschreiben; ein balanciertes Korpus verteilt die Merkmale daher möglichst gleichmäßig.)
- **Anwendung:** Ideal für Studien, die Unterschiede und Entwicklungen innerhalb einer Kategorie analysieren wollen, z.B. die Entwicklung literarischer Untergattungen des Romans. 
- **Beispiel:** Eine Sammlung von Romanen aus verschiedenen Jahrzehnten und Untergattungen, mit breiter Variation in Autoren, Erzählperspektiven und Handlungsorten, Untergattungen.
	
## Opportunistisches Korpus
Eine Sammlung, deren Auswahl nur durch die Verfügbarkeit von Daten geleitet wird.
 
- **Voraussetzung:** Digitale Verfügbarkeit der Daten.
- **Anwendung:** Geeignet für wenig erschlossene Forschungsbereiche oder erste Explorationen, bleibt allerdings insgesamt unbefriedigend, da nicht beurteilt werden kann, was die Sammlung abbildet. 
- **Beispiel:** Das <a href="https://github.com/tnhaider/DLK" class="external-link" target="_blank">"Deutsche Lyrik Korpus (DLK)"</a>, das alle verfügbaren Gedichte in deutscher Sprache zu aggregieren versucht, oder das <a href="https://dracor.org/ger" class="external-link" target="_blank">German Drama Corpus (GerDraCor)</a>, das sukzessive digital verfügbare deutschsprachige Dramen sammelt.

## Zusammenfassung 
Mit welcher Strategie und nach welchen Kriterien ein Korpus aufgebaut wird, entscheidet darüber, welche Forschungsfragen sich mit ihm überhaupt sinnvoll und belastbar beantworten lassen. Mit dem Korpusaufbau wird dabei das epistemische Objekt der Forschung konstruiert. Entsprechend reflektiert sollten wir bei diesem Vorgang vorgehen. Darüber hinaus ist eine Reflektion auf die korpusbedingten Grenzen der Analyseergebnisse unabdingbarer Bestandteil von Digital Humanities-Forschungsprojekten.


`````{admonition} Weiterführende Links
:class: seealso
- <a href="https://fortext.net/routinen/methoden/korpusbildung" class="external-link" target="_blank">forTextArtikel "Korpusbildung"</a>,  mit Fokus auf literaturwissenschafliche Korpora. {cite:p}`fortext-2020-id-203`
`````

## Bibliographie
```{bibliography}
:filter: docname in docnames
```



