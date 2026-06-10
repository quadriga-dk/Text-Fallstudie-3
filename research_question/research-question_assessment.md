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
Diese Übungsaufgaben dienen Ihrer Selbsteinschätzung und helfen Ihnen, das im Kapitel Gelernte zu reflektieren.

Sie können die Fragen in beliebiger Reihenfolge beantworten und auch mehrfach versuchen. 

**So funktioniert es:**
- Wählen Sie bei jeder Frage die Antwort(en), die Sie für richtig halten.
- Lesen Sie das Feedback zu den einzelnen Antwortoptionen sorgfältig durch.
- Die Erklärungen helfen Ihnen, Ihr Verständnis zu vertiefen – auch bei korrekten Antworten.

Es erfolgt keine Bewertung oder Speicherung Ihrer Ergebnisse. Nutzen Sie dieses Assessment, um Wissenslücken zu identifizieren und gegebenenfalls die entsprechenden Abschnitte des Kapitels noch einmal zu bearbeiten. 

**Geschätzte Zeit**: 15min

Viel Erfolg!
````

## Frage 1

Eine Forschungsfrage im Bereich der Digital Humanities lautet: "Wie entwickelte sich die öffentliche Aufmerksamkeit für Umweltthemen in deutschen Tageszeitungen zwischen 1960-1980?"

(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question2 = [
    {
        "question": "Welche der folgenden Operationalisierungen eignen sich, um die öffentliche Aufmerksamkeit für Umweltthemen in deutschen Tageszeitungen zwischen 1960-1980 messbar zu machen? (Mehrere Antworten sind korrekt)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Zählen der Häufigkeit von umweltbezogenen Begriffen (wie 'Umweltschutz', 'Verschmutzung') in den Zeitungstexten",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Operationalisierung ist geeignet, weil:
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Sie ein quantifizierbares Maß für die Intensität der Berichterstattung liefert</li>
<li>Die Häufigkeit von Schlüsselbegriffen messbar ist</li>
<li>Systematische Vergleiche über Zeit möglich sind</li>
<li>Die Analyse auf dem definierten Korpus basiert</li>
</ul>"""
            },
            {
                "answer": "Messen der Länge von Artikeln, die Umweltthemen behandeln",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Methode ist geeignet, weil:
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Sie den Umfang der Berichterstattung quantifiziert</li>
<li>Längere Artikel oft mehr Aufmerksamkeit bedeuten</li>
<li>Die Messung über Zeit vergleichbar ist</li>
<li>Die Analyse innerhalb des Quellenkorpus bleibt</li>
</ul>"""
            },
            {
                "answer": "Erfassen der tatsächlichen Umweltverschmutzungswerte aus diesem Zeitraum",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Dies keine mediale Aufmerksamkeit misst</li>
<li>Es außerhalb des Untersuchungskorpus liegt</li>
<li>Es das tatsächliche Geschehen statt der Berichterstattung erfasst</li>
<li>Es nicht die Forschungsfrage beantwortet</li>
</ul>"""
            },
            {
                "answer": "Analyse von Regierungsdokumenten zur Umweltpolitik",
                "correct": False,
                "feedback": """× Nicht korrekt, weil:
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Dies außerhalb des definierten Quellenkorpus (Tageszeitungen) liegt</li>
<li>Es eine andere Textgattung betrifft</li>
<li>Es nicht die mediale Aufmerksamkeit misst</li>
<li>Es eine andere Forschungsfrage erfordern würde</li>
</ul>"""
            },
            {
                "answer": "Erfassen des prozentualen Anteils der Zeitungsseiten mit Umweltthemen",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Operationalisierung ist geeignet, weil:
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Sie den relativen Stellenwert des Themas misst</li>
<li>Sie verschiedene Zeitpunkte vergleichbar macht</li>
<li>Sie auf dem definierten Korpus basiert</li>
<li>Sie ein quantifizierbares Maß liefert</li>
</ul>"""
            }
        ]
    }
]
display_quiz(question2, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 2
Entwickeln Sie eine Operationalisierung für folgende Forschungsfrage: "Wie veränderte sich die Berichterstattung über wissenschaftliche Themen in der Wochenzeitung 'Die Zeit' zwischen 1950-1970?"

### Frage 2(a)
Formulieren Sie zunächst selbst eine mögliche Operationalisierung

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('1')
```

### Frage 2(b)
Vergleichen Sie Ihre Antwort mit den folgenden Kriterien für eine geeignete Operationalisierung. Bewerten Sie Ihre eigene Antwort anhand dieser Kriterien


```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

questions = [
    {
        "question": "Verwendet Ihre Operationalisierung quantifizierbare Indikatoren?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                    "feedback": """× Nicht korrekt! Die Indikatoren müssen in Zahlen ausdrückbar sein
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Beispiele für quantifizierbare Indikatoren:
<ul>
<li>Worthäufigkeiten (z.B. Anzahl wissenschaftsbezogener Begriffe)</li>
<li>Textlängen (z.B. Wörter pro Artikel)</li>
<li>Prozentuale Anteile (z.B. Anteil am Gesamtumfang)</li>
</ul>
</li>
<li>Gegenbeispiele (nicht quantifizierbar):
<ul>
<li>"Wichtigkeit" ohne weitere Spezifikation</li>
<li>"Qualität der Berichterstattung" ohne Messkriterien</li>
<li>Vage Beschreibungen wie "häufig" oder "selten"</li>
</ul>
</li>
</ul>"""
            }
        ]
    },
    {
        "question": "Basieren die Messungen auf dem definierten Quellenkorpus (Die Zeit)?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": """× Nicht korrekt! Alle Messungen müssen im Korpus der "Zeit" durchführbar sein.
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Zu beachten:
<ul>
<li>Verfügbarkeit aller Ausgaben im Untersuchungszeitraum</li>
<li>Konsistenz des Zeitungsformats</li>
<li>Zugänglichkeit der relevanten Artikel</li>
</ul>
</li>
<li>Nicht geeignet sind Messungen, die:
<ul>
<li>andere Zeitungen einbeziehen</li>
<li>externe Datenquellen erfordern</li>
<li>nicht im Zeitungskorpus enthaltene Informationen benötigen</li>
</ul>
</li>
</ul>"""
            }
        ]
    },
    {
        "question": "Lassen sich die Messungen über den gesamten Zeitraum durchführen?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": """× Nicht korrekt! Die Messungen müssen von 1950-1970 konsistent möglich sein
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Wichtige Aspekte:
<ul>
<li>gleichbleibende Verfügbarkeit der Daten</li>
<li>Vergleichbarkeit der Messungen über Zeit</li>
<li>Berücksichtigung möglicher Formatänderungen</li>
</ul>
</li>
<li>Problematisch wären:
<ul>
<li>Indikatoren, die nur für Teilzeiträume verfügbar sind</li>
<li>Messungen, die durch Änderungen der Zeitung beeinflusst werden</li>
<li>nicht durchgängig dokumentierte Aspekte</li>
</ul>
</li>
</ul>"""
            }
        ]
    },
    {
        "question": "Sind die vorgeschlagenen Messverfahren praktisch umsetzbar?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Ja",
                "correct": True,
                "feedback": "✓ Korrekt!"
            },
            {
                "answer": "Nein",
                "correct": False,
                "feedback": """× Nicht korrekt! Die Methoden müssen mit verfügbaren Ressourcen durchführbar sein
<ul style="text-align: left; display: inline-block; margin: 0.3em auto;">
<li>Praktische Aspekte:
<ul>
<li>verfügbare Zeit und Personal</li>
<li>technische Möglichkeiten (z.B. OCR, Textanalysetools)</li>
<li>Aufwand-Nutzen-Verhältnis</li>
</ul>
</li>
<li>Problematisch wären:
<ul>
<li>zu zeitaufwendige manuelle Analysen</li>
<li>technisch nicht realisierbare Messungen</li>
<li>unverhältnismäßig komplexe Verfahren</li>
</ul>
</li>
</ul>"""
            }
        ]
    }
]
display_quiz(questions, colors=colors.jupyterquiz)
```

#### Anwendung der Kriterien

Bei der Bewertung Ihrer Operationalisierung:

1. Prüfen Sie jeden Indikator einzeln gegen alle Kriterien
2. Identifizieren Sie mögliche Schwachstellen
3. Erwägen Sie Alternativen für problematische Aspekte
4. Dokumentieren Sie Ihre Überlegungen zu jedem Kriterium


````{admonition} Lösungen
:class: solution, dropdown
**Beispielhafte Anwendung**
Ein Indikator wie "Anzahl wissenschaftlicher Artikel pro Ausgabe":
- ✓ Quantifizierbar (zählbare Einheit)
- ✓ Basiert auf Quellenkorpus (nur Zeit-Artikel) 
- ✓ Durchgängig messbar (über gesamten Zeitraum)
- ✓ Praktisch umsetzbar (mit klarer Definition und OCR)

**Hinweis** 
Es gibt nicht die eine "richtige" Operationalisierung. Verschiedene Ansätze können geeignet sein, solange sie den grundlegenden Kriterien entsprechen und praktisch umsetzbar sind.
````
