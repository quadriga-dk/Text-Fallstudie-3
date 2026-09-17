(corpus-collection_metadata)=
# Metadaten

Metadaten sind Daten über Daten. Sie liefern kontextuelle Informationen, die helfen, die Bedeutung, Herkunft, Struktur und Nutzungsmöglichkeiten eines Datensatzes besser zu verstehen. In den Digital Humanities sind Metadaten unerlässlich, um die Volltextkorpora systematisch zu organisieren, auffindbar zu machen und deren inhaltliche und strukturelle Qualität zu sichern. Ein einfaches Beispiel: Bei einem Roman ist der Text selbst die eigentliche Datengrundlage, während Angaben *über* das Buch – etwa *Titel: „Die Geier-Wally", Autorin: Wilhelmine von Hillern, Jahr: 1873, Sprache: Deutsch* – die Metadaten bilden; ähnlich wie ein Bibliothekskatalog ein Buch beschreibt, ohne seinen Inhalt abzudrucken.

**Metadatenschemata**

Ein **Metadatenschema** ist ein standardisierter, gemeinschaftlich vereinbarter Satz von Feldern – oft *Elemente* genannt –, mit denen sich eine Ressource beschreiben lässt. Es legt fest, *welche* Angaben erfasst werden (etwa Titel, Urheber:in, Datum oder Sprache), wie diese Felder benannt sind und teilweise auch, in welcher Form sie auszufüllen sind. Ein einfaches Beispiel: Das verbreitete Schema *Dublin Core* gibt etwa vor, dass das Erscheinungsdatum stets im Feld namens `DC.date` und im Format `JJJJ-MM-TT` (Jahr–Monat–Tag) einzutragen ist. So benennt und schreibt jede:r dieselbe Angabe gleich, statt sie einmal „Jahr", einmal „erschienen" oder als „11. April 1873" zu erfassen.

Ein Schema wirkt damit wie ein gemeinsames Vokabular: Beschreiben verschiedene Personen, Institutionen oder Programme ihre Daten nach demselben Schema, werden die Metadaten untereinander vergleichbar, maschinell auswertbar und über Systemgrenzen hinweg austauschbar (interoperabel). Ohne ein solches Schema würde dagegen jede:r eigene, uneinheitliche Bezeichnungen verwenden, was die gemeinsame Nutzung und die Auffindbarkeit der Daten erheblich erschwert.

Es gibt verschiedene Metadatenschemata, die entwickelt wurden, um spezifische Anforderungen unterschiedlicher Disziplinen und Anwendungen zu erfüllen. Zu den bekanntesten gehören:

1. **<a href="https://www.dublincore.org/specifications/dublin-core/dces/" class="external-link" target="_blank">Dublin Core</a>**: Ein einfaches und weit verbreitetes Schema, das 15 grundlegende Elemente umfasst, wie Titel, Autor, Thema und Datum.
2. **<a href="https://tei-c.org/" class="external-link" target="_blank">TEI (Text Encoding Initiative)</a>**: Speziell für Texte entwickelt, bietet TEI detaillierte Richtlinien zur Auszeichnung von Texten und zur Erfassung von deren Metadaten im <a href="https://tei-c.org/release/doc/tei-p5-doc/de/html/ref-teiHeader.html" class="external-link" target="_blank"><code>&lt;teiHeader&gt;</code></a>.
3. **<a href="https://www.loc.gov/standards/mods/" class="external-link" target="_blank">MODS (Metadata Object Description Schema)</a>**: Von der Library of Congress entwickelt, bietet MODS eine umfangreichere Beschreibung als Dublin Core und ist besonders für bibliographische Informationen geeignet.
4. **<a href="https://www.loc.gov/standards/mets/" class="external-link" target="_blank">METS (Metadata Encoding and Transmission Standard)</a>**: Ein Standard zur Kodierung und Übertragung von Digitalisaten und deren Metadaten, häufig in Bibliotheken und Archiven verwendet.

```{admonition} TEI: Textrepräsentation und Metadatenschema in einem
:class: hinweis
TEI ist Ihnen im Abschnitt [Texte als digitale Objekte](corpus-collection_text_as_digital_objects) bereits als Format zur Repräsentation digitaler Texte begegnet – hier taucht es nun als Metadatenschema auf. Das ist kein Widerspruch: TEI ist ein einziger, umfassender XML-Standard, der beide Funktionen in einem Dokument vereint. Das `<text>`-Element kodiert den eigentlichen Text mit seiner Struktur und semantischen Auszeichnung, während der `<teiHeader>` die Metadaten zum Dokument enthält. Die übrigen hier genannten Schemata – Dublin Core, MODS und METS – beschreiben dagegen ausschließlich Metadaten und sagen nichts über die Auszeichnung des Textinhalts selbst aus.
```

## Metadaten zur Beschreibung eines Korpus

Bei der Beschreibung eines gesamten Korpus sind die Metadaten entscheidend, um den Kontext, den Umfang und die Struktur des Korpus zu dokumentieren. Wichtige Aspekte sind unter anderem:

- **Titel und Beschreibung**: Um das Korpus eindeutig zu identifizieren und dessen Inhalt zu beschreiben.
- **Ersteller:innen und/oder Herausgeber:innen**: Angaben zu den Personen oder Institutionen, die das Korpus erstellt und veröffentlicht haben.
- **Datum**: Zeitangaben zur Erstellung und Veröffentlichung des Korpus.
- **Umfang und Format**: Informationen über die Anzahl der enthaltenen Dokumente und deren Dateiformate.
- **Sprache**: Die im Korpus vertretenen Sprachen.

**Beispiel unter Verwendung Dublin Core**

Ein beispielhaftes Metadaten-Set für ein Korpus könnte unter Verwendung von Dublin Core so aussehen:

- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/" class="external-link" target="_blank">DC.title</a>**: "German Novel Corpus (ELTeC-deu)"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/source/" class="external-link" target="_blank">DC.source</a>**: <a href="https://zenodo.org/records/4662482" class="external-link" target="_blank">"https://zenodo.org/records/4662482"</a>
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/description/" class="external-link" target="_blank">DC.description</a>**: "the German novel collection for the ELTeC, the European Literary Text Collection, produced by the COST Action Distant Reading for European Literary History"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/" class="external-link" target="_blank">DC.creator</a>**: "Leonard Konle, Fotis Jannidis, Carolin Odebrecht, Lou Burnard"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/publisher/" class="external-link" target="_blank">DC.publisher</a>**: "COST Action 'Distant Reading for European Literary History'"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/" class="external-link" target="_blank">DC.date</a>**: "2021-04-11"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/" class="external-link" target="_blank">DC.format</a>**: "XML"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/" class="external-link" target="_blank">DC.language</a>**: "Deutsch"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/coverage/" class="external-link" target="_blank">DC.coverage</a>**: "1840-1920, Deutschland"

## Metadaten für einzelne Korpus-Elemente

Für einzelne Elemente eines Korpus, wie beispielsweise einzelne Artikel oder Dokumente, sind spezifische Metadaten notwendig, um diese präzise zu identifizieren und zu kontextualisieren. Wichtige Metadaten umfassen hier z.B.:

- **Titel und Autor:innen**: Um das Dokument eindeutig zu identifizieren.
- **Datum der Veröffentlichung**: Für zeitliche Einordnung.
- **Quelle**: Angaben zur ursprünglichen Publikation oder Fundort.
- **Sprache**: Die im Dokument verwendete Sprache.
- **Identifier**: Ein eindeutiger Identifikator wie eine DOI oder eine andere Art von Kennung.

**Beispiel unter Verwendung von Dublin Core**

Für ein einzelnes Buch könnten die Metadaten so aussehen:

- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/" class="external-link" target="_blank">DC.title</a>**: "Die Geier-Wally"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/" class="external-link" target="_blank">DC.creator</a>**: "Wilhelmine von Hillern"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/" class="external-link" target="_blank">DC.date</a>**: "1873"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/source/" class="external-link" target="_blank">DC.source</a>**: <a href="https://projekt-gutenberg.org/authors/wilhelmine-von-hillern/books/die-geier-wally/" class="external-link" target="_blank">"https://projekt-gutenberg.org/authors/wilhelmine-von-hillern/books/die-geier-wally/"</a>
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/" class="external-link" target="_blank">DC.language</a>**: "Deutsch"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/identifier/" class="external-link" target="_blank">DC.identifier</a>**: "Q1212872"

Durch die sorgfältige Erfassung und Verwaltung von Metadaten auf beiden Ebenen – sowohl für das gesamte Korpus als auch für einzelne Elemente – wird die Nutzbarkeit und Nachnutzbarkeit von Forschungsdaten in den Digital Humanities erheblich verbessert. Dies trägt zur besseren Auffindbarkeit, Nachvollziehbarkeit und langfristigen Erhaltung der Daten bei.
