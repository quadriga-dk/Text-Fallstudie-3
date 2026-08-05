---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# 🏆Selbsttest: Wissen und Praxis

````{admonition} Hinweis
:class: hinweis
Mit diesen Übungsaufgaben können Sie sich selbst einschätzen und das im Kapitel Gelernte reflektieren.

Sie können die Fragen in beliebiger Reihenfolge beantworten und auch mehrfach versuchen. 

**So funktioniert es:**
- Wählen Sie bei jeder Frage die Antwort(en), die Sie für richtig halten
- Lesen Sie das Feedback zu den einzelnen Antwortoptionen sorgfältig durch
- Die Erklärungen helfen Ihnen, Ihr Verständnis zu vertiefen – auch bei korrekten Antworten 

Ihre Ergebnisse werden weder bewertet noch gespeichert. Nutzen Sie dieses Assessment, um Wissenslücken zu identifizieren und gegebenenfalls die entsprechenden Abschnitte des Kapitels noch einmal zu bearbeiten. 

**Geschätzte Zeit**: 1h 15min

Viel Erfolg!
````

## Frage 1
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

"""
Lernziel: 
    Sie können Korpora als geisteswissenschaftliche Forschungsobjekte definieren und ihre wesentlichen Merkmale beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice + Zuordnungsaufgabe
Geschätzte Zeit: 5 Minuten
Schwerpunkte:
    - Verständnis der Korpus-Grundprinzipien
    - Unterscheidung von Korpustypen
    - Bewertung von Korpusqualität
"""


question1 = [
    {
        "question": "Welche der folgenden Aussagen beschreiben korrekt die wesentlichen Merkmale eines Korpus in den Digital Humanities? Wählen Sie alle zutreffenden Aussagen.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Eine Sammlung von maschinenlesbaren Textdokumenten",
                "correct": True,
                "feedback": """✓ Korrekt! Die Maschinenlesbarkeit ist ein zentrales Merkmal von DH-Korpora, da sie die computergestützte Analyse ermöglicht. Dies unterscheidet DH-Korpora von traditionellen Textsammlungen und ist Voraussetzung für quantitative Analysen."""
            },
            {
                "answer": "Eine nach bestimmten Kriterien zusammengestellte Textsammlung",
                "correct": True,
                "feedback": """✓ Korrekt! Die kriteriengeleitete Zusammenstellung ist essentiell für wissenschaftliche Korpora. Die Kriterien müssen dabei transparent dokumentiert sein, zur Forschungsfrage passen und systematisch angewendet werden."""
            },
            {
                "answer": "Eine Sammlung, die nur digitalisierte Bücher enthält",
                "correct": False,
                "feedback": """× Nicht korrekt. Korpora können verschiedene Arten von Texten enthalten: literarische Texte (wie in unserer Fallstudie), Zeitungsartikel, Dokumente und andere Textformen. Die Art der Texte wird durch die Forschungsfrage bestimmt, nicht durch das Format."""
            },
            {
                "answer": "Eine Textsammlung, die spezifischen Forschungszwecken dient",
                "correct": True,
                "feedback": """✓ Korrekt! Die Zweckgebundenheit ist ein wichtiges Merkmal: Das Korpus wird für bestimmte Forschungsfragen zusammengestellt, die Forschungszwecke bestimmen die Auswahlkriterien und die Zweckbindung beeinflusst auch die Art der Aufbereitung der Texte."""
            },
            {
                "answer": "Eine Sammlung digitalisierter Texte, deren Zusammenstellung weder dokumentiert noch durch einen Forschungszweck motiviert ist",
                "correct": False,
                "feedback": """× Nicht korrekt. Entscheidend ist nicht, wie streng die Auswahl eingeschränkt wird, sondern dass die Auswahlentscheidungen dokumentiert und auf einen Forschungszweck bezogen sind. Auch ein opportunistisches Korpus (siehe Abschnitt "Korpora als Forschungsobjekte") folgt einem nachvollziehbaren Kriterium – der digitalen Verfügbarkeit – und ist ein wissenschaftliches Korpus. Eine Sammlung ohne jede dokumentierte Auswahlentscheidung lässt sich dagegen nicht methodisch einordnen, weil unklar bleibt, was sie abbildet."""
            },
            {
                "answer": "Eine Sammlung, die immer alle verfügbaren Texte zu einem Thema enthalten muss",
                "correct": False,
                "feedback": """× Nicht korrekt. Vollständigkeit ist nur eine mögliche Strategie des Korpusaufbaus: Wie im Text erläutert, gibt es verschiedene Strategien (z.B. repräsentative Stichproben), die Vollständigkeit ist nur bei klar begrenzten, kleinen Untersuchungsbereichen sinnvoll und die Strategie der Korpuserstellung richtet sich nach der Forschungsfrage und praktischen Erwägungen."""
            }
        ]
    }
]
display_quiz(question1, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 2

Welche Aussage trifft auf das jeweilige Textformat zu? Wählen Sie für jede Aussage das passende Format.

### Frage 2(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

"""
Lernziel:
    Sie können die vier Hauptformate digitaler Texte (Bilddigitalisate, Plain Text, XML/TEI, CSV) anhand ihrer charakteristischen Eigenschaften unterscheiden und deren Vor- und Nachteile für spezifische Anwendungsfälle analysieren.
Bloom-Stufe: Analysieren
Format: Vergleichsmatrix + Multiple Choice
Geschätzte Zeit: 15 Minuten
Schwerpunkte:
    - Eigenschaften digitaler Textformate
    - Vor- und Nachteile verschiedener Formate
    - Formatauswahl für spezifische Zwecke
"""

statements = [
    {
        "question": "Dieses Format eignet sich besonders für linguistische Annotationen wie Wortarten und Lemmata in tabellarischer Form.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "CSV",
                "correct": True,
                "feedback": "✓ Korrekt! Die tabellarische Struktur ermöglicht eine klare Zuordnung von Token und Annotationen, sie lässt sich einfach mit Analysewerkzeugen verarbeiten, ist gut für große Datenmengen geeignet und ist das Standardformat für viele linguistische Tools."
            },
            {
                "answer": "XML/TEI",
                "correct": False,
                "feedback": """× Nicht optimal. Obwohl XML/TEI auch Annotationen unterstützt, ist der Aufbau komplexer als nötig für einfache tabellarische Daten und weniger effizient für große Mengen einfach strukturierter Annotationen."""
            },
            {
                "answer": "Plain Text",
                "correct": False,
                "feedback": """× Nicht korrekt, weil keine Strukturierung für Annotationen möglich ist und keine Möglichkeit besteht, zusätzliche Informationen systematisch zu speichern."""
            },
            {
                "answer": "Bilddigitalisate",
                "correct": False,
                "feedback": """× Nicht optimal, weil keine maschinenlesbare Textstruktur und keine Möglichkeit für systematische Annotationen vorhanden ist."""
            }
        ]
    }
]
display_quiz(statements, colors=colors.jupyterquiz)
```


### Frage 2(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

statements = [
    {
        "question": "Dieses Format bewahrt die ursprüngliche visuelle Erscheinung des Dokuments, ist aber nicht direkt maschinenlesbar.",
        "type": "multiple_choice",
        "answers":  [
            {
                "answer": "CSV",
                "correct": False,
                "feedback": """× Nicht korrekt, weil CSV nur tabellarische Daten speichert, keine visuellen Informationen enthält und primär für strukturierte Daten gedacht ist."""
            },
            {
                "answer": "XML/TEI",
                "correct": False,
                "feedback": """× Nicht ganz korrekt. XML/TEI kann zwar Layoutinformationen beschreiben, bewahrt aber nicht das visuelle Erscheinungsbild selbst und ist bereits maschinenlesbar."""
            },
            {
                "answer": "Plain Text",
                "correct": False,
                "feedback": """× Nicht korrekt, weil alle Formatierungen verloren gehen, nur der reine Text erhalten bleibt und keine visuellen Informationen gespeichert werden."""
            },
            {
                "answer": "Bilddigitalisate",
                "correct": True,
                "feedback": """✓ Korrekt! Bilddigitalisate (PDF, PNG, JPG) sind ideal dafür, weil sie Layout und Typographie originalgetreu bewahren, Illustrationen und grafische Elemente erhalten und als historische Referenz dienen können. Allerdings benötigen sie OCR für Textanalysen."""
            }
        ]
    }
]
display_quiz(statements, colors=colors.jupyterquiz)
```

## Frage 3

**Szenario:** Ein Forschungsprojekt möchte ein Korpus digitalisierter Romane des 19. Jahrhunderts erstellen, das:
- für automatische Textanalysen nutzbar ist
- die ursprüngliche Seitengestaltung der historischen Buchausgaben dokumentiert
- langfristig archiviert werden soll

**Frage:** Welches Format oder Kombination von Formaten würden Sie empfehlen?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('korpus-1')
```

````{admonition}  Lösungen
:class: solution, dropdown
**Musterlösung:** XML oder Kombination aus Bilddigitalisaten (PDF) und Plain Text

**Begründung:**
XML:
- kann sowohl Text als auch Informationen zum originalen Layout in spezialisierten Tags speichern
- kann Text und Bildinformationen verknüpfen
- ermöglicht automatische Textanalysen
- eignet sich zur Langzeitarchivierung
- Nachteil: Die Verarbeitung ist komplexer als die von Plain Text

Bilddigitalisate (PDF):
- Bewahren das originale Layout
- Dienen als Referenz
- Eignen sich für die Langzeitarchivierung
- Nachteil: automatische Prozessierung und Verknüpfung zu Plain Text ist nicht möglich

Plain Text (nach OCR):
- Ermöglicht automatische Textanalysen  
- Einfach zu verarbeiten
- Geringer Speicherbedarf

Alternative Ansätze:
- CSV ist nicht geeignet für Volltext
- Nur Bilddigitalisate würden Analysen erschweren
- Nur Plain Text dokumentiert die ursprüngliche Seitengestaltung nicht
````
## Frage 4
(Wählen Sie alle zutreffenden Antworten aus)

### Frage 4(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

format_questions = [
    {
        "question": "Welche der folgenden Formate sind direkt maschinenlesbar? (Mehrere Antworten können korrekt sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Bilddigitalisate",
                "correct": False,
                "feedback": "Falsch. Bilddigitalisate benötigen erst OCR (Optical Character Recognition), um für Maschinen lesbar zu werden. Die Inhalte sind für Computer nicht direkt zugänglich."
            },
            {
                "answer": "Plain Text",
                "correct": True,
                "feedback": "Richtig. Text in einfachen Textdateien kann direkt von Algorithmen gelesen und verarbeitet werden."
            },
            {
                "answer": "XML/TEI",
                "correct": True,
                "feedback": "Richtig. XML und TEI sind strukturierte Textformate, die von Computern direkt verarbeitet werden können."
            },
            {
                "answer": "CSV",
                "correct": True,
                "feedback": "Richtig. Comma-Separated Values sind strukturierte Daten, die direkt maschinenlesbar sind."
            }
        ]
    }
]

display_quiz(format_questions, colors=colors.jupyterquiz)
```

### Frage 4(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

format_questions = [
    {
        "question": "Welche der folgenden Formate können Formatierungen (z.B. Kursivierung / Fettung) darstellen oder speichern? (Mehrere Antworten können korrekt sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Bilddigitalisate",
                "correct": True,
                "feedback": "Richtig. Sie bewahren alle visuellen Formatierungen des Originaldokuments."
            },
            {
                "answer": "Plain Text",
                "correct": False,
                "feedback": "Falsch. In reinen Textdateien können keine Formatierungen (wie Fettdruck, Kursiv, etc.) gespeichert werden."
            },
            {
                "answer": "XML/TEI",
                "correct": True,
                "feedback": "Richtig. Diese Formate können Formatierungen strukturiert beschreiben und kodieren."
            },
            {
                "answer": "CSV",
                "correct": False,
                "feedback": "Falsch. CSV-Dateien können nur tabellarische Strukturen speichern, aber keine Textformatierungen."
            }
        ]
    }
]

display_quiz(format_questions, colors=colors.jupyterquiz)
```

### Frage 4(c)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

format_questions = [
    {
        "question": "Welche der folgenden Formate eignen sich für linguistische Annotationen? (Mehrere Antworten können korrekt sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Bilddigitalisate",
                "correct": False,
                "feedback": "Falsch. Ohne Textextraktion können keine linguistischen Informationen hinzugefügt werden."
            },
            {
                "answer": "Plain Text",
                "correct": True,
                "feedback": "Teilweise richtig. Grundlegende Annotationen können durch zusätzliche Zeichen eingefügt werden, aber die Möglichkeiten sind sehr begrenzt."
            },
            {
                "answer": "XML/TEI",
                "correct": True,
                "feedback": "Richtig. Diese Formate wurden speziell für strukturierte Textannotationen entwickelt und eignen sich hervorragend für linguistische Informationen."
            },
            {
                "answer": "CSV",
                "correct": True,
                "feedback": "Teilweise richtig. Tabellarische Strukturen können linguistische Merkmale in separaten Spalten speichern, sind aber für komplexe hierarchische Annotationen weniger geeignet."
            }
        ]
    }
]

display_quiz(format_questions, colors=colors.jupyterquiz)
```

### Frage 4(d)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

format_questions = [
    {
        "question": "Zusatzfrage: Welche der folgenden Formate sind besonders speichereffizient? (Mehrere Antworten können korrekt sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Bilddigitalisate",
                "correct": False,
                "feedback": "Falsch. Bilddateien benötigen in der Regel viel Speicherplatz, besonders bei hoher Auflösung."
            },
            {
                "answer": "Plain Text",
                "correct": True,
                "feedback": "Richtig. Reiner Text ohne Metadaten oder Formatierungen braucht sehr wenig Speicherplatz."
            },
            {
                "answer": "XML/TEI",
                "correct": False,
                "feedback": "Falsch. Durch die zusätzlichen Tags und strukturellen Informationen benötigen diese Formate mehr Speicherplatz als Plain Text."
            },
            {
                "answer": "CSV",
                "correct": True,
                "feedback": "Richtig. Tabellarische Daten in CSV-Format sind sehr speichereffizient für strukturierte Informationen."
            }
        ]
    }
]

display_quiz(format_questions, colors=colors.jupyterquiz)
```

### Frage 4(e)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

format_questions = [
    {
        "question": "Welche der folgenden Formate bewahren visuelle Informationen? (Mehrere Antworten können korrekt sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Bilddigitalisate",
                "correct": True,
                "feedback": "Richtig. Sie enthalten die vollständige visuelle Information des Originaldokuments."
            },
            {
                "answer": "Plain Text",
                "correct": False,
                "feedback": "Falsch. Visuelle Informationen wie Layout, Schriftarten oder Bilder gehen in Plain Text vollständig verloren."
            },
            {
                "answer": "XML/TEI",
                "correct": True,
                "feedback": "Teilweise richtig. Layout und visuelle Strukturen können beschrieben werden, aber die tatsächlichen visuellen Informationen werden nicht direkt gespeichert."
            },
            {
                "answer": "CSV",
                "correct": False,
                "feedback": "Falsch. CSV-Dateien speichern nur tabellarische Daten ohne visuelle Informationen."
            }
        ]
    }
]

display_quiz(format_questions, colors=colors.jupyterquiz)
```

## Frage 5
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel:
    Sie können die grundlegenden Metadatenschemata (Dublin Core, TEI, MODS, METS) und deren charakteristische Elemente für Korpora und Einzeldokumente beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice + Selbsteinschätzung
Zeitaufwand: 25 Minuten
Schwerpunkte:
    - Verständnis verschiedener Metadatenschemata (Dublin Core, TEI, MODS, METS)
    - Kenntnis charakteristischer Elemente 
    - Unterscheidung Korpus- und Dokumentebene
"""

question5 = [
    {
        "question": "Welche Aussagen beschreiben die verschiedenen Metadatenschemata korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core umfasst 15 grundlegende Elemente wie Titel, Autor und Datum",
                "correct": True,
                "feedback": """✓ Richtig! Dublin Core bietet ein einfaches, universelles Schema, dessen 15 Kernelemente standardisiert sind, eignet sich für grundlegende Beschreibungen und ist weit verbreitet und leicht anzuwenden."""
            },
            {
                "answer": "TEI wurde speziell für die Auszeichnung von Texten entwickelt und speichert Metadaten im teiHeader",
                "correct": True,
                "feedback": """✓ Richtig! TEI ist ein spezialisiertes Schema für Texte, nutzt den teiHeader für Metadaten, ermöglicht detaillierte Textauszeichnung und bietet umfangreiche Beschreibungsmöglichkeiten."""
            },
            {
                "answer": "MODS und METS sind identische Standards für Bibliotheken",
                "correct": False,
                "feedback": """× Nicht korrekt. Die Standards unterscheiden sich: MODS ist für bibliographische Beschreibungen gedacht, METS dient der Kodierung und Übertragung von Digitalisaten, und beide haben unterschiedliche Schwerpunkte und Anwendungsbereiche."""
            },
            {
                "answer": "Dublin Core wurde speziell für die detaillierte Auszeichnung von Volltexten entwickelt",
                "correct": False,
                "feedback": """× Nicht korrekt. Dublin Core ist bewusst einfach gehalten und universell einsetzbar, mit 15 grundlegenden Elementen zur Beschreibung von Ressourcen. Für die detaillierte Auszeichnung von Volltexten wurde hingegen TEI entwickelt."""
            }
        ]
    }
]
display_quiz(question5, colors=colors.jupyterquiz)
```

## Frage 6

### Frage 6(a)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_questions = [
    {
        "question": """Zu welchem Metadatenschema gehört das Element "teiHeader"?""",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core",
                "correct": False,
                "feedback": """× Falsch. Der "teiHeader" ist ein Element aus dem TEI-Schema, nicht aus Dublin Core."""
            },
            {
                "answer": "TEI",
                "correct": True,
                "feedback": """✓ Richtig. Der "teiHeader" ist ein zentrales Element des TEI-Schemas (Text Encoding Initiative) und dient der strukturierten Beschreibung von Metadaten in TEI-Dokumenten."""
            },
            {
                "answer": "MARC",
                "correct": False,
                "feedback": """× Falsch. MARC ist ein bibliothekarisches Metadatenformat und enthält kein "teiHeader"-Element."""
            },
            {
                "answer": "MODS",
                "correct": False,
                "feedback": """× Falsch. MODS (Metadata Object Description Schema) ist ein XML-Schema für bibliografische Metadaten, aber enthält kein "teiHeader"-Element."""
            }
        ]
    }
]

display_quiz(metadata_questions, colors=colors.jupyterquiz)
```

### Frage 6(b)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_questions = [
    {
        "question": """Zu welchem Metadatenschema gehört das Element "DC.coverage"?""",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core",
                "correct": True,
                "feedback": """✓ Richtig. \"DC.coverage\" ist ein Element aus dem Dublin Core Metadatenstandard, das räumliche und zeitliche Angaben zum beschriebenen Objekt enthält."""
            },
            {
                "answer": "TEI",
                "correct": False,
                "feedback": """× Falsch. Obwohl TEI Dublin Core Elemente integrieren kann, ist \"DC.coverage\" kein genuines TEI-Element."""
            },
            {
                "answer": "MARC",
                "correct": False,
                "feedback": """× Falsch. MARC verwendet andere Bezeichnungen für räumliche und zeitliche Abdeckungen."""
            },
            {
                "answer": "MODS",
                "correct": False,
                "feedback": """× Falsch. MODS hat eigene Elemente für geografische und chronologische Informationen."""
            }
        ]
    }
]

display_quiz(metadata_questions, colors=colors.jupyterquiz)
```
### Frage 6(c)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_questions = [
    {
        "question": """Auf welcher Beschreibungsebene wird das "DC.coverage"-Element in dieser Fallstudie verwendet?""",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Nur auf Korpus-Level",
                "correct": True,
                "feedback": """✓ Richtig. In dieser Fallstudie beschreibt "DC.coverage" die zeitliche und räumliche Abdeckung der gesamten Sammlung – im Beispiel des ELTeC-deu-Korpus etwa "1840-1920, Deutschland". Es definiert damit den Rahmen der Sammlung und ist wichtig für die Gesamteinordnung des Korpus. (Grundsätzlich erlaubt Dublin Core das Element auch auf Dokumentebene – in unserem Metadaten-Set kommt es dort aber nicht vor.)"""
            },
            {
                "answer": "Nur auf Dokument-Level",
                "correct": False,
                "feedback": """× Falsch. In dieser Fallstudie wird "DC.coverage" nicht auf Dokumentebene verwendet: Die Einzeldokumente – wie im Beispiel "Die Geier-Wally" – werden über Elemente wie DC.title, DC.creator, DC.date und DC.identifier beschrieben."""
            },
            {
                "answer": "Sowohl auf Korpus- als auch auf Dokument-Level",
                "correct": False,
                "feedback": """× Falsch. Grundsätzlich ließe sich "DC.coverage" zwar auf beiden Ebenen einsetzen, in dieser Fallstudie wird es aber ausschließlich auf Korpus-Level verwendet, um die zeitliche und räumliche Abdeckung der Gesamtsammlung anzugeben."""
            },
            {
                "answer": "Auf keiner der genannten Ebenen",
                "correct": False,
                "feedback": """× Falsch. "DC.coverage" wird in dieser Fallstudie durchaus verwendet – und zwar auf Korpus-Level, um die zeitliche und räumliche Abdeckung der Sammlung zu beschreiben."""
            }
        ]
    }
]

display_quiz(metadata_questions, colors=colors.jupyterquiz)
```


## Frage 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

question7 = [
    {
        "question": "Welche Metadatenelemente sind charakteristisch für die Beschreibung einzelner Korpus-Dokumente?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Eindeutiger Identifikator (z.B. DOI oder spezifische Kennung)",
                "correct": True,
                "feedback": """✓ Richtig! Ein eindeutiger Identifikator ist essentiell für die Dokumentidentifikation, ermöglicht präzise Referenzierung, unterstützt die Langzeitarchivierung und erleichtert die Verknüpfung von Dokumenten."""
            },
            {
                "answer": "Gesamtumfang des Korpus",
                "correct": False,
                "feedback": """× Nicht korrekt! Der Gesamtumfang ist ein Korpus-Level-Metadatum, beschreibt die gesamte Sammlung und gehört nicht zur Dokumentbeschreibung."""
            }
        ]
    }
]
display_quiz(question7, colors=colors.jupyterquiz)
```
````{admonition} Lösungen
:class: solution, dropdown
Für Einzeldokumente sind stattdessen relevant:
- Individuelle Eigenschaften
- Spezifische Publikationsdaten
- Dokumentspezifische Merkmale
````

## Frage 8

### Frage 8(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_schema_questions = [
    {
        "question": "Welches Metadatenschema wird als \"einfach und universell verwendbar, mit grundlegenden Elementen\" beschrieben?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core",
                "correct": True,
                "feedback": """✓ Richtig. Dublin Core ist bewusst einfach gehalten, universal einsetzbar und besteht aus 15 Kernelementen, die grundlegend für die Beschreibung digitaler Ressourcen sind. Es ist weit verbreitet und international standardisiert."""
            },
            {
                "answer": "TEI",
                "correct": False,
                "feedback": """× Falsch. TEI ist ein komplexeres Schema, das speziell für die Auszeichnung und Beschreibung von Texten entwickelt wurde, nicht primär für universelle Einfachheit."""
            },
            {
                "answer": "MARC",
                "correct": False,
                "feedback": """× Falsch. MARC ist ein umfassendes Format für bibliographische Informationen, aber nicht als besonders einfach oder universell bekannt."""
            },
            {
                "answer": "METS",
                "correct": False,
                "feedback": """× Falsch. METS ist ein XML-Schema für Metadaten zu digitalen Objekten in Repositorien, aber nicht primär für Einfachheit konzipiert."""
            }
        ]
    }
]

display_quiz(metadata_schema_questions, colors=colors.jupyterquiz)
```
### Frage 8(b)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_schema_questions = [
    {
        "question": "Welches Metadatenschema wird als \"spezialisiert auf Textauszeichnung und -beschreibung\" charakterisiert?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core",
                "correct": False,
                "feedback": """× Falsch. Dublin Core bietet allgemeine Metadatenelemente, ist aber nicht speziell für detaillierte Textauszeichnung konzipiert."""
            },
            {
                "answer": "TEI",
                "correct": True,
                "feedback": """✓ Richtig. Die Text Encoding Initiative (TEI) wurde speziell für Texte entwickelt und ermöglicht detaillierte Textauszeichnung mit umfangreichen Beschreibungsmöglichkeiten. Der spezialisierte teiHeader erlaubt eine präzise Beschreibung von Textdokumenten."""
            },
            {
                "answer": "MARC",
                "correct": False,
                "feedback": """× Falsch. MARC dient in erster Linie der bibliographischen Beschreibung, nicht der Auszeichnung von Textinhalten."""
            },
            {
                "answer": "METS",
                "correct": False,
                "feedback": """× Falsch. METS beschreibt die Struktur digitaler Objekte, ist aber nicht speziell für Textauszeichnung konzipiert."""
            }
        ]
    }
]

display_quiz(metadata_schema_questions, colors=colors.jupyterquiz)
```

### Frage 8(c)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_schema_questions = [
    {
        "question": "Welches Metadatenschema wird als \"umfassend für bibliographische Informationen\" beschrieben?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core",
                "correct": False,
                "feedback": """× Falsch. Dublin Core bietet zwar bibliographische Grundelemente, ist aber nicht so umfassend wie spezialisierte bibliographische Formate."""
            },
            {
                "answer": "TEI",
                "correct": False,
                "feedback": """× Falsch. TEI kann bibliographische Informationen enthalten, ist aber primär ein Textauszeichnungsformat."""
            },
            {
                "answer": "MARC",
                "correct": True,
                "feedback": """✓ Richtig. MARC (Machine-Readable Cataloging) wurde speziell für umfassende bibliographische Informationen entwickelt und ist ein Standard in Bibliotheken weltweit. Es enthält detaillierte Felder für alle Aspekte bibliographischer Beschreibung."""
            },
            {
                "answer": "EAD",
                "correct": False,
                "feedback": """× Falsch. Encoded Archival Description ist für archivische Findmittel konzipiert, nicht primär für bibliographische Daten."""
            }
        ]
    }
]

display_quiz(metadata_schema_questions, colors=colors.jupyterquiz)
```

### Frage 8(d)
```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

metadata_schema_questions = [
    {
        "question": "Welches Metadatenschema wird als \"Standard für Digitalisate und deren Übertragung\" bezeichnet?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core",
                "correct": False,
                "feedback": """× Falsch. Dublin Core bietet zwar einen einfachen Standard für digitale Ressourcen, ist aber nicht speziell auf Digitalisate und deren Übertragung ausgerichtet."""
            },
            {
                "answer": "TEI",
                "correct": False,
                "feedback": """× Falsch. TEI konzentriert sich auf die Auszeichnung und Beschreibung von Texten, nicht auf die Übertragung von Digitalisaten."""
            },
            {
                "answer": "MARC",
                "correct": False,
                "feedback": """× Falsch. MARC dient hauptsächlich der bibliographischen Beschreibung, nicht dem Management von Digitalisaten."""
            },
            {
                "answer": "METS",
                "correct": True,
                "feedback": """✓ Richtig. Das Metadata Encoding and Transmission Standard (METS) wurde speziell für die Beschreibung und Übertragung digitaler Objekte in Repositorien entwickelt. Es dient als Container für verschiedene Metadatentypen und unterstützt die strukturierte Beschreibung von Digitalisaten."""
            }
        ]
    }
]

display_quiz(metadata_schema_questions, colors=colors.jupyterquiz)
```

## Frage 9

Bringen Sie die Schritte des Korpusaufbaus in die richtige Reihenfolge, indem Sie die Schritte per Drag & Drop den Positionen zuordnen.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from quadriga.assessment import DragDropQuiz

quiz = DragDropQuiz()
quiz.create_matching_quiz(
    title="In welcher Reihenfolge werden die folgenden Schritte beim Korpusaufbau durchgeführt?",
    descriptions=["Schritt 1", "Schritt 2", "Schritt 3", "Schritt 4", "Schritt 5"],
    options=[
        "Test der Sammlungsmethodik",
        "Entwicklung des Korpuskonzepts",
        "Durchführung der Datensammlung",
        "Dokumentation der Auswahlkriterien",
        "Festlegung der Metadatenstruktur",
    ],
    correct_mapping={
        "Schritt 1": "Entwicklung des Korpuskonzepts",
        "Schritt 2": "Dokumentation der Auswahlkriterien",
        "Schritt 3": "Festlegung der Metadatenstruktur",
        "Schritt 4": "Test der Sammlungsmethodik",
        "Schritt 5": "Durchführung der Datensammlung",
    },
)
```

````{admonition} Lösung mit Erläuterung
:class: solution, dropdown
**Korrekte Reihenfolge:** 1. Entwicklung des Korpuskonzepts → 2. Dokumentation der Auswahlkriterien → 3. Festlegung der Metadatenstruktur → 4. Test der Sammlungsmethodik → 5. Durchführung der Datensammlung

**Begründung:** Die Erstellung des Konzepts muss an erster Stelle erfolgen. Bevor ein erster Test zur Machbarkeit der Sammlungsmethodik durchgeführt werden kann, müssen die Kriterien zur Auswahl der Daten festgelegt werden sowie eine Struktur, in der die Metadaten gespeichert werden. Wenn erste Tests der Sammlungsmethodik erfolgreich waren, kann die Sammlung der kompletten Daten ausgeführt werden.
````

## Frage 10

Analysieren Sie den folgenden Ausschnitt aus einem Korpusaufbau-Konzept:

"Für die Untersuchung literarischer Reaktionen auf die Luftverschmutzung im 19. Jahrhundert wird das *Corpus of German-Language Fiction* (über 2.700 Texte, frei verfügbar als Plain Text) verwendet. Das Korpus wird auf das 19. Jahrhundert eingegrenzt; Jahrzehnte mit weniger als 50 verfügbaren Texten werden ausgeschlossen. Anschließend werden zwei unabhängige, nach Jahrzehnten geschichtete Zufallsstichproben mit je 50 Texten pro Jahrzehnt (1810er bis 1890er, also je 450 Texte) gezogen – Korpus I und Korpus II."

Bewerten Sie die folgenden Aspekte:

1.	Quellenauswahl
2.	Auswahlstrategie (nach Schöch)
3.	Praktische Einschränkungen
4.	Lösungsansatz

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('korpus-2')
```


````{admonition} Lösungen
:class: solution, dropdown

**Musterlösung**:

1. Quellenauswahl:
    - Einziges der geprüften Korpora (ELTeC-DEU, d-Prose, Corpus of German-Language Fiction), das das gesamte 19. Jahrhundert abdeckt
    - Großer Umfang (über 2.700 Texte) und freie Verfügbarkeit
    - Plain Text ist direkt maschinenlesbar, kein OCR nötig
    - Einschränkung: Die Metadaten mussten erst per RegEx aus den Dateinamen extrahiert und bereinigt werden

2. Auswahlstrategie (nach Schöch):
    - Das Ausgangskorpus ist opportunistisch zusammengestellt und nicht repräsentativ – spätere Jahrzehnte enthalten deutlich mehr Texte als frühere
    - Ein vollständiges Korpus ("alle Romane des 19. Jahrhunderts") ist nicht realisierbar
    - Die geschichtete Zufallsstichprobe kombiniert zwei Strategien: Schichtung nach Jahrzehnten sorgt für zeitliche Balance, die Zufallsauswahl innerhalb jeder Schicht vermeidet subjektive Verzerrungen

3. Praktische Einschränkungen:
    - Sehr ungleichmäßige Verteilung der Texte über die Jahrzehnte
    - Das Jahrzehnt 1800–1809 liegt unter dem Schwellenwert von 50 Texten und muss ausgeschlossen werden
    - Balance nur entlang der Zeitachse: Andere Merkmale (z.B. Geschlecht der Autor:innen, Untergattung) bleiben so verteilt wie im Quellkorpus

4. Lösungsansatz:
    - 50 Texte pro Jahrzehnt als pragmatischer Kompromiss zwischen Stichprobengröße und Abdeckung möglichst vieler Jahrzehnte
    - Zwei unabhängige Stichproben (Korpus I und Korpus II) erlauben es, die Robustheit der Ergebnisse gegenüber der konkreten Zufallsauswahl zu prüfen
    - Feste Random States machen die Ziehung reproduzierbar
````

## Frage 11
(Wählen Sie alle zutreffenden Antworten aus)

Im Abschnitt [Metadaten](corpus-collection_metadata) wurden zwei Dublin-Core-Beispiele vorgestellt: die Beschreibung des Korpus "German Novel Corpus (ELTeC-deu)" und die Beschreibung des Einzeldokuments "Die Geier-Wally" von Wilhelmine von Hillern.

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

"""
Lernziel:
    Sie können die grundlegenden Metadatenschemata (Dublin Core, TEI, MODS, METS) und deren charakteristische Elemente für Korpora und Einzeldokumente beschreiben.
Bloom-Stufe: Analysieren
Format: Multiple Choice
Geschätzte Zeit: 5 Minuten
Schwerpunkte:
    - Anwendung von Dublin Core auf konkrete Beispiele
    - Unterscheidung Korpus- und Dokumentebene
"""

question11 = [
    {
        "question": "Welche der folgenden Aussagen zu diesen beiden Metadaten-Beispielen sind korrekt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": """"DC.coverage: 1840-1920, Deutschland" beschreibt die zeitliche und räumliche Abdeckung des gesamten ELTeC-deu-Korpus""",
                "correct": True,
                "feedback": """✓ Richtig! "DC.coverage" gibt hier auf Korpus-Level an, welchen Zeitraum (1840-1920) und welchen Raum (Deutschland) die Sammlung abdeckt. Solche Angaben helfen bei der Einschätzung, ob ein Korpus für eine Forschungsfrage geeignet ist – etwa im Hinblick auf die zeitliche Abdeckung des 19. Jahrhunderts."""
            },
            {
                "answer": """"DC.identifier: Q1212872" ist ein eindeutiger Identifikator für das Einzeldokument "Die Geier-Wally\"""",
                "correct": True,
                "feedback": """✓ Richtig! Der Identifikator ermöglicht es, das Dokument eindeutig zu referenzieren und mit anderen Datenbeständen zu verknüpfen. Eindeutige Identifikatoren sind typische Metadaten auf Dokumentebene."""
            },
            {
                "answer": """"DC.date" bezeichnet in beiden Beispielen das Publikationsjahr eines literarischen Werks""",
                "correct": False,
                "feedback": """× Nicht korrekt. Nur auf Dokumentebene bezeichnet "DC.date: 1873" das Publikationsjahr des Romans "Die Geier-Wally". Auf Korpus-Level bezieht sich "DC.date: 2021-04-11" dagegen auf die Veröffentlichung des Korpus selbst – die Bedeutung eines Elements hängt also davon ab, welches Objekt beschrieben wird."""
            },
            {
                "answer": """"DC.creator" nennt in beiden Beispielen die Autor:innen literarischer Werke""",
                "correct": False,
                "feedback": """× Nicht korrekt. Auf Dokumentebene nennt "DC.creator" mit Wilhelmine von Hillern tatsächlich die Autorin des Romans. Auf Korpus-Level stehen dort aber die Ersteller:innen des Korpus (Leonard Konle, Fotis Jannidis, Carolin Odebrecht, Lou Burnard) – nicht die Autor:innen der enthaltenen Werke."""
            }
        ]
    }
]
display_quiz(question11, colors=colors.jupyterquiz, max_width=1000)
```
