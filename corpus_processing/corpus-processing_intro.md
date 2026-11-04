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

Dieses Kapitel verfolgt die folgenden Lernziele:

```{include} ../introduction/introduction_learning-outcomes.md
:start-after: "<!-- START: Korpusverarbeitung. Von Strings zu Token -->"
:end-before: "<!-- END: Korpusverarbeitung. Von Strings zu Token -->"
```

Um eine digitale Analyse auszuführen, in diesem Fall die Analyse von Worthäufigkeiten und Kollokationen über Zeit, wird ein über die Zeit gestreutes Korpus benötigt, das im txt-Format (oder einem anderen, computerlesbaren Format) vorliegt. Bevor die Analyse auf dem Korpus ausgeführt werden kann, muss das Korpus mit linguistischen Informationen angereichert werden, etwa um Wörter einer bestimmten Wortart, in diesem Fall Adjektiv-Nomen-Paare, zu identifizieren.  


```{figure} ../assets/images/flow-chart_corpus-processing.png
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie, das aktuelle Arbeitspaket ist hervorgehoben.
```

In diesem Kapitel wird konzeptionell in die Methoden der Anreicherung eingeführt (Tokenisierung, Lemmatisierung und POS-Tagging). Dann wird kurz darauf eingegangen, welche Möglichkeiten die Programmiersprache Python für die Anreicherung bietet. Im nächsten Schritt wird gezeigt, wie das Korpus mit Hilfe der Python-Bibliothek `spaCy` annotiert werden kann. Zum Schluss wird ein Resümee gezogen.
