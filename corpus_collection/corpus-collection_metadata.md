(corpus-collection_metadata)=
# Metadaten

Metadaten sind Daten über Daten. Sie liefern kontextuelle Informationen, die helfen, die Bedeutung, Herkunft, Struktur und Nutzungsmöglichkeiten eines Datensatzes besser zu verstehen. In den Digital Humanities sind Metadaten unerlässlich, um die Volltextkorpora systematisch zu organisieren, auffindbar zu machen und deren inhaltliche und strukturelle Qualität zu sichern.

**Metadatenschemata**

Es gibt verschiedene Metadatenschemata, die entwickelt wurden, um spezifische Anforderungen unterschiedlicher Disziplinen und Anwendungen zu erfüllen. Zu den bekanntesten gehören:

1. **<a href="https://www.dublincore.org/specifications/dublin-core/dces/" class="external-link" target="_blank">Dublin Core</a>**: Ein einfaches und weit verbreitetes Schema, das 15 grundlegende Elemente umfasst, wie Titel, Autor, Thema und Datum.
2. **<a href="https://tei-c.org/" class="external-link" target="_blank">TEI (Text Encoding Initiative)</a>**: Speziell für Texte entwickelt, bietet TEI detaillierte Richtlinien zur Auszeichnung von Texten und zur Erfassung von deren Metadaten im [`<teiHeader>`](https://tei-c.org/release/doc/tei-p5-doc/de/html/ref-teiHeader.html).
3. **<a href="https://www.loc.gov/standards/mods/" class="external-link" target="_blank">MODS (Metadata Object Description Schema)</a>**: Von der Library of Congress entwickelt, bietet MODS eine umfangreichere Beschreibung als Dublin Core und ist besonders für bibliographische Informationen geeignet.
4. **<a href="https://www.loc.gov/standards/mets/" class="external-link" target="_blank">METS (Metadata Encoding and Transmission Standard)</a>**: Ein Standard zur Kodierung und Übertragung von Digitalisaten und deren Metadaten, häufig in Bibliotheken und Archiven verwendet.

## Metadaten zur Beschreibung eines Korpus

Bei der Beschreibung eines gesamten Korpus sind die Metadaten entscheidend, um den Kontext, den Umfang und die Struktur des Korpus zu dokumentieren. Wichtige Aspekte sind unter anderem:

- **Titel und Beschreibung**: Um das Korpus eindeutig zu identifizieren und dessen Inhalt zu beschreiben.
- **Ersteller:innen und/oder Herausgeber:innen**: Angaben zu den Personen oder Institutionen, die das Korpus erstellt und veröffentlicht haben.
- **Datum**: Zeitangaben zur Erstellung und Veröffentlichung des Korpus.
- **Umfang und Format**: Informationen über die Anzahl der enthaltenen Dokumente und deren Dateiformate.
- **Sprache**: Die im Korpus vertretenen Sprachen.

**Beispiel unter Verwendung Dublin Core**

Ein beispielhaftes Metadaten-Set für ein Korpus könnte unter Verwendung von Dublin Core so aussehen:

- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/" class="external-link" target="_blank">DC.title</a>**: "Corpus of German-Language Fiction"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/source/" class="external-link" target="_blank">DC.source</a>**: "https://doi.org/10.6084/m9.figshare.4524680"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/description/" class="external-link" target="_blank">DC.description</a>**: "Contains 2,735 German-language prose works (mainly novels and short stories) by 549 authors, spanning from ca. 1510 to the 1940s (the bulk of texts is from 1840–1930). Texts were extracted from the Gutenberg-DE Edition 13 DVD-ROM (released in November, 2013) and converted from HTML to TXT."
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/" class="external-link" target="_blank">DC.creator</a>**: "Frank Fischer, Jannik Strötgen"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/publisher/" class="external-link" target="_blank">DC.publisher</a>**: "Frank Fischer, Jannik Strötgen"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/" class="external-link" target="_blank">DC.date</a>**: "2017-01-06"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/" class="external-link" target="_blank">DC.format</a>**: "TXT"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/" class="external-link" target="_blank">DC.language</a>**: "Deutsch"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/coverage/" class="external-link" target="_blank">DC.coverage</a>**: "1510-1940, Deutschland"

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
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/" class="external-link" target="_blank">DC.creator</a>**: "Wilhemine von Hillern"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/date/" class="external-link" target="_blank">DC.date</a>**: "1873"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/source/" class="external-link" target="_blank">DC.source</a>**: "https://projekt-gutenberg.org/authors/wilhelmine-von-hillern/books/die-geier-wally/"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/language/" class="external-link" target="_blank">DC.language</a>**: "Deutsch"
- **<a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/identifier/" class="external-link" target="_blank">DC.identifier</a>**: "Q1212872"

Durch die sorgfältige Erfassung und Verwaltung von Metadaten auf beiden Ebenen – sowohl für das gesamte Korpus als auch für einzelne Elemente – wird die Nutzbarkeit und Nachnutzbarkeit von Forschungsdaten in den Digital Humanities erheblich verbessert. Dies trägt zur besseren Auffindbarkeit, Nachvollziehbarkeit und langfristigen Erhaltung der Daten bei.
