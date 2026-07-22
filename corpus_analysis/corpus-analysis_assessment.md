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

**Geschätzte Zeit**: 1h 30min

Viel Erfolg!
````

## Frage 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie verfügen über ein Grundverständnis des Konzepts des semantischen Feldes, können den Unterschied zwischen absoluten und relativen Häufigkeiten erklären und die Darstellungsmethoden des Streudiagramms mit Trend-Linie interpretieren.
Bloom-Stufe: Verstehen, Analysieren
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_1 = [{
    "question": """Was versteht man in dieser Fallstudie unter dem semantischen Feld "Luft"?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Eine Karte, auf der die Luftqualität im 19. Jahrhundert geografisch dargestellt wird",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt kein semantisches Feld, sondern eher eine historische Umweltkarte. Ein semantisches Feld ist eine linguistische Kategorie: eine Gruppe von Wörtern, die zum selben Bedeutungsbereich gehören."""
        },
        {
            "answer": "Eine Liste von Wörtern, die zum Bedeutungsbereich \"Luft\" gehören – etwa \"Atmosphäre\", \"Dunst\" oder \"Stadtluft\"",
            "correct": True,
            "feedback": """✓ Richtig! Im Kapitel wird ein semantisches Feld als "Gruppe von Wörtern, die zum selben Bedeutungsbereich gehören" definiert. Für die Analyse wurde eine Liste von 127 Substantiven erstellt, die inhaltlich eng mit "Luft" verwandt sind – darunter "Atmosphäre", "Dunst", "Miasma" oder "Stadtluft". Wichtig ist dabei, dass die Wörter möglichst eindeutig sind, sich also ausschließlich auf Luft beziehen, da sie losgelöst von ihrem Kontext gezählt werden."""
        },
        {
            "answer": "Die Gesamtheit aller literarischen Texte, in denen das Wort \"Luft\" vorkommt",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage beschreibt eine Teilmenge des Korpus, nicht ein semantisches Feld. Ein semantisches Feld besteht aus bedeutungsverwandten Wörtern, nicht aus vollständigen Texten."""
        },
        {
            "answer": "Eine statistische Methode zur Messung der Luftverschmutzung im 19. Jahrhundert",
            "correct": False,
            "feedback": """× Nicht korrekt. Die tatsächliche Luftverschmutzung wird in dieser Fallstudie nicht gemessen – untersucht wird, wie Literatur über Luft *spricht*. Das semantische Feld ist dabei keine statistische Methode, sondern die Wortliste, auf deren Basis die Häufigkeiten berechnet werden."""
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
    "question": """Worin besteht der Unterschied zwischen absoluter und relativer Häufigkeit?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Absolute Häufigkeit bezieht sich auf das Wort \"Luft\" selbst, relative Häufigkeit auf die übrigen Wörter des semantischen Felds",
            "correct": False,
            "feedback": """× Nicht korrekt. Beide Häufigkeitsmaße können sich auf ein einzelnes Wort oder auf das gesamte semantische Feld beziehen. Der Unterschied liegt in der Art der Berechnung, nicht im betrachteten Wortmaterial."""
        },
        {
            "answer": "Absolute Häufigkeit wird auf Korpus I berechnet, relative Häufigkeit auf Korpus II",
            "correct": False,
            "feedback": """× Nicht korrekt. Beide Maße werden für jeden Text in beiden Korpora berechnet. Die Unterscheidung zwischen Korpus I und II betrifft das Zwei-Stichproben-Design der Fallstudie, nicht die Häufigkeitsberechnung."""
        },
        {
            "answer": "Absolute Häufigkeit ist die tatsächliche Anzahl des Vorkommens eines Wortes, relative Häufigkeit setzt diese ins Verhältnis zur Textlänge",
            "correct": True,
            "feedback": """✓ Richtig! Im Kapitel wird erklärt: "Dafür wird die absolute Häufigkeit durch die Textlänge dividiert, daraus ergibt sich die relative Häufigkeit." Die relative Häufigkeit kann als Anteil der Luftwörter am Gesamttext gesehen werden und ermöglicht den Vergleich von Texten unterschiedlicher Länge."""
        },
        {
            "answer": "Absolute Häufigkeit bezieht sich auf die Anzahl der Texte im Korpus, relative Häufigkeit auf die Anzahl der Wörter pro Text",
            "correct": False,
            "feedback": """× Nicht korrekt. Die absolute Häufigkeit zählt, wie oft ein Wort (bzw. die Wörter des semantischen Felds) in einem Text vorkommt – nicht die Anzahl der Texte. Die relative Häufigkeit ergibt sich, indem diese Anzahl durch die Textlänge geteilt wird."""
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
    "question": """Warum ist die Verwendung relativer Häufigkeiten bei der vergleichenden Analyse der literarischen Texte unseres Korpus sinnvoll?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Weil die Autor:innen unterschiedliche Schreibstile verwenden",
            "correct": False,
            "feedback": """× Nicht korrekt. Unterschiedliche Schreibstile sind zwar ein wichtiger Aspekt bei der Textanalyse, erklären aber nicht, warum relative statt absolute Häufigkeiten verwendet werden sollten."""
        },
        {
            "answer": "Weil die Texte unterschiedlich lang sein können und die relative Häufigkeit diese Unterschiede ausgleicht",
            "correct": True,
            "feedback": """✓ Richtig! Das Kapitel erklärt: "Wenn Texte verschieden lang sind, sollten die Häufigkeiten normalisiert werden, das heißt sie werden in Bezug zur Textlänge gesetzt." Unser Korpus enthält sowohl kurze Erzählungen mit wenigen hundert Tokens als auch lange Romane mit zehntausenden Tokens – erst die Normalisierung macht diese Texte fair vergleichbar."""
        },
        {
            "answer": "Weil absolute Häufigkeiten nur in Prozentangaben aussagekräftig sind",
            "correct": False,
            "feedback": """× Nicht korrekt. Absolute Häufigkeiten sind durchaus aussagekräftig, allerdings nicht für den Vergleich von Texten unterschiedlicher Länge. Prozentangaben sind eine Form der relativen Häufigkeit, nicht der absoluten."""
        },
        {
            "answer": "Weil die Texte aus unterschiedlichen Verlagen stammen",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Herkunft der Texte aus unterschiedlichen Verlagen hat keinen direkten Einfluss auf die Wahl zwischen absoluter und relativer Häufigkeit. Entscheidend ist vielmehr die Vergleichbarkeit der Textlängen."""
        }
    ]
}]

display_quiz(multiple_choice_3, colors=colors.jupyterquiz)
```

## Frage 4

Ein Text hat eine Länge von 500 Wörtern und enthält 15 Wörter aus dem semantischen Feld "Luft". Ein zweiter Text hat eine Länge von 800 Wörtern und enthält 20 Wörter aus demselben semantischen Feld. 

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_4 = [{
    "question": """Welche Aussage ist korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Der erste Text hat eine höhere absolute Häufigkeit von Luftwörtern",
            "correct": False,
            "feedback": """× Nicht korrekt. Der erste Text enthält 15 Luftwörter, der zweite 20 Luftwörter. Daher hat der zweite Text die höhere absolute Häufigkeit."""
        },
        {
            "answer": "Beide Texte haben dieselbe relative Häufigkeit von Luftwörtern",
            "correct": False,
            "feedback": """× Nicht korrekt. Die relative Häufigkeit des ersten Textes ist 15/500 = 0,03 (3%), die des zweiten Textes ist 20/800 = 0,025 (2,5%). Die relativen Häufigkeiten sind unterschiedlich."""
        },
        {
            "answer": "Der erste Text hat eine höhere relative Häufigkeit von Luftwörtern",
            "correct": True,
            "feedback": """✓ Richtig! Die relative Häufigkeit des ersten Textes beträgt 15/500 = 0,03 (3%), die des zweiten Textes 20/800 = 0,025 (2,5%). Obwohl der zweite Text mehr Luftwörter enthält (höhere absolute Häufigkeit), ist ihr Anteil am Gesamttext (relative Häufigkeit) geringer als im ersten Text – Luft ist im ersten Text also vermutlich präsenter."""
        },
        {
            "answer": "Aus den gegebenen Informationen kann keine Aussage über die Häufigkeiten getroffen werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Die gegebenen Informationen (Textlänge und Anzahl der Luftwörter) sind ausreichend, um sowohl absolute als auch relative Häufigkeiten zu berechnen und zu vergleichen."""
        }
    ]
}]

display_quiz(multiple_choice_4, colors=colors.jupyterquiz)
```

## Frage 5
Betrachten Sie folgende drei Texte aus demselben Erscheinungsjahr und ihre Häufigkeitswerte:

- Text A: 30 Luftwörter bei 600 Wörtern Gesamtlänge 
- Text B: 25 Luftwörter bei 400 Wörtern Gesamtlänge 
- Text C: 20 Luftwörter bei 500 Wörtern Gesamtlänge

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_5 = [{
    "question": """Was ist die korrekte relative Häufigkeit der Luftwörter, wenn alle drei Texte zusammen betrachtet werden – etwa um einen gemeinsamen Wert für dieses Jahr zu erhalten?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "0,05083 (5,083%)",
            "correct": False,
            "feedback": """× Nicht korrekt. Dieser Wert entspricht dem Durchschnitt der relativen Häufigkeiten (0,05 + 0,0625 + 0,04)/3 = 0,05083. Der Hinweiskasten "Durchschnitt von relativen Häufigkeiten" im Kapitel erklärt, warum diese Berechnungsmethode problematisch ist: Alle Texte desselben Jahres hätten den gleichen Einfluss auf das Ergebnis, unabhängig davon, wie lang sie sind – kurze Texte mit hohen Werten würden das Ergebnis verzerren."""
        },
        {
            "answer": "0,075 (7,5%)",
            "correct": False,
            "feedback": """× Nicht korrekt. Die korrekte Berechnung ist: Summe aller Luftwörter geteilt durch Summe aller Wörter: (30+25+20)/(600+400+500) = 75/1500 = 0,05 (5%)."""
        },
        {
            "answer": "0,0625 (6,25%)",
            "correct": False,
            "feedback": """× Nicht korrekt. Dieser Wert entspricht der relativen Häufigkeit von Text B (25/400 = 0,0625), nicht der Gesamthäufigkeit aller drei Texte."""
        },
        {
            "answer": "0,05 (5%)",
            "correct": True,
            "feedback": """✓ Richtig! Die korrekte Berechnung der relativen Häufigkeit für mehrere Texte addiert alle absoluten Häufigkeiten und teilt sie durch die Summe aller Textlängen: (30+25+20)/(600+400+500) = 75/1500 = 0,05 (5%). Wie im Kapitel erläutert, ist diese Methode besser als der Durchschnitt der einzelnen relativen Häufigkeiten, weil sonst kurze Texte einen unverhältnismäßig großen Einfluss auf das Ergebnis hätten."""
        }
    ]
}]

display_quiz(multiple_choice_5, colors=colors.jupyterquiz)
```

## Frage 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können das Konzept einer Trend-Linie beschreiben und die aus einem Streudiagramm erzeugte Trend-Linie interpretieren.
Bloom-Stufe: Verstehen, Analysieren
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_6 = [{
    "question": """Warum wird in dieser Fallstudie ein Streudiagramm als primäre Darstellungsform für die relativen Häufigkeiten des semantischen Felds "Luft" gewählt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Weil jeder Text als einzelner Datenpunkt erkennbar bleibt und sich so besonders auffällige Texte identifizieren lassen",
            "correct": True,
            "feedback": """✓ Richtig! Im Kapitel wird erklärt, dass die Datenpunkte nicht pro Jahr oder Dekade aggregiert werden sollen, sondern jeder Text einzeln erkennbar sein soll – etwa um Texte zu finden, in denen Luft besonders häufig thematisiert wird und die möglicherweise wegweisend gewesen sein könnten. Im Streudiagramm ist jeder der 450 Texte eines Korpus ein Punkt: Der X-Wert ist das Publikationsjahr, der Y-Wert die relative Häufigkeit."""
        },
        {
            "answer": "Weil Streudiagramme die einzige Darstellungsform sind, die zeitliche Entwicklungen zeigen kann",
            "correct": False,
            "feedback": """× Nicht korrekt. Das Kapitel nennt ausdrücklich das Liniendiagramm als Alternative: Wenn es weniger wichtig ist, die Häufigkeiten einzelner Texte abzulesen, lassen sich die Werte über Zeiträume zusammenfassen und als Liniendiagramm darstellen, in dem lokale und globale Minima und Maxima leicht erkennbar sind."""
        },
        {
            "answer": "Weil das Streudiagramm die Datenpunkte automatisch pro Jahrzehnt zusammenfasst",
            "correct": False,
            "feedback": """× Nicht korrekt. Das Gegenteil ist der Fall: Das Streudiagramm wurde gerade deshalb gewählt, weil es *nicht* aggregiert – jeder Text bleibt als einzelner Punkt sichtbar. Eine Zusammenfassung über Zeiträume wäre eher die Grundlage für ein Liniendiagramm."""
        },
        {
            "answer": "Weil sich im Streudiagramm absolute und relative Häufigkeiten gleichzeitig auf einer Achse darstellen lassen",
            "correct": False,
            "feedback": """× Nicht korrekt. Auch im Streudiagramm wird auf der Y-Achse nur ein Maß dargestellt – in unserem Fall die relative Häufigkeit (pro 100 Tokens). Absolute und relative Häufigkeiten haben unterschiedliche Maßeinheiten und können nicht sinnvoll auf derselben Skala liegen."""
        }
    ]
}]

display_quiz(multiple_choice_6, colors=colors.jupyterquiz)
```

## Frage 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_7 = [{
    "question": """Welche Aussage über die Trend-Linie (Regressionsgerade) im Streudiagramm ist korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie verbindet alle Datenpunkte der Reihe nach miteinander",
            "correct": False,
            "feedback": """× Nicht korrekt. Das würde eher einem Linienzug durch alle Punkte entsprechen. Die Regressionsgerade ist eine einzelne Gerade, die das Gesamtmuster der Punktwolke zusammenfasst – sie läuft in der Regel *zwischen* den Punkten hindurch, nicht durch alle hindurch."""
        },
        {
            "answer": "Sie wird so berechnet, dass die Summe der quadrierten vertikalen Abstände aller Punkte zur Geraden möglichst klein ist; ihre Steigung zeigt eine Zu- oder Abnahme an",
            "correct": True,
            "feedback": """✓ Richtig! Diese Berechnungsweise heißt Methode der kleinsten Quadrate: Für jeden Punkt wird der vertikale Abstand zur Geraden bestimmt, die Abstände werden quadriert (damit sich positive und negative Abweichungen nicht aufheben) und die beste Gerade minimiert deren Summe. Steigt die Gerade, nimmt das semantische Feld "Luft" über die Zeit zu; fällt sie, nimmt es ab; verläuft sie waagerecht, zeigt sich kein Zusammenhang."""
        },
        {
            "answer": "Schon ab zwei Datenpunkten liefert die Trend-Linie einen generalisierbaren Trend",
            "correct": False,
            "feedback": """× Nicht korrekt. Zwar lässt sich rechnerisch schon ab zwei Datenpunkten eine Regressionsgerade bestimmen, doch das Kapitel warnt ausdrücklich: Um mittels der Regressionsgeraden tatsächlich einen Effekt zu messen, sollten mindestens 30 Datenpunkte vorliegen, die möglichst gleichmäßig über die Zeit verteilt sind."""
        },
        {
            "answer": "Eine steigende Trend-Linie beweist, dass die Industrialisierung die Ursache für die häufigere Thematisierung von Luft ist",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Trend-Linie beschreibt lediglich einen statistischen Zusammenhang zwischen Publikationsjahr und relativer Häufigkeit. Ob eine beobachtete Zunahme tatsächlich auf die Industrialisierung zurückgeht, ist eine Interpretationsfrage, die zusätzliche (auch qualitative) Evidenz erfordert – Korrelation ist keine Kausalität."""
        }
    ]
}]

display_quiz(multiple_choice_7, colors=colors.jupyterquiz)
```

## Frage 8
(Wählen Sie alle zutreffenden Antworten aus)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können die notwendigen Schritte zur Frequenzanalyse eines semantischen Felds aufzählen, Unterschiede in der Berechnung der Häufigkeiten benennen und die Ergebnisse reflektieren.
Bloom-Stufe: Verstehen, Analysieren
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_8 = [{
    "question": """Welche Schritte sind für die Frequenzanalyse des semantischen Felds "Luft" auf unseren literarischen Korpora notwendig?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Einlesen des annotierten Korpus (CSV-Dateien) und der Metadaten für Korpus I und II",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook werden zunächst die annotierten CSV-Dateien aller 724 Texte sowie die beiden Metadaten-Tabellen eingelesen. Die Metadaten liefern unter anderem das Publikationsjahr (Spalte `DC.date`) und entscheiden über die Spalte `DC.identifier`, welche Texte zu Korpus I bzw. Korpus II gehören."""
        },
        {
            "answer": "Einlesen der definierten Wortliste (semantisches Feld \"Luft\")",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook wird die Datei `luft_semantisches_feld.txt` eingelesen, die die Substantive des semantischen Felds enthält. Diese Wörter werden mit den Lemmata in den annotierten Texten verglichen."""
        },
        {
            "answer": "Manuelle Annotation aller Texte nach relevanten Begriffen",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Texte wurden bereits im Kapitel Korpusverarbeitung automatisch annotiert (tokenisiert und lemmatisiert) und liegen als CSV-Dateien vor. Eine manuelle Annotation ist nicht Teil des Analyseprozesses."""
        },
        {
            "answer": "Berechnung der relativen Häufigkeit des semantischen Felds für jeden einzelnen Text",
            "correct": True,
            "feedback": """✓ Richtig! Die Funktion `extract_noun_list_counts` zählt für jeden Text die Treffer aus der Wortliste, und `get_relative_frequencies` berechnet daraus die relative Häufigkeit – die Treffer geteilt durch die Gesamtzahl der Tokens des Textes, mal 100 (Treffer pro 100 Tokens)."""
        },
        {
            "answer": "Visualisierung der Ergebnisse als Streudiagramm mit Trend-Linie",
            "correct": True,
            "feedback": """✓ Richtig! Die berechneten Häufigkeiten werden in einem interaktiven Streudiagramm dargestellt: Jeder Text ist ein Punkt (X-Wert: Publikationsjahr, Y-Wert: relative Häufigkeit), und eine per linearer Regression berechnete Trend-Linie zeigt die Entwicklung über das Jahrhundert an."""
        }
    ]
}]

display_quiz(multiple_choice_8, colors=colors.jupyterquiz)
```

## Frage 9

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_9 = [{
    "question": """Wie wird im Notebook der Wert in der Spalte `relative_frequency` der Ergebnistabelle für einen Text berechnet?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Anzahl der Treffer aus dem semantischen Feld geteilt durch die Anzahl der Wörter in der Wortliste",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Größe der Wortliste spielt für die Berechnung keine Rolle. Die Treffer werden ins Verhältnis zur Länge des jeweiligen *Textes* gesetzt, nicht zur Länge der Wortliste."""
        },
        {
            "answer": "Anzahl der Treffer aus dem semantischen Feld (total_count_semantic_field) geteilt durch die Gesamtzahl der Tokens des Textes (total_count_tokens), multipliziert mit 100",
            "correct": True,
            "feedback": """✓ Richtig! Die Funktion `get_relative_frequencies` berechnet `relative_frequency` als `total_count_semantic_field / total_count_tokens * 100` – also die Treffer pro 100 Tokens. Ein hoher Wert bedeutet, dass das semantische Feld "Luft" in diesem Text besonders präsent ist, unabhängig davon, wie lang der Text ist."""
        },
        {
            "answer": "Gesamtzahl der Tokens des Textes geteilt durch die Anzahl der Texte im Korpus",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Rechnung ergäbe eine durchschnittliche Textlänge, keine Häufigkeit des semantischen Felds. Die Anzahl der Texte im Korpus geht in die relative Häufigkeit eines einzelnen Textes nicht ein."""
        },
        {
            "answer": "Anzahl der Treffer aus dem semantischen Feld multipliziert mit der Textlänge",
            "correct": False,
            "feedback": """× Nicht korrekt. Eine Multiplikation mit der Textlänge würde lange Texte zusätzlich bevorzugen. Die Normalisierung funktioniert genau umgekehrt: Die absolute Häufigkeit wird durch die Textlänge *dividiert*, damit Texte unterschiedlicher Länge vergleichbar werden."""
        }
    ]
}]

display_quiz(multiple_choice_9, colors=colors.jupyterquiz)
```

## Frage 10

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_10 = [{
    "question": """Warum ist die Unterscheidung zwischen absoluten und relativen Häufigkeiten bei der diachronen Analyse – also der Analyse über die Zeit hinweg – wichtig?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Absolute Häufigkeiten sind präziser und sollten daher immer bevorzugt werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Absolute Häufigkeiten geben zwar die tatsächliche Anzahl der Vorkommen an, können aber bei unterschiedlich langen Texten zu verzerrten Ergebnissen führen: Ein langer Roman hätte fast zwangsläufig mehr Luftwörter als eine kurze Erzählung, selbst wenn Luft in der Erzählung eine viel größere Rolle spielt."""
        },
        {
            "answer": "Relative Häufigkeiten berücksichtigen, dass die Texte aus verschiedenen Jahren unterschiedlich lang sind",
            "correct": True,
            "feedback": """✓ Richtig! Relative Häufigkeiten setzen die Anzahl der Vorkommen ins Verhältnis zur Textlänge. Da unsere 450 Texte pro Korpus sehr unterschiedlich lang sind und sich über das ganze Jahrhundert verteilen, wäre ein Vergleich absoluter Zahlen über die Zeit hinweg irreführend – erst die Normalisierung macht die Entwicklung im Streudiagramm interpretierbar."""
        },
        {
            "answer": "Absolute Häufigkeiten sind nur für frühe Texte relevant, relative Häufigkeiten nur für späte",
            "correct": False,
            "feedback": """× Nicht korrekt. Beide Maße lassen sich für Texte aus allen Zeiträumen berechnen. Die Wahl zwischen absoluter und relativer Häufigkeit hängt vom Analyseziel und der Vergleichbarkeit der Texte ab, nicht vom Publikationsjahr."""
        },
        {
            "answer": "Die Unterscheidung ist nur wichtig, wenn zwei verschiedene Korpora verglichen werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Diese Aussage ist zu eingeschränkt. Auch innerhalb eines einzelnen Korpus variieren die Textlängen stark, sodass die Normalisierung bei jeder diachronen Analyse wichtig ist – nicht nur beim Vergleich von Korpus I und Korpus II."""
        }
    ]
}]

display_quiz(multiple_choice_10, colors=colors.jupyterquiz)
```

## Frage 11

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_11 = [{
    "question": """Welche zeitliche Information steht für die diachrone Analyse unserer literarischen Texte zur Verfügung?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Das exakte Erscheinungsdatum mit Tag und Monat, sodass die Häufigkeiten nach Tagen, Wochen und Monaten aggregiert werden können",
            "correct": False,
            "feedback": """× Nicht korrekt. Anders als etwa bei Zeitungskorpora liegt für literarische Werke kein genaues Erscheinungsdatum vor. Eine Aggregation nach Tagen, Wochen oder Monaten ist deshalb nicht möglich."""
        },
        {
            "answer": "Nur das Publikationsjahr, das als ganze Zahl in der Metadaten-Spalte DC.date steht",
            "correct": True,
            "feedback": """✓ Richtig! Für jeden Text ist als zeitliche Angabe nur das Publikationsjahr verfügbar; es steht als ganze Zahl (z.B. 1861) in der Spalte `DC.date`, dem Dublin-Core-Feld für das Erscheinungsdatum. Alle zeitbasierten Auswertungen – das Streudiagramm, die Trend-Linie und die Aggregation nach Jahrzehnten in der N-Gramm-Analyse – stützen sich auf dieses Jahr."""
        },
        {
            "answer": "Das Datum wird automatisch aus dem Text selbst extrahiert, z.B. aus erwähnten historischen Ereignissen",
            "correct": False,
            "feedback": """× Nicht korrekt. Die zeitliche Einordnung stammt aus den bibliografischen Metadaten des *Corpus of German-Language Fiction*, nicht aus einer inhaltlichen Analyse der Texte. Eine automatische Datierung anhand des Textinhalts wäre ein eigenes (fehleranfälliges) Forschungsproblem."""
        },
        {
            "answer": "Es liegt keine zeitliche Information vor, deshalb wird die Reihenfolge der Dateien im Ordner verwendet",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Reihenfolge der Dateien im Dateisystem hat keinerlei inhaltliche Bedeutung. Die zeitliche Einordnung erfolgt über das Publikationsjahr in den Metadaten, die über die Spalte `DC.identifier` mit den annotierten Texten verknüpft werden."""
        }
    ]
}]

display_quiz(multiple_choice_11, colors=colors.jupyterquiz)
```

## Frage 12

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_12 = [{
    "question": """Zu welchem Ergebnis kommt die Häufigkeitsanalyse des semantischen Felds "Luft" auf unseren beiden Korpora?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die relative Häufigkeit steigt parallel zur Industrialisierung stark an – die Literatur reagiert deutlich auf die Luftverschmutzung",
            "correct": False,
            "feedback": """× Nicht korrekt. Genau dieser erwartbare Befund bleibt aus: Die Trend-Linie steigt in beiden Korpora zwar leicht an, der Anstieg ist aber nicht maßgeblich. Ein deutlicher Aufwärtstrend, der eine wachsende Auseinandersetzung mit Luft(-verschmutzung) belegen würde, lässt sich nicht nachweisen."""
        },
        {
            "answer": "Die Trend-Linie steigt in beiden Korpora nur leicht und nicht maßgeblich an; auffällig sind einzelne Ausreißertexte, besonders gegen Ende des Jahrhunderts",
            "correct": True,
            "feedback": """✓ Richtig! In beiden Streudiagrammen ist kein deutlicher Aufwärts- oder Abwärtstrend erkennbar. Auffällig sind jedoch Ausreißer wie "Das Dorf im Gebirge" (von Hofmannsthal) oder "Das Schattenspiel. Eine Morgenwanderung" (Flaischlen), die beide Natur zum Thema haben – ein möglicher Ansatzpunkt für weitere Analysen zur Naturdarstellung."""
        },
        {
            "answer": "Die relative Häufigkeit nimmt über das Jahrhundert kontinuierlich ab – Luft verschwindet als literarisches Thema",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Trend-Linie fällt nicht, sondern steigt leicht an. Von einem Verschwinden des Themas kann keine Rede sein; es lässt sich nur eben auch keine maßgebliche Zunahme feststellen."""
        },
        {
            "answer": "Korpus I und Korpus II liefern gegensätzliche Trends, sodass keine Aussage möglich ist",
            "correct": False,
            "feedback": """× Nicht korrekt. Die beiden Stichproben liefern konsistente Ergebnisse: In beiden steigt die Trend-Linie nur leicht an. Gerade diese Übereinstimmung spricht dafür, dass der Befund robust ist und nicht von der konkreten Zufallsauswahl abhängt."""
        }
    ]
}]

display_quiz(multiple_choice_12, colors=colors.jupyterquiz)
```

## Frage 13

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können das Konzept von syntaktischen n-Grammen in Bezug auf Adjektiv-Nomen-Paare beschreiben und die notwendigen Schritte zur automatischen Extraktion der syntaktischen n-Gramme aufzählen.
Bloom-Stufe: Verstehen, Analysieren
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_13 = [{
    "question": """Was ist ein (lineares) n-Gramm?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die n häufigsten Wörter eines Textes",
            "correct": False,
            "feedback": """× Nicht korrekt. Das wäre eine Frequenzliste. Ein n-Gramm ist keine Auswahl nach Häufigkeit, sondern eine Sequenz von Tokens, die im Text unmittelbar aufeinanderfolgen."""
        },
        {
            "answer": "Eine Sequenz von n unmittelbar aufeinanderfolgenden Tokens – etwa das 2-Gramm \"frischer Wind\" oder das 3-Gramm \"ein frischer Wind\"",
            "correct": True,
            "feedback": """✓ Richtig! N-Gramme modellieren Sprache als Sequenzen von n aufeinanderfolgenden Tokens. Aus der Phrase "ein frischer Wind spielte mit unsern Locken" entstehen z.B. die 2-Gramme "ein frischer", "frischer Wind", "Wind spielte" usw. Da diese Sequenzen der linearen Abfolge der Tokens im Text folgen, spricht man von *linearen* n-Grammen. So werden wiederkehrende Mehrwortmuster wie Kollokationen oder feste Wendungen sichtbar."""
        },
        {
            "answer": "Eine Gruppe von n Wörtern mit ähnlicher Bedeutung",
            "correct": False,
            "feedback": """× Nicht korrekt. Eine Gruppe bedeutungsverwandter Wörter entspricht eher einem semantischen Feld. N-Gramme sind über die *Abfolge* im Text definiert, nicht über Bedeutungsähnlichkeit."""
        },
        {
            "answer": "Ein Wort, das aus genau n Buchstaben besteht",
            "correct": False,
            "feedback": """× Nicht korrekt. Das n in n-Gramm bezieht sich auf die Anzahl der Tokens in der Sequenz (Unigramm, Bigramm, Trigramm, …), nicht auf die Anzahl der Buchstaben eines Wortes. (Zeichen-n-Gramme existieren zwar auch, in diesem Kapitel sind aber Token-Sequenzen gemeint.)"""
        }
    ]
}]

display_quiz(multiple_choice_13, colors=colors.jupyterquiz)
```

## Frage 14

Betrachten Sie den Beispielsatz aus dem Kapitel:

> *Ich roch eine üble, von den Schloten der neuen Fabriken schwer geschwängerte Luft.*

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_14 = [{
    "question": """Warum kann eine lineare 2-Gramm-Analyse das inhaltlich zentrale Paar "üble Luft" in diesem Satz nicht als Muster erfassen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Weil \"üble\" in diesem Satz kein Adjektiv ist",
            "correct": False,
            "feedback": """× Nicht korrekt. "Üble" ist sehr wohl ein Adjektiv und charakterisiert semantisch klar die "Luft". Das Problem liegt nicht in der Wortart, sondern in der linearen Distanz zwischen Adjektiv und Substantiv."""
        },
        {
            "answer": "Weil lineare n-Gramme nur unmittelbar benachbarte Tokens erfassen und \"üble\" hier durch die lange attributive Erweiterung von \"Luft\" getrennt ist",
            "correct": True,
            "feedback": """✓ Richtig! Lineare 2-Gramme bestehen nur aus direkt aufeinanderfolgenden Tokens – hier also z.B. "eine üble", "üble von", …, "geschwängerte Luft". Das Partizipialattribut "von den Schloten der neuen Fabriken schwer geschwängerte" schiebt sich zwischen "üble" und "Luft", sodass die zusammengehörige Einheit fragmentiert wird. Gerade im Deutschen mit seiner flexiblen Wortstellung und Konstruktionen wie Partizipialattributen oder Verbklammern tritt dieses Problem häufig auf."""
        },
        {
            "answer": "Weil der Satz zu viele Tokens enthält, um überhaupt n-Gramme zu berechnen",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Länge eines Satzes ist für die Berechnung von n-Grammen kein Hindernis – aus einem langen Satz entstehen einfach mehr n-Gramme. Das Problem ist die *Diskontinuität*: Zusammengehörige Wörter stehen nicht nebeneinander."""
        },
        {
            "answer": "Weil 2-Gramme grundsätzlich keine Adjektiv-Substantiv-Paare enthalten können",
            "correct": False,
            "feedback": """× Nicht korrekt. Stehen Adjektiv und Substantiv direkt nebeneinander (wie in "frische Luft"), erfasst auch ein lineares 2-Gramm das Paar problemlos. Nur wenn Einschübe die beiden Wörter trennen, versagt der lineare Ansatz."""
        }
    ]
}]

display_quiz(multiple_choice_14, colors=colors.jupyterquiz)
```

## Frage 15

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_15 = [{
    "question": """Was macht ein n-Gramm zu einem *syntaktischen* n-Gramm?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Es besteht nur aus grammatisch korrekten Wortfolgen, die aus den linearen n-Grammen herausgefiltert wurden",
            "correct": False,
            "feedback": """× Nicht korrekt. Syntaktische n-Gramme sind keine gefilterte Teilmenge der linearen n-Gramme. Sie werden auf einer ganz anderen Grundlage gebildet: nicht auf der Textoberfläche, sondern auf der syntaktischen Struktur des Satzes."""
        },
        {
            "answer": "Die Sequenz wird nicht über die lineare Tokenfolge definiert, sondern über Pfade in der syntaktischen Struktur, typischerweise im Dependenzbaum",
            "correct": True,
            "feedback": """✓ Richtig! Syntaktische n-Gramme redefinieren, was als Sequenz gilt: Sie folgen den Relationen einer syntaktischen Analyse (typischerweise eines Dependenzbaums) statt der Wortstellung im Text. Im Beispielsatz ist "üble" im Dependenzbaum direkt als Attribut von "Luft" analysiert – unabhängig davon, wie viele Wörter auf der Textoberfläche dazwischenstehen. Genau dafür wurde im Kapitel Korpusverarbeitung die Dependenzannotation mit spaCy erzeugt."""
        },
        {
            "answer": "Es umfasst immer einen vollständigen Satz vom ersten bis zum letzten Token",
            "correct": False,
            "feedback": """× Nicht korrekt. Syntaktische n-Gramme sind in der Regel kleine Einheiten – in unserer Analyse Wortpaare (syntaktische Bigramme) wie "übel ← Luft" –, keine vollständigen Sätze."""
        },
        {
            "answer": "Es wird manuell von Linguist:innen annotiert statt automatisch berechnet",
            "correct": False,
            "feedback": """× Nicht korrekt. Die syntaktischen n-Gramme werden automatisch aus den Dependenzannotationen extrahiert, die das spaCy-Modell `de_core_news_sm` erzeugt hat. Eine manuelle Annotation findet nicht statt – gerade die Automatisierbarkeit macht die Methode für große Korpora attraktiv."""
        }
    ]
}]

display_quiz(multiple_choice_15, colors=colors.jupyterquiz)
```

## Frage 16

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_16 = [{
    "question": """Warum eignen sich Adjektiv-Substantiv-Paare mit "Luft", um die *Semantisierung* von Luft – den zweiten Teil unserer Operationalisierung – zu untersuchen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Weil Adjektive in literarischen Texten häufiger vorkommen als Substantive",
            "correct": False,
            "feedback": """× Nicht korrekt. Die relative Häufigkeit von Wortarten ist hier nicht der Punkt. Entscheidend ist die *Funktion* der Adjektive: Sie bestimmen das Substantiv inhaltlich näher und geben ihm eine Bewertung mit."""
        },
        {
            "answer": "Weil die Adjektive zeigen, WIE Luft charakterisiert und bewertet wird – etwa als \"frische Luft\" oder \"verdorbene Luft\" – und nicht nur, WIE OFT sie erwähnt wird",
            "correct": True,
            "feedback": """✓ Richtig! Während die Häufigkeitsanalyse des semantischen Felds misst, *wie häufig* Luft thematisiert wird, fragt die N-Gramm-Analyse danach, *auf welche Art und Weise* über Luft gesprochen wird. Die Adjektive, die "Luft" syntaktisch modifizieren, machen diese Semantisierung messbar: Eine Zunahme von Adjektiven wie "verdorben" oder "rauchig" wäre ein Indiz für eine literarische Reaktion auf die Luftverschmutzung, eine Dominanz von "frisch" und "rein" spricht dagegen."""
        },
        {
            "answer": "Weil das Wort \"Luft\" ohne Adjektiv im Deutschen nicht verwendet werden kann",
            "correct": False,
            "feedback": """× Nicht korrekt. "Luft" kommt selbstverständlich auch ohne adjektivische Modifikatoren vor – das zeigt schon die Spalte `noun_count` im Notebook, die alle Vorkommen von "Luft" zählt, während `count` nur die adjektivisch modifizierten erfasst."""
        },
        {
            "answer": "Weil nur Adjektive von den spaCy-Modellen zuverlässig erkannt werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Die spaCy-Modelle annotieren alle Wortarten sowie die Dependenzstruktur. Die Beschränkung auf Adjektiv-Substantiv-Paare ist eine inhaltlich begründete Entscheidung der Operationalisierung, keine technische Notwendigkeit."""
        }
    ]
}]

display_quiz(multiple_choice_16, colors=colors.jupyterquiz)
```

## Frage 17

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_17 = [{
    "question": """Mit welcher Kombination von Annotationen werden im Notebook die Adjektive identifiziert, die das Substantiv "Luft" näher bestimmen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Dependenzlabel \"amod\" in Kombination mit dem POS-Tag \"ADJ\"",
            "correct": False,
            "feedback": """× Nicht korrekt – aber knapp daneben. Das Label "amod" (adjectival modifier) wird im Englischen und einigen anderen Sprachen verwendet. Die Standard-spaCy-Modelle für das Deutsche annotieren die syntaktische Position eines adjektivischen Modifikators aus historischen Gründen jedoch mit "nk" (noun kernel element)."""
        },
        {
            "answer": "Dependenzlabel \"nk\" (noun kernel element) in Kombination mit dem POS-Tag \"ADJ\"",
            "correct": True,
            "feedback": """✓ Richtig! Die Funktion `extract_dependent_adjective_list` durchläuft alle Tokens: Ist ein Token ein Substantiv mit dem Lemma "Luft", werden seine syntaktischen Kinder geprüft – gezählt wird ein Kind genau dann, wenn es das Dependenzlabel "nk" und das POS-Tag "ADJ" trägt. Die deutschen spaCy-Modelle verwenden "nk" anstelle des in anderen Sprachen üblichen Labels "amod"."""
        },
        {
            "answer": "Alle Tokens, die im Text unmittelbar vor \"Luft\" stehen",
            "correct": False,
            "feedback": """× Nicht korrekt. Das wäre wieder der lineare Ansatz, dessen Grenzen wir gerade überwinden wollen: Er würde Fälle wie "eine üble, von den Schloten … geschwängerte Luft" verpassen (dort steht "geschwängerte" direkt vor "Luft", "üble" aber weit entfernt). Die Extraktion folgt stattdessen den Dependenzrelationen."""
        },
        {
            "answer": "Alle Wörter aus der Wortliste des semantischen Felds \"Luft\"",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Wortliste des semantischen Felds enthält Substantive und gehört zur ersten Analyse (Häufigkeitsanalyse). Die N-Gramm-Analyse extrahiert dagegen Adjektive aus der Dependenzstruktur – sie benötigt keine vordefinierte Adjektivliste, sondern findet alle vorkommenden Modifikatoren selbst."""
        }
    ]
}]

display_quiz(multiple_choice_17, colors=colors.jupyterquiz)
```

## Frage 18

Bringen Sie die Schritte der syntaktischen N-Gramm-Analyse in die Reihenfolge, in der sie im Notebook durchgeführt werden.

```{code-cell} ipython3
:tags: [remove-input]

"""
Lernziel: Sie können die notwendigen Schritte zur automatischen Extraktion der syntaktischen n-Gramme aufzählen und in die richtige Reihenfolge bringen.
Bloom-Stufe: Verstehen, Anwenden
Format: Drag & Drop (Reihenfolge)
"""

import sys
sys.path.append("../quadriga")
from assessment import DragDropQuiz

schritt_1 = "Einlesen der gespeicherten spaCy-Annotationen (DocBin-Dateien) und der Metadaten"
schritt_2 = "Extraktion der abhängigen Adjektive von \"Luft\" über Dependenzlabel \"nk\" und POS-Tag \"ADJ\""
schritt_3 = "Aggregation und Visualisierung der Adjektiv-Häufigkeiten im Zeitverlauf"
schritt_4 = "Identifikation von Ausreißertexten, die die Ausschläge in den Zeitreihen (mit-)verursachen"
schritt_5 = "KWIC-Kontextanalyse der Belegstellen aus den Ausreißertexten zur qualitativen Einordnung"

quiz = DragDropQuiz()
quiz.create_matching_quiz(
    title="Ordnen Sie die Schritte der syntaktischen N-Gramm-Analyse in der richtigen Reihenfolge an:",
    descriptions=["Schritt 1", "Schritt 2", "Schritt 3", "Schritt 4", "Schritt 5"],
    options=[schritt_3, schritt_5, schritt_1, schritt_4, schritt_2],
    correct_mapping={
        "Schritt 1": schritt_1,
        "Schritt 2": schritt_2,
        "Schritt 3": schritt_3,
        "Schritt 4": schritt_4,
        "Schritt 5": schritt_5,
    },
    feedback_messages={
        "correct": "Perfekt! Alle {total} Schritte sind in der richtigen Reihenfolge: Zuerst werden die im Kapitel Korpusverarbeitung erzeugten Dependenzannotationen und die Metadaten eingelesen, dann werden die Adjektiv-Substantiv-Paare extrahiert, anschließend über die Zeit aggregiert und visualisiert, bevor Ausreißertexte identifiziert und per KWIC qualitativ eingeordnet werden.",
        "incorrect": "Leider ist keine Zuordnung korrekt. Überlegen Sie: Was muss vorliegen, bevor extrahiert werden kann – und was wird erst geprüft, nachdem die Zeitreihen Ausschläge gezeigt haben? Sehen Sie sich ggf. die Übersicht am Anfang des Notebooks noch einmal an.",
        "partial": "Teilweise richtig: {correct} von {total} Schritten sind korrekt platziert. Tipp: Die quantitative Auswertung (Extraktion, Aggregation) kommt vor der qualitativen Überprüfung (Ausreißer, KWIC).",
    },
)
```

## Frage 19

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_19 = [{
    "question": """Zu welchem Ergebnis kommt die syntaktische N-Gramm-Analyse der Adjektive, die "Luft" näher bestimmen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Adjektive wie \"verdorben\", \"rauchig\" und \"stickig\" dominieren und belegen eine kritische Auseinandersetzung mit der Luftverschmutzung",
            "correct": False,
            "feedback": """× Nicht korrekt. Genau dieser Befund bleibt aus: In der Liste der häufigsten Adjektive spiegeln sich keinerlei Anzeichen für schlechte Luftqualität wider. Negativ konnotierte Modifikatoren spielen quantitativ kaum eine Rolle."""
        },
        {
            "answer": "\"Frisch\" ist mit Abstand der häufigste Modifikator, gefolgt von \"frei\"; die dominierenden Adjektive sind durchweg positiv konnotiert",
            "correct": True,
            "feedback": """✓ Richtig! In beiden Korpora steht "frisch" eindeutig an der Spitze und "frei" ist das zweithäufigste Adjektiv; die übrigen Adjektive weisen deutlich geringere Häufigkeiten auf. Die Dominanz positiv konnotierter Adjektive wie "frisch", "rein" und "frei" deutet darauf hin, dass die Literatur eher in die Richtung reagiert, die in der Operationalisierung als utopischer Gegenentwurf beschrieben wurde – mit einer herausgehoben positiven Semantik von "Luft"."""
        },
        {
            "answer": "Ab etwa 1850 lösen negative Adjektive die positiven vollständig ab",
            "correct": False,
            "feedback": """× Nicht korrekt. Ein solcher Umschwung zeigt sich in den diachronen Verläufen (gleitender 10-Jahres-Durchschnitt) nicht. Die dominanten Modifikatoren – insbesondere "frisch" – bleiben über das Jahrhundert hinweg stabil."""
        },
        {
            "answer": "Es wurden keine Adjektiv-Substantiv-Paare mit \"Luft\" gefunden, sodass die Analyse ergebnislos blieb",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Extraktion liefert in beiden Korpora zahlreiche Adjektiv-Substantiv-Paare – die Konstruktionen wie "frische Luft" oder "freie Luft" sind sogar sehr häufig. Der Befund ist nicht das Fehlen von Daten, sondern deren durchweg positive Konnotation."""
        }
    ]
}]

display_quiz(multiple_choice_19, colors=colors.jupyterquiz)
```

## Frage 20

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_20 = [{
    "question": """Warum werden alle Analysen dieser Fallstudie parallel auf zwei Korpora (Korpus I und Korpus II) durchgeführt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Weil Korpus I die erste und Korpus II die zweite Hälfte des 19. Jahrhunderts abdeckt",
            "correct": False,
            "feedback": """× Nicht korrekt. Beide Korpora decken denselben Zeitraum ab: Aus dem auf das 19. Jahrhundert eingegrenzten *Corpus of German-Language Fiction* wurden pro Jahrzehnt jeweils bis zu 50 Texte gezogen – für beide Stichproben gleichermaßen. Der Unterschied liegt allein in der Zufallsauswahl (Random State 42 bzw. 31415)."""
        },
        {
            "answer": "Weil zwei unabhängige Zufallsstichproben eine Robustheitsprüfung ermöglichen: Zeigen beide dieselben Muster, hängen die Befunde nicht von der konkreten Zufallsauswahl ab",
            "correct": True,
            "feedback": """✓ Richtig! Korpus I und Korpus II sind zwei unabhängig gezogene Stichproben aus demselben Quellkorpus. Führt man alle Analysen parallel durch, lässt sich einschätzen, welche Muster robust sind: Tatsächlich liefern beide Stichproben sehr ähnliche Ergebnisse – die Trend-Linien steigen in beiden nur leicht an, und die Listen der zehn häufigsten Adjektive enthalten dieselben Begriffe in nur geringfügig unterschiedlicher Reihenfolge. Das spricht dafür, dass die Befunde nicht durch die spezifische Textauswahl verursacht sind."""
        },
        {
            "answer": "Weil Korpus II als Kontrollkorpus keine Texte mit Luftwörtern enthält",
            "correct": False,
            "feedback": """× Nicht korrekt. Korpus II ist kein Kontrollkorpus ohne Luftwörter, sondern eine zweite, gleichartig gezogene Zufallsstichprobe. Beide Korpora enthalten Texte mit und ohne Bezug zum semantischen Feld – 176 Texte kommen sogar in beiden Stichproben vor."""
        },
        {
            "answer": "Weil erst die doppelte Textmenge statistisch signifikante Ergebnisse ermöglicht",
            "correct": False,
            "feedback": """× Nicht korrekt. Die beiden Korpora werden nicht zu einer größeren Datenmenge zusammengelegt, sondern getrennt analysiert und miteinander verglichen. Es geht nicht um mehr Daten, sondern um die Überprüfung, ob die Ergebnisse gegenüber unterschiedlichen Stichproben stabil sind."""
        }
    ]
}]

display_quiz(multiple_choice_20, colors=colors.jupyterquiz)
```

## Frage 21

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

"""
Lernziel: Sie können die Darstellungsmethode Keyword in Context beschreiben und ihre Funktion bei der qualitativen Überprüfung quantitativer Ergebnisse erklären.
Format: Multiple Choice
"""


import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_21 = [{
    "question": """Was ist der Hauptzweck der KWIC-Darstellung (Keyword in Context) in der Textanalyse?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die automatische Lemmatisierung von Texten",
            "correct": False,
            "feedback": """× Nicht korrekt. Die KWIC-Darstellung dient nicht der Lemmatisierung von Texten. Die Lemmatisierung ist ein separater Vorverarbeitungsschritt, der bereits im Kapitel Korpusverarbeitung durchgeführt wurde."""
        },
        {
            "answer": "Die Anzeige von Suchbegriffen mit ihrem unmittelbaren textuellen Kontext",
            "correct": True,
            "feedback": """✓ Richtig! Die KWIC-Darstellung zeigt den gesuchten Ausdruck – in unserem Notebook die jeweilige Adjektiv-Nomen-Konstruktion wie "frische Luft" – in der Mitte einer Zeile an, flankiert von einigen Wörtern unmittelbar davor und danach. So lässt sich auf einen Blick lesen, in welchem sprachlichen Umfeld ein Ausdruck tatsächlich vorkommt, und seine Verwendung qualitativ einordnen."""
        },
        {
            "answer": "Die statistische Berechnung von Wortfrequenzen",
            "correct": False,
            "feedback": """× Nicht korrekt. Die KWIC-Darstellung berechnet keine statistischen Werte wie Wortfrequenzen. Sie dient vielmehr der kontextuellen Einbettung von bereits identifizierten Treffern – im Notebook ergänzt sie die zuvor berechneten Häufigkeiten der Adjektiv-Nomen-Paare."""
        },
        {
            "answer": "Die grafische Visualisierung von Häufigkeiten über Zeit",
            "correct": False,
            "feedback": """× Nicht korrekt. Für die Visualisierung von Häufigkeiten über Zeit werden in diesem Kapitel Streudiagramme mit Trend-Linien und Liniendiagramme mit gleitendem Durchschnitt verwendet. Die KWIC-Darstellung ist dagegen eine tabellarische, konkordanzartige Ansicht einzelner Belegstellen."""
        }
    ]
}]

display_quiz(multiple_choice_21, colors=colors.jupyterquiz)
```

## Frage 22

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_22 = [{
    "question": """Welche Informationen werden in der KWIC-Tabelle des Notebooks angezeigt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Nur das Suchwort und seine Häufigkeit",
            "correct": False,
            "feedback": """× Nicht korrekt. Die KWIC-Darstellung zeigt mehr als nur das Suchwort und seine Häufigkeit. Sie stellt jeden einzelnen Treffer in seinem textuellen Kontext dar."""
        },
        {
            "answer": "Das Suchwort, seine Lemmatisierung und seine Wortart",
            "correct": False,
            "feedback": """× Nicht korrekt. Obwohl die Extraktion der Treffer auf Lemmata und Wortarten basiert, zeigt die KWIC-Tabelle selbst primär den textuellen Kontext der Belegstellen, nicht deren linguistische Annotationen."""
        },
        {
            "answer": "Der linke Kontext, das Schlüsselwort und der rechte Kontext sowie zusätzliche Metadaten wie Titel, Autor:in und Erscheinungsjahr",
            "correct": True,
            "feedback": """✓ Richtig! Die von der Funktion `kwic_adj_noun` erzeugte Tabelle enthält die Spalten für den linken Kontext, das Schlüsselwort (das Vorkommen von "Luft") und den rechten Kontext sowie den jeweiligen Modifikator und Metadaten wie Titel, Autor:in, Jahrzehnt und Erscheinungsjahr. Zusätzlich wird der vollständige Satz mitgeführt, falls der enge KWIC-Ausschnitt für die Interpretation nicht ausreicht."""
        },
        {
            "answer": "Eine statistische Zusammenfassung aller Vorkommen des Suchwortes",
            "correct": False,
            "feedback": """× Nicht korrekt. Die KWIC-Darstellung bietet keine statistische Zusammenfassung, sondern zeigt einzelne Vorkommen des Suchausdrucks in ihrem Kontext – im Notebook eine Auswahl von Belegstellen aus den zuvor identifizierten Ausreißertexten."""
        }
    ]
}]

display_quiz(multiple_choice_22, colors=colors.jupyterquiz)
```

## Frage 23

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_23 = [{
    "question": """Welche Funktion erfüllt der Parameter `window` in der Funktion `kwic_adj_noun` des Notebooks?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Er gibt die maximale Anzahl der anzuzeigenden Belegstellen an",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Anzahl der angezeigten Belegstellen wird über den separaten Parameter `max_examples` gesteuert (im Notebook z.B. 25). `window` bezieht sich auf den Umfang des Kontexts pro Belegstelle."""
        },
        {
            "answer": "Er definiert die minimale Häufigkeit, die eine Adjektiv-Nomen-Konstruktion haben muss, um angezeigt zu werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Eine Mindesthäufigkeit spielt bei der KWIC-Anzeige keine Rolle; eine Mindestanzahl (`min_noun_count`) wird nur bei der Ausreißer-Identifikation verwendet, um instabile Extremwerte aus Texten mit sehr wenigen "Luft"-Belegen zu vermeiden. `window` betrifft den Kontextumfang."""
        },
        {
            "answer": "Er bestimmt die Anzahl der Wörter, die links und rechts vom Schlüsselwort als Kontext angezeigt werden",
            "correct": True,
            "feedback": """✓ Richtig! Im Notebook wird `window=7` verwendet: Es werden jeweils 7 Tokens vor und nach dem Vorkommen von "Luft" als linker bzw. rechter Kontext ausgegeben. Reicht dieser enge Ausschnitt für die Interpretation nicht aus, kann ergänzend die mitgelieferte Spalte mit dem vollständigen Satz herangezogen werden."""
        },
        {
            "answer": "Er legt fest, über wie viele Jahre der gleitende Durchschnitt berechnet wird",
            "correct": False,
            "feedback": """× Nicht korrekt. Das Fenster des gleitenden Durchschnitts wird in der Visualisierungsfunktion über den Parameter `window_years` (im Notebook 10 Jahre) gesteuert – das ist ein anderer Analyseschritt. `window` in `kwic_adj_noun` bezieht sich auf Wörter im Textkontext, nicht auf Jahre."""
        }
    ]
}]

display_quiz(multiple_choice_23, colors=colors.jupyterquiz)
```

## Frage 24

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_24 = [{
    "question": """Warum ist die KWIC-Darstellung eine sinnvolle Ergänzung zur quantitativen N-Gramm-Analyse?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie ist schneller durchzuführen als die Frequenzanalyse",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Geschwindigkeit ist kein Vorteil der KWIC-Darstellung gegenüber der Frequenzanalyse. Beide Methoden ergänzen sich in ihren analytischen Möglichkeiten."""
        },
        {
            "answer": "Sie erlaubt es, die Treffer nicht nur zu zählen, sondern ihre konkrete Verwendung im Satz nachzulesen und qualitativ einzuordnen",
            "correct": True,
            "feedback": """✓ Richtig! Genau so wird KWIC im Notebook eingesetzt: Nachdem die Zeitreihen Ausschläge gezeigt haben und die verantwortlichen Ausreißertexte identifiziert wurden, werden deren Belegstellen per KWIC- bzw. Satzkontext qualitativ überprüft. So lässt sich einordnen, welche semantische Funktion Konstruktionen wie "frische Luft" in den jeweiligen Texten tatsächlich haben – und ob ein Ausschlag der Kurve inhaltlich bedeutsam oder eher ein Artefakt weniger Werke ist."""
        },
        {
            "answer": "Sie ist genauer als die Frequenzanalyse",
            "correct": False,
            "feedback": """× Nicht korrekt. Es geht nicht um Genauigkeit, sondern um unterschiedliche Perspektiven: Die Frequenzanalyse liefert quantitative Muster über das ganze Korpus, die KWIC-Darstellung ermöglicht die qualitative Prüfung einzelner Belegstellen. Erst die Kombination beider Zugänge trägt die Interpretation."""
        },
        {
            "answer": "Sie kann ohne vorherige Annotation der Texte durchgeführt werden",
            "correct": False,
            "feedback": """× Nicht korrekt. Unsere KWIC-Funktion `kwic_adj_noun` greift auf die spaCy-Annotationen zurück: Sie findet die Belegstellen über Lemma, POS-Tag und Dependenzlabel und nutzt die Satzsegmentierung für den erweiterten Kontext. Die Annotation ist also Voraussetzung, nicht verzichtbar."""
        }
    ]
}]

display_quiz(multiple_choice_24, colors=colors.jupyterquiz)
```

## Frage 25

Analysieren Sie das folgende Szenario:

Ein Forschungsteam möchte untersuchen, ob die Thematisierung von "Wald" in der deutschsprachigen Literatur des 19. Jahrhunderts zunimmt – etwa als Reaktion auf die fortschreitende Abholzung und Industrialisierung.

1. Beschreiben Sie, wie das Team ein semantisches Feld "Wald" erstellen könnte und worauf dabei zu achten ist.
2. Erläutern Sie, warum für den Vergleich der Texte relative statt absolute Häufigkeiten berechnet werden sollten.
3. Beschreiben Sie, wie die Ergebnisse als Streudiagramm mit Trend-Linie visualisiert und interpretiert werden könnten – und welche Mindestanforderungen an die Datenpunkte gelten.
4. Diskutieren Sie, wie das Team mit einem Zwei-Stichproben-Design die Robustheit seiner Befunde prüfen könnte.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('semantic-field-transfer')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiellösung zur Selbstbewertung:**

**1. Erstellung des semantischen Felds "Wald":**
- Sammlung bedeutungsverwandter Substantive, z.B. "Forst", "Gehölz", "Tann", "Waldung", "Dickicht"
- Wie in der Fallstudie gezeigt, können Large Language Models bei der Generierung von Kandidaten helfen; der Prompt sollte den historischen Sprachgebrauch des 19. Jahrhunderts sowie Eindeutigkeit der Wörter einfordern
- Ergänzend korpusbasiertes Vorgehen: z.B. mit AntConc alle Komposita mit "Wald" als Erstglied extrahieren (analog zu "Stadtluft", "Bergluft" usw.)
- Manuelle Filterung der Liste: mehrdeutige oder zu allgemeine Wörter entfernen, da die Wörter losgelöst vom Kontext gezählt werden und sich möglichst ausschließlich auf den Zielbereich beziehen sollten
- Da die Wörter mit den Lemmata der annotierten Texte verglichen werden, sollten sie in der Grundform vorliegen

**2. Relative statt absolute Häufigkeiten:**
- Literarische Texte sind sehr unterschiedlich lang (von kurzen Erzählungen bis zu langen Romanen)
- Absolute Häufigkeiten würden lange Texte systematisch bevorzugen
- Relative Häufigkeit = absolute Häufigkeit geteilt durch Textlänge (ggf. mal 100, also Treffer pro 100 Tokens) – so wird der Anteil der Waldwörter am Gesamttext vergleichbar
- Beim Zusammenfassen mehrerer Texte (z.B. eines Jahres): Summe der absoluten Häufigkeiten durch Summe der Textlängen teilen, nicht den Durchschnitt der relativen Häufigkeiten bilden, da sonst kurze Texte überproportionalen Einfluss hätten

**3. Visualisierung und Interpretation:**
- Streudiagramm: jeder Text ein Datenpunkt, X-Wert = Publikationsjahr (nur das Jahr liegt als Metadatum vor), Y-Wert = relative Häufigkeit
- Trend-Linie per linearer Regression (Methode der kleinsten Quadrate): eine steigende Gerade zeigt eine Zunahme, eine fallende eine Abnahme, eine waagerechte keinen Zusammenhang
- Für eine generalisierbare Interpretation sollten mindestens 30 Datenpunkte vorliegen, die möglichst gleichmäßig über die Zeit verteilt sind
- Einzelne Ausreißertexte identifizieren und qualitativ (z.B. per KWIC) prüfen – sie könnten inhaltlich wegweisend sein oder den Trend verzerren
- Vorsicht bei der Deutung: Ein steigender Trend belegt noch keine Kausalität (z.B. Abholzung als Ursache)

**4. Zwei-Stichproben-Design:**
- Zwei unabhängige Zufallsstichproben aus demselben Quellkorpus ziehen (unterschiedliche Random States), idealerweise zeitlich balanciert, z.B. gleich viele Texte pro Jahrzehnt
- Alle Analysen parallel auf beiden Stichproben durchführen und die Ergebnisse vergleichen
- Zeigen beide Stichproben dieselben Muster (ähnliche Trend-Linien, ähnliche Ausreißerstruktur), sind die Befunde robust gegenüber der konkreten Zufallsauswahl
- Weichen die Ergebnisse deutlich voneinander ab, hängen sie vermutlich an einzelnen Texten der jeweiligen Stichprobe und sollten nicht generalisiert werden
````


## Frage 26

Stellen Sie sich vor, Sie möchten mit den Methoden dieses Kapitels untersuchen, wie das Substantiv "Wasser" in der deutschsprachigen Literatur des 19. Jahrhunderts semantisiert wird.

1. Erklären Sie, warum sich hierfür syntaktische n-Gramme besser eignen als lineare n-Gramme.
2. Beschreiben Sie, wie die Extraktion der Adjektiv-Substantiv-Paare mit den vorhandenen spaCy-Annotationen technisch funktioniert und welche Anpassung am Notebook-Code dafür nötig wäre.
3. Erläutern Sie, wie Sie auffällige Ausschläge in den Zeitreihen überprüfen würden, bevor Sie sie interpretieren.
4. Beschreiben Sie, wie Sie quantitative und qualitative Analyse kombinieren würden, um zu einer belastbaren Aussage über die Semantisierung von "Wasser" zu kommen.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('syntactic-ngram-transfer')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiellösung zur Selbstbewertung:**

**1. Syntaktische statt lineare n-Gramme:**
- Lineare n-Gramme erfassen nur unmittelbar benachbarte Tokens und zerfallen bei Einschüben: In "das trübe, von Abwässern der Fabriken verschmutzte Wasser" würde das Paar "trübe – Wasser" nicht als Muster erkannt
- Das Deutsche realisiert viele Konstruktionen diskontinuierlich (Partizipialattribute, Verbklammern, flexible Wortstellung), sodass lineare n-Gramme gerade die interpretativ interessanten Muster fragmentieren
- Syntaktische n-Gramme folgen den Relationen im Dependenzbaum: Das Adjektiv ist dort direkt als Attribut des Substantivs analysiert – unabhängig davon, wie viele Wörter auf der Textoberfläche dazwischenstehen
- So werden stabile Beschreibungsweisen auch dann erfasst, wenn die Oberflächenform stark variiert

**2. Technische Umsetzung:**
- Die im Kapitel Korpusverarbeitung erzeugten spaCy-Annotationen (DocBin-Dateien) einlesen und über die Spalte `DC.identifier` mit den Metadaten verknüpfen
- Für jedes Token prüfen: Ist es ein Substantiv (POS-Tag "NOUN") mit dem Lemma "Wasser"? Dann alle syntaktischen Kinder durchgehen und diejenigen zählen, die das Dependenzlabel "nk" und das POS-Tag "ADJ" tragen (die deutschen spaCy-Modelle verwenden "nk" statt "amod")
- Nötige Anpassung im Notebook: lediglich die Variable für das Zielsubstantiv ändern, also `noun = "Wasser"` statt `noun = "Luft"` – die Funktion `extract_dependent_adjective_list` akzeptiert auch Listen mehrerer Substantive, z.B. `noun = ["Wasser", "Fluss", "Strom"]`
- Ergebnis: pro Text die Häufigkeit jedes beobachteten Adjektivs (`count`) sowie die Gesamtzahl der "Wasser"-Vorkommen (`noun_count`), aus denen sich die relative Häufigkeit `rel_freq = (count / noun_count) * 100` berechnen lässt

**3. Überprüfung auffälliger Ausschläge:**
- Zunächst prüfen, ob ein Ausschlag von wenigen Texten getragen wird: pro Text die normalisierte Kennzahl `rel_freq` berechnen, Peak-Dekaden bestimmen und die Texte mit den höchsten Werten (Top-k) als Ausreißertexte auflisten
- Texte mit sehr wenigen Belegen des Zielsubstantivs herausfiltern (z.B. `noun_count < 5`), um instabile Extremwerte zu vermeiden
- Den Anteil einzelner Texte an allen Treffern einer Dekade berechnen, um sichtbar zu machen, ob ein einzelnes Werk den Ausschlag dominiert
- Die Belegstellen der Ausreißertexte per KWIC-Ansicht (Kontextfenster, z.B. `window=7`) und ggf. ganzem Satzkontext lesen und semantisch einordnen

**4. Kombination quantitativer und qualitativer Analyse:**
- Quantitativ: korpusweite Rangliste der Adjektive (Balkendiagramm/Tabelle), diachrone Verläufe mit gleitendem Durchschnitt (z.B. 10-Jahres-Fenster), parallel auf zwei Stichproben zur Robustheitsprüfung
- Qualitativ: KWIC-Lektüre ausgewählter Belegstellen, um zu prüfen, ob die Adjektive tatsächlich im vermuteten Sinn verwendet werden (z.B. "trübes Wasser" wörtlich oder metaphorisch)
- Interpretation nur auf Muster stützen, die in beiden Stichproben auftreten und sich in der qualitativen Prüfung bestätigen
- Grenzen der Operationalisierung reflektieren: Adjektiv-Substantiv-Paare erfassen nur einen Ausschnitt der Semantisierung; subtilere Formen (Metaphern, Handlungskontexte) bleiben unsichtbar
````
