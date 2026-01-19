(corpus-processing_intro)=
# Korpusverarbeitung. Von Strings zu Token

````{margin}
```{admonition} Fragen oder Feedback 
:class: frage-feedback

<a href="https://github.com/quadriga-dk/Text-Fallstudie-3/issues/new?assignees=&labels=question&projects=&template=frage.yml" class="external-link" target="_blank">
    Stellen Sie eine Frage
</a> <br>
<a href="https://github.com/quadriga-dk/Text-Fallstudie-3/issues/new?assignees=&labels=feedback&projects=&template=feedback.yml" class="external-link" target="_blank">
    Geben Sie uns Feedback
</a>

Mit Ihren Rückmeldungen können wir unser interaktives Lehrbuch gezielt an Ihre Bedürfnisse anpassen.

```
````
```{admonition} Korpusverarbeitung mit Natural Language Processing
:class: lernziele
1. Die Grundkonzepte des Natural Language Processing können erklärt und die Funktionen von Tokenisierung, Lemmatisierung, POS-Tagging und Dependency Parsing für die Textanalyse beschrieben werden.

2. Die notwendigen Schritte zur automatischen Annotation eines Texts können aufgezählt und Vorteile der Tokenisierung gegenüber einfacheren Methoden der Worttrennung genannt werden.
```

Für die Ausführung einer digitalen Analyse, in diesem Fall die Analyse von Worthäufigkeiten und Kollokationen über Zeit, wird ein über die Zeit gestreutes Korpus benötigt, das im txt-Format (oder einem anderen, computerlesbaren Format) vorliegt. Bevor die Analyse auf dem Korpus ausgeführt werden kann, muss das Korpus mit linguistischen Informationen angereichert werden, etwa um Wörter einer bestimmten Wortart, in diesem Fall Adjektiv-Nomen-Paare, zu identifizieren.  


```{figure} ../assets/images/flow-chart_corpus-processing.png
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie, das aktuelle Arbeitspaket ist hevorgehoben.
```

In diesem Kapitel wird konzeptionell in die Methoden der Anreicherung eingeführt (Tokenisierung, Lemmatisierung und POS-Tagging), dann wird kurz darauf eingegangen, welche Möglichkeiten es in Python für die Anreicherung gibt. Im nächsten Schritt wird gezeigt, wie das Korpus mit Hilfe von `spaCy` annotiert werden kann. Zum Schluss wird ein Resümee gezogen.
