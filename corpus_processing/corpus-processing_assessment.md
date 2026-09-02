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

**Geschätzte Zeit**: 60min

Viel Erfolg!
````

## Frage 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können die Grundkonzepte des Natural Language Processing erklären und die Funktionen von Tokenisierung und Lemmatisierung für die Textanalyse beschreiben.
Bloom-Stufe: Verstehen
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_1 = [{
    "question": """Welche der folgenden Aussagen beschreibt korrekt, was NLP im Kontext der Textanalyse leistet?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "NLP dient ausschließlich der automatischen Übersetzung zwischen Sprachen",
            "correct": False,
            "feedback": """× Nicht korrekt. Obwohl maschinelle Übersetzung ein Anwendungsgebiet von NLP ist, umfasst NLP viel mehr, insbesondere die Anreicherung von Texten mit linguistischen Informationen für verschiedene Analysezwecke. NLP beinhaltet Methoden wie Tokenisierung, Lemmatisierung und viele weitere Techniken zur Textverarbeitung."""
        },
        {
            "answer": "NLP ermöglicht die Anreicherung von Texten mit linguistischen Informationen, die für Computer sonst nicht erkennbar wären",
            "correct": True,
            "feedback": """✓ Richtig! NLP (Natural Language Processing) ermöglicht es, Texte mit linguistischen Informationen anzureichern und damit für Computer "verständlich" zu machen. Computer sehen Text zunächst nur als Zeichenkette, während NLP-Methoden semantische Strukturen hinzufügen und Analysen auf Wortebene ermöglichen."""
        },
        {
            "answer": "NLP ist ein Verfahren zur manuellen Annotation von Texten durch Sprachwissenschaftler:innen",
            "correct": False,
            "feedback": """× Nicht korrekt. NLP bezieht sich auf automatisierte Verfahren zur Textverarbeitung durch Computer, nicht auf manuelle Annotation. Während manuelle Annotation durchaus für Training und Evaluation von NLP-Systemen wichtig sein kann, ist NLP selbst ein computergestützter Prozess."""
        },
        {
            "answer": "NLP kann nur auf modernen Texten angewendet werden, nicht auf historischen Dokumenten",
            "correct": False,
            "feedback": """× Nicht korrekt. NLP kann grundsätzlich auf Texte jeder Epoche angewendet werden, auch wenn historische Texte aufgrund von Sprachveränderungen, anderen Schriften oder OCR-Qualität besondere Herausforderungen darstellen können. Gerade in den Digital Humanities wird NLP häufig für historische Textanalyse eingesetzt."""
        }
    ]
}]

display_quiz(multiple_choice_1, colors=colors.jupyterquiz)
```

## Frage 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_2 = [{
    "question": """Welche Funktion erfüllt die Tokenisierung im NLP-Prozess?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie übersetzt den Text in eine andere Sprache",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Übersetzung ist eine komplexe NLP-Aufgabe, die weit über die Tokenisierung hinausgeht. Tokenisierung ist ein grundlegender Vorverarbeitungsschritt, der Texte in kleinere Einheiten zerlegt, aber keine Übersetzung vornimmt."""
        },
        {
            "answer": "Sie identifiziert die Stimmung (positiv/negativ) eines Textes",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Tokenisierung, sondern die Sentimentanalyse, die eine fortgeschrittene NLP-Aufgabe ist. Tokenisierung ist ein Vorverarbeitungsschritt, der für die Sentimentanalyse notwendig sein kann, aber selbst keine emotionale Bewertung vornimmt."""
        },
        {
            "answer": "Sie zerlegt einen Text in einzelne, sinnvolle Einheiten wie Wörter und Satzzeichen",
            "correct": True,
            "feedback": """✓ Richtig! Die Tokenisierung ist der Prozess der Zerlegung eines Textes in einzelne, bedeutungstragende Einheiten (Token). Diese können Wörter, Zahlen oder Satzzeichen sein. Sie ist der erste grundlegende Schritt in der NLP-Pipeline, auf dem weitere Verarbeitungsschritte aufbauen."""
        },
        {
            "answer": "Sie wandelt alle Wörter in ihre Grundform um",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Tokenisierung, sondern die Lemmatisierung. Die Tokenisierung zerlegt Text in einzelne Einheiten, während die Lemmatisierung in einem späteren Schritt diese Einheiten auf ihre Grundform zurückführt."""
        }
    ]
}]

display_quiz(multiple_choice_2, colors=colors.jupyterquiz)
```

## Frage 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_3 = [{
    "question": """Was ist das Hauptziel der Lemmatisierung in der NLP-Pipeline?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Bestimmung der grammatikalischen Funktion eines Wortes im Satz",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Lemmatisierung, sondern das Part-of-Speech Tagging (POS-Tagging). Die Lemmatisierung befasst sich mit der Reduktion von Wortformen auf ihre Grundform, nicht mit der grammatikalischen Funktionsanalyse."""
        },
        {
            "answer": "Die Zurückführung verschiedener Wortformen auf ihre gemeinsame Grundform",
            "correct": True,
            "feedback": """✓ Richtig! Die Lemmatisierung führt verschiedene Formen eines Wortes auf ihre gemeinsame Grundform (Lemma) zurück. Beispielsweise werden "gehe", "gehst", "geht", "ging" auf "gehen" zurückgeführt. Dies vereinfacht die Textanalyse, da verschiedene Formen desselben Wortes als eine Einheit betrachtet werden können."""
        },
        {
            "answer": "Die Erkennung von Eigennamen und geographischen Bezeichnungen",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die Lemmatisierung, sondern die Named Entity Recognition (NER). Die Lemmatisierung hat nicht das Ziel, bestimmte semantische Kategorien von Wörtern zu identifizieren, sondern Wortformen zu vereinheitlichen."""
        },
        {
            "answer": "Die Zerlegung von Komposita in ihre Bestandteile",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt nicht die primäre Funktion der Lemmatisierung. Die Zerlegung von Komposita (zusammengesetzten Wörtern) ist eine separate NLP-Aufgabe, die als Compound Splitting bezeichnet wird. Die Lemmatisierung befasst sich mit der Reduktion von flektierten Formen auf ihre Grundform."""
        }
    ]
}]

display_quiz(multiple_choice_3, colors=colors.jupyterquiz)
```

## Frage 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_4 = [{
    "question": """Warum ist die Kombination von Tokenisierung und Lemmatisierung für die quantitative Textanalyse besonders wertvoll?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie ermöglicht die automatische Übersetzung des Textes",
            "correct": False,
            "feedback": """× Nicht korrekt. Obwohl Tokenisierung und Lemmatisierung grundlegende Schritte in der Übersetzungspipeline sein können, reichen sie allein nicht aus, um eine automatische Übersetzung zu ermöglichen. Dafür sind komplexere Modelle notwendig."""
        },
        {
            "answer": "Sie verbessert die Lesbarkeit des Textes für Menschen",
            "correct": False,
            "feedback": """× Nicht korrekt. Tokenisierung und Lemmatisierung sind in erster Linie für die maschinelle Verarbeitung gedacht, nicht für die menschliche Lesbarkeit. Im Gegenteil, ein lemmatisierter Text kann für Menschen sogar schwerer zu lesen sein, da er nicht mehr den gewohnten grammatikalischen Formen entspricht."""
        },
        {
            "answer": "Sie ermöglicht präzisere Häufigkeitsanalysen durch Normalisierung verschiedener Wortformen",
            "correct": True,
            "feedback": """✓ Richtig! Die Kombination von Tokenisierung und Lemmatisierung ist für quantitative Textanalysen besonders wertvoll, weil sie die Varianz der Wortformen reduziert. Dadurch können Häufigkeitsanalysen präziser durchgeführt werden, da verschiedene Formen desselben Wortes nicht mehr als verschiedene Wörter gezählt werden."""
        },
        {
            "answer": "Sie korrigiert Rechtschreibfehler im Originaltext",
            "correct": False,
            "feedback": """× Nicht korrekt. Weder Tokenisierung noch Lemmatisierung sind primär darauf ausgerichtet, Rechtschreibfehler zu korrigieren. Rechtschreibkorrektur ist eine separate NLP-Aufgabe, die vor der Tokenisierung und Lemmatisierung durchgeführt werden sollte."""
        }
    ]
}]

display_quiz(multiple_choice_4, colors=colors.jupyterquiz)
```

## Frage 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_5 = [{
    "question": """Welcher Unterschied besteht zwischen dem ursprünglichen Text und dem mit NLP-Methoden verarbeiteten Text?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Der verarbeitete Text enthält keine Satzzeichen mehr",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht allgemein zutreffend. Ob Satzzeichen im verarbeiteten Text erhalten bleiben, hängt von den spezifischen NLP-Methoden und deren Konfiguration ab. In vielen NLP-Pipelines werden Satzzeichen als eigene Token behandelt und bleiben somit erhalten."""
        },
        {
            "answer": "Der verarbeitete Text ist in eine andere Sprache übersetzt",
            "correct": False,
            "feedback": """× Nicht korrekt. NLP-Methoden umfassen viele verschiedene Verarbeitungsschritte, von denen Übersetzung nur einer ist. Die meisten grundlegenden NLP-Verarbeitungsschritte wie Tokenisierung und Lemmatisierung verändern die Sprache des Textes nicht."""
        },
        {
            "answer": "Der verarbeitete Text ist mit zusätzlichen linguistischen Informationen angereichert",
            "correct": True,
            "feedback": """✓ Richtig! Der wesentliche Unterschied besteht darin, dass der mit NLP-Methoden verarbeitete Text mit zusätzlichen linguistischen Informationen angereichert ist. Dies können Informationen über Wortarten, Grundformen, syntaktische Beziehungen oder semantische Bedeutungen sein. Der Computer kann dadurch auf verschiedenen linguistischen Ebenen mit dem Text arbeiten."""
        },
        {
            "answer": "Der verarbeitete Text ist kürzer als der Originaltext",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht allgemein zutreffend. Die Länge des verarbeiteten Textes hängt von den angewendeten NLP-Methoden ab. Bei manchen Methoden (wie z.B. Zusammenfassung) kann der Text kürzer werden, bei anderen (wie z.B. Annotation) kann er durch zusätzliche Informationen sogar länger werden."""
        }
    ]
}]

display_quiz(multiple_choice_5, colors=colors.jupyterquiz)
```

## Frage 6
Analysieren Sie den folgenden Satz mit NLP-Methoden und beschreiben Sie die Ergebnisse:

Originaltext: "Die Forschenden untersuchten verschiedene deutsche Romane."

1.	Führen Sie eine Tokenisierung durch.
2.	Bestimmen Sie die Lemmata der einzelnen Token.
3.	Reflektieren Sie, wie diese Verarbeitung eine quantitative Analyse unterstützen würde.


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('process-1')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiellösung zur Selbstbewertung:**
1.	Tokenisierung: ["Die", "Forschenden", "untersuchten", "verschiedene", "deutsche", "Romane", "."]
2.	Lemmatisierung: ["der", "Forschende", "untersuchen", "verschieden", "deutsch", "Roman", "."]

**Reflexion:**
- Die Tokenisierung ermöglicht die Analyse auf Wortebene und bereitet den Text für weitere Verarbeitung vor; der Punkt am Satzende wird dabei als eigenes Token abgetrennt
- Die Lemmatisierung würde alle Formen von "untersuchen" zusammenfassen, was bei einer Frequenzanalyse hilfreich ist
- Durch die Lemmatisierung werden verschiedene Flexionsformen (wie "deutsche" zu "deutsch" oder "Romane" zu "Roman") vereinheitlicht ('die' wird standardmäßig zu 'der' lemmatisiert).
- Bei einer größeren Textsammlung würden verschiedene grammatikalische Formen desselben Wortes nicht als unterschiedliche Begriffe gezählt
- Diese Normalisierung verbessert die Qualität von Häufigkeitsanalysen, Keyword-Extraktion und thematischen Analysen
- Die Informationen über die ursprüngliche Form bleiben erhalten und können für detailliertere linguistische Analysen genutzt werden

**Bewertungskriterien für die Selbsteinschätzung:**
- Korrekte Tokenisierung mit Berücksichtigung von Satzzeichen als eigene Token
- Korrekte Bestimmung der Grundformen bei der Lemmatisierung
- Verständnis des Nutzens für quantitative Textanalyse, insbesondere für Häufigkeitsanalysen
- Reflexion über die Vor- und Nachteile der Methoden für die spezifische Forschungsfrage

````



## Frage 7
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können die notwendigen Schritte zur automatischen Annotation eines Texts aufzählen und Vorteile der Tokenisierung gegenüber einfacheren Methoden der Worttrennung nennen.
Bloom-Stufe: Verstehen
Format: Multiple Choice
"""

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_1 = [{
    "question": """Welche Schritte gehören zur automatischen Annotation eines Textes mit spaCy?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Einlesen des Textes",
            "correct": True,
            "feedback": """✓ Richtig! Der erste Schritt im Notebook ist das Einlesen des Textes mit text_path.read_text(encoding="utf-8"), nachdem der Pfad zur Datei definiert wurde (text_path = Path("../data/txt/Adalbert_Stifter_-_Feldblumen_(1841).txt"))."""
        },
        {
            "answer": "Laden des sprachspezifischen Modells",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook wird das deutsche Sprachmodell mit nlp = spacy.load('de_core_news_sm') geladen, welches für die Verarbeitung deutscher Texte optimiert ist."""
        },
        {
            "answer": "Auswahl der relevanten Analysekomponenten",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook werden nicht benötigte Komponenten ausgewählt und ausgeschlossen: disable_components = ['ner', 'attribute_ruler', 'sentencizer'], um die Verarbeitungsgeschwindigkeit zu erhöhen. Die Komponenten für das POS-Tagging und das Dependency Parsing bleiben dagegen aktiv, da die Analyse sie benötigt. Dieser Schritt kann bei geringer Textmenge übersprungen werden."""
        },
        {
            "answer": "Manuelle Korrektur der Tokenisierungsfehler",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Annotation mit spaCy erfolgt vollautomatisch. Im Notebook gibt es keinen Schritt zur manuellen Korrektur von Tokenisierungsfehlern."""
        },
        {
            "answer": "Speichern der Ergebnisse in einem strukturierten Format",
            "correct": True,
            "feedback": """✓ Richtig! Im letzten Schritt werden die Annotationen in zwei Formaten gespeichert: im spaCy-eigenen Format mit doc.to_disk(output_path_spacy) (Dateiendung .spacy) und als Tabelle mit anno_df.to_csv(output_path_table, index=False) (CSV-Format). Zusätzlich wird eine Dokumentationsdatei mit spaCy-Version, Modellname, Modellversion und Datum geschrieben, um die Reproduzierbarkeit der Annotation sicherzustellen."""
        }
    ]
}]

display_quiz(multiple_choice_1, colors=colors.jupyterquiz)
```

## Frage 8
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_2 = [{
    "question": """Welche Vorteile bietet die Tokenisierung mit spaCy gegenüber einer einfachen Worttrennung mittels split()?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Satzzeichen werden als eigene Token erkannt",
            "correct": True,
            "feedback": """✓ Richtig! Das Notebook zeigt im Beispiel words[7:79], dass bei der einfachen Teilung mit split() Satzzeichen an Wörtern hängen bleiben (z.B. "Last,", "hat."), während spaCy sie als separate Token erkennt."""
        },
        {
            "answer": "Die Gesamtanzahl der Token ist akkurater",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook wird explizit darauf hingewiesen: "Wie zu sehen ist, hat diese Art der 'falschen' Tokenisierung den Nachteil, dass Satzzeichen nicht von Wörtern abgetrennt werden. Die Wortanzahl ist dementsprechend auch nicht akkurat." Der Vergleich für den Roman "Feldblumen" zeigt rund 38.000 Wörter mit split() gegenüber rund 47.000 Token mit spaCy."""
        },
        {
            "answer": "Die Tokenisierung mit spaCy ist immer schneller",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Im Gegenteil: Die Annotation mit spaCy dauert deutlich länger als ein einfaches split(). Das Notebook misst deshalb die Annotationsdauer und schlägt für die Annotation der gesamten Korpora Optimierungen vor, z.B. das Ausschließen nicht benötigter Komponenten, die .pipe()-Methode und die parallele Prozessierung mehrerer Texte."""
        },
        {
            "answer": "Sie ermöglicht die Lemmatisierung der Tokens",
            "correct": False,
            "feedback": """× Nicht korrekt: Auch wenn im Notebook die Tokenisierung und die Lemmatisierung im selben Schritt erfolgen, ist die Lemmatisierung kein Teil der Tokenisierung, sondern erfolgt aufbauend auf dieser.""" 
        },
        {
            "answer": "Sie korrigiert automatisch OCR-Fehler im Text",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. spaCy führt keine automatische Korrektur von OCR-Fehlern durch. Die Qualität der Annotation hängt von der Qualität des Eingabetextes ab."""
        }
    ]
}]

display_quiz(multiple_choice_2, colors=colors.jupyterquiz)
```

## Frage 9

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_3 = [{
    "question": """Warum werden im Beispiel bestimmte Analysekomponenten von spaCy ausgeschlossen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Um die Genauigkeit der Tokenisierung zu erhöhen",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Das Ausschließen von Komponenten dient nicht der Verbesserung der Genauigkeit."""
        },
        {
            "answer": "Um die Verarbeitungsgeschwindigkeit zu erhöhen",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook steht explizit: "Es werden einige Analysekomponenten wie z. B. das Aufteilen des Texts in Sätze (sentencizer) oder die Named Entity Recognition (ner) ausgeschlossen, da diese für die Tokenisierung und die Lemmatisierung sowie für das POS-Tagging und Dependency Parsing nicht benötigt werden. Der Ausschluss der Komponenten erhöht die Annotationsgeschwindigkeit." Wichtig ist dabei: Es werden nur Komponenten ausgeschlossen, deren Annotationen für die Analyse nicht gebraucht werden – die Komponenten für das POS-Tagging und das Dependency Parsing bleiben aktiv."""
        },
        {
            "answer": "Um mehr Speicherplatz für die Ergebnisse zu haben",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Der Speicherplatz für die Ergebnisse wird nicht als Grund für den Ausschluss von Komponenten genannt."""
        },
        {
            "answer": "Um Kompatibilitätsprobleme mit dem CSV-Format zu vermeiden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage wird nicht durch das Notebook unterstützt. Es gibt keinen Hinweis darauf, dass der Ausschluss von Komponenten mit dem CSV-Format zusammenhängt."""
        }
    ]
}]

display_quiz(multiple_choice_3, colors=colors.jupyterquiz)
```

## Frage 10

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_4 = [{
    "question": """Welches textbasierte, interoperable Dateiformat wird im Beispiel für die Speicherung der Annotationstabelle verwendet und warum?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "TXT, weil es am wenigsten Speicherplatz benötigt",
            "correct": False,
            "feedback": """× Nicht korrekt. Laut Notebook wird die Annotationstabelle nicht als TXT-Datei gespeichert."""
        },
        {
            "answer": "CSV, weil es gut für die Speicherung tabellarischer Daten geeignet ist",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook steht: "Für die Speicherung von relationalen Daten (wie ein Wort und die unterschiedlichen Annotationen des Worts) eignet sich das Tabellenformat gut." Die Annotationstabelle (anno_df) wird deshalb als .csv-Datei gespeichert. Beachten Sie: Zusätzlich speichert das Notebook die Annotationen auch im spaCy-eigenen Format (Dateiendung .spacy, mit doc.to_disk()), damit die spaCy-spezifischen Funktionen – etwa die Navigation der Dependenzstruktur – weiter genutzt werden können. Da dieses Format von spaCy abhängig und damit weniger interoperabel ist, wird die Annotation zusätzlich im plattformunabhängigen, textbasierten CSV-Format abgelegt."""
        },
        {
            "answer": "JSON, weil es die hierarchische Struktur der Annotation am besten abbildet",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt, da die Annotationen nicht hierarchisch strukturiert sind. Im Notebook wird JSON nicht als Speicherformat erwähnt, ist aber auch ein mögliches Format, um annotierte Daten zu speichern. """
        },
        {
            "answer": "XML, weil es von den meisten Textanalysewerkzeugen unterstützt wird",
            "correct": False,
            "feedback": """× Nicht korrekt. XML ist in den Digital Humanities zwar ein Standardformat, um Annotationen zu speichern, allerdings sind nicht die meisten Analysewerkzeuge auf das Format ausgelegt. XML eignet sich für die Speicherung von komplexeren Annotationen oder Textauszeichnungen besser."""
        }
    ]
}]

display_quiz(multiple_choice_4, colors=colors.jupyterquiz)
```

## Frage 11

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_5 = [{
    "question": """Was zeigt der Vergleich der Textlänge vor und nach der Tokenisierung mit spaCy im Beispiel?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Der tokenisierte Text ist kürzer, weil Stoppwörter entfernt wurden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist nicht korrekt, da es im Notebook keinen Hinweis darauf gibt, dass Stoppwörter entfernt wurden. Im Gegenteil, die Tokenzahl erhöht sich."""
        },
        {
            "answer": "Der tokenisierte Text enthält mehr Elemente, weil Satzzeichen als eigene Token erkannt werden",
            "correct": True,
            "feedback": """✓ Richtig! Das Notebook zeigt: "Durch die Tokenisierung wurden z. B. Satzzeichen von Wörtern abgetrennt. An der Textlänge lässt sich dies schon erkennen." Für den Roman "Feldblumen" steigt die Anzahl von rund 38.000 (Aufteilung nach Leerzeichen mit split()) auf rund 47.000 Token (Tokenisierung mit spaCy)."""
        },
        {
            "answer": "Der tokenisierte Text ist unverändert in seiner Länge, nur die Qualität der Tokens ist verbessert",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage widerspricht dem im Notebook gezeigten Unterschied in der Tokenanzahl (rund 38.000 vs. rund 47.000)."""
        },
        {
            "answer": "Der tokenisierte Text ist kürzer, weil zusammengehörige Mehrwortausdrücke als ein Token erkannt werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage widerspricht dem im Notebook gezeigten Anstieg der Tokenanzahl."""
        }
    ]
}]

display_quiz(multiple_choice_5, colors=colors.jupyterquiz)
```

## Frage 12
Bringen Sie die Verarbeitungsschritte in die richtige Reihenfolge, um einen Text mit spaCy zu annotieren. Ziehen Sie dazu die Schritte per Drag & Drop an die passende Position.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from quadriga.assessment import DragDropQuiz

schritte = [
    "Einlesen des Textes",
    "Laden des Sprachmodells",
    "Auswahl der Analysekomponenten",
    "Durchführung der Annotation mit nlp(text)",
    "Speichern der Annotationen (als CSV- und .spacy-Datei)",
]

beschreibungen = [f"Schritt {i}" for i in range(1, len(schritte) + 1)]

# scrambled order of the draggable options
optionen = [schritte[3], schritte[0], schritte[4], schritte[1], schritte[2]]

quiz = DragDropQuiz()
quiz.create_matching_quiz(
    title="Welche Reihenfolge der Verarbeitungsschritte ist korrekt für die Textannotation mit spaCy?",
    descriptions=beschreibungen,
    options=optionen,
    correct_mapping={beschreibung: schritt for beschreibung, schritt in zip(beschreibungen, schritte)},
)
```

````{admonition} Lösung
:class: solution, dropdown
Die Reihenfolge im Notebook ist: 1. Einlesen des Textes, 2. Laden des Sprachmodells, 3. Auswahl der Analysekomponenten, 4. Durchführung der Annotation mit nlp(text), 5. Speichern der Annotationen – sowohl im spaCy-eigenen Format (.spacy) als auch als Tabelle im CSV-Format.
````

## Frage 13
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können begründen, welche Annotationsebenen (Lemmatisierung, POS-Tagging, Dependency Parsing) für die Extraktion von Adjektiv-Nomen-Paaren benötigt werden.
Bloom-Stufe: Analysieren
Format: Multiple Choice
"""

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_7 = [{
    "question": """Im Notebook werden die Adjektive extrahiert, die sich auf das Nomen "Luft" beziehen (z.B. "reine Luft"). Welche Annotationsebenen werden dafür benötigt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Part-of-Speech-Tagging (Wortarten)",
            "correct": True,
            "feedback": """✓ Richtig! Im Code wird mit token.pos_ == "NOUN" geprüft, ob "Luft" als Nomen verwendet wird, und mit child.pos_ == "ADJ" werden die Adjektive identifiziert. Ohne POS-Tags könnte der Computer Wortarten nicht unterscheiden – genau deshalb dürfen die Komponenten, die die POS-Tags erzeugen, auch nicht ausgeschlossen werden."""
        },
        {
            "answer": "Dependency Parsing (syntaktische Beziehungen)",
            "correct": True,
            "feedback": """✓ Richtig! Über die Dependenzstruktur des spaCy-Doc (token.children) werden attributive Adjektive gefunden, die direkt vom Nomen "Luft" abhängen. Zusätzlich werden über die Dependenz-Tags "sb" (Subjekt) und "pd" (Prädikat) prädikative Adjektive erfasst, etwa in Sätzen wie "Die Luft ist rein"."""
        },
        {
            "answer": "Lemmatisierung",
            "correct": True,
            "feedback": """✓ Richtig! Die Bedingung token.lemma_ == "Luft" nutzt das Lemma, damit auch flektierte Formen des Nomens gefunden werden. Auch die gefundenen Adjektive werden als Lemmata (child.lemma_) gesammelt, sodass z.B. "reine" und "reiner" gemeinsam als "rein" gezählt werden."""
        },
        {
            "answer": "Named Entity Recognition (NER)",
            "correct": False,
            "feedback": """× Nicht korrekt. NER erkennt Eigennamen wie Personen- oder Ortsnamen. Für die Extraktion von Adjektiv-Nomen-Paaren wird diese Annotationsebene nicht benötigt – im Notebook ist "ner" deshalb sogar in der Liste disable_components enthalten."""
        },
        {
            "answer": "Sentimentanalyse",
            "correct": False,
            "feedback": """× Nicht korrekt. Ob Adjektive wie "rein" und "weich" positiv oder Adjektive wie "finster" negativ konnotiert sind, wird in der Fallstudie interpretativ eingeordnet und nicht durch eine automatische Sentimentanalyse bestimmt. Für die Extraktion der Adjektive selbst wird keine Sentimentanalyse benötigt."""
        }
    ]
}]

display_quiz(multiple_choice_7, colors=colors.jupyterquiz)
```

## Frage 14

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können erklären, warum die Extraktion von Adjektiv-Nomen-Paaren auf dem Dependency Parsing basiert und nicht auf dem Wortabstand.
Bloom-Stufe: Verstehen
Format: Multiple Choice
"""

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_8 = [{
    "question": """Warum werden die Adjektiv-Nomen-Paare über das Dependency Parsing extrahiert und nicht einfach über den geringsten Abstand zwischen Adjektiv und Nomen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Weil sich ein Adjektiv auch auf ein weiter entferntes Nomen beziehen kann – der geringste Abstand führt daher zu Fehlzuordnungen",
            "correct": True,
            "feedback": """✓ Richtig! Das Kapitel zeigt dies am Beispielsatz "Ich roch eine üble, von den Schloten der neuen Fabriken schwer geschwängerte Luft.": Das Nomen mit dem geringsten Abstand zu "üble" ist "Schloten", tatsächlich bezieht sich das Adjektiv aber auf "Luft". Die Dependenzannotation beschreibt die gerichteten grammatikalischen Beziehungen zwischen den Wörtern und ordnet das Adjektiv deshalb dem richtigen Bezugswort zu. Zusätzlich lassen sich über die Dependenzstruktur auch prädikative Konstruktionen wie "Die Luft ist rein" erfassen, bei denen das Adjektiv nicht direkt neben dem Nomen steht."""
        },
        {
            "answer": "Weil spaCy den Abstand zwischen Wörtern nicht berechnen kann",
            "correct": False,
            "feedback": """× Nicht korrekt. Der Abstand zwischen Wörtern ließe sich über die Token-Indizes (token.i) leicht berechnen. Das Problem ist nicht technischer, sondern linguistischer Natur: Das nächststehende Nomen ist nicht immer das Bezugswort des Adjektivs."""
        },
        {
            "answer": "Weil das Dependency Parsing schneller ist als ein Abstandsvergleich",
            "correct": False,
            "feedback": """× Nicht korrekt. Das Dependency Parsing ist rechenaufwendiger als ein einfacher Abstandsvergleich. Es wird nicht wegen der Geschwindigkeit eingesetzt, sondern weil es die grammatikalischen Beziehungen zwischen den Wörtern abbildet und damit korrektere Zuordnungen ermöglicht."""
        },
        {
            "answer": "Weil Adjektive im Deutschen immer direkt nach dem Nomen stehen",
            "correct": False,
            "feedback": """× Nicht korrekt. Attributive Adjektive stehen im Deutschen in der Regel vor dem Nomen ("reine Luft"), prädikative Adjektive können durch mehrere Wörter vom Nomen getrennt sein ("Die Luft ist rein"). Gerade weil die Position variiert, wird die Dependenzstruktur für die Zuordnung genutzt."""
        }
    ]
}]

display_quiz(multiple_choice_8, colors=colors.jupyterquiz)
```
