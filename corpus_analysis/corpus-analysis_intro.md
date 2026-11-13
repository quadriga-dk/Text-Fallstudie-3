(corpus-analysis_intro)=
# Korpusanalyse. Semantische Felder und syntaktische N-Gramme 
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
:start-after: "<!-- START: Korpusanalyse. Semantische Felder und syntaktische N-Gramme -->"
:end-before: "<!-- END: Korpusanalyse. Semantische Felder und syntaktische N-Gramme -->"
```

Nachdem wir im vorherigen Kapitel das Vorgehen der automatischen linguistischen Annotation vorgestellt und unsere beiden Korpora literarischer Texte damit annotiert haben (siehe Kapitel [Korpusverarbeitung – Von Strings zu Token](corpus-processing_intro)), sind alle Vorverarbeitungsschritte durchgeführt und wir wenden uns in diesem Kapitel der Korpusanalyse zu.

Bei diesen beiden Korpora handelt es sich um die zwei Zufallsstichproben, die wir im Abschnitt [Sampling und Filterung des Korpus](../corpus_collection/corpus-collection_filtering-our-corpus.ipynb) gezogen und dort als **Korpus I** (Random State `42`) und **Korpus II** (Random State `31415`) benannt haben. Beide Korpora sind also zwei unabhängig gezogene Stichproben aus demselben Quellkorpus – dem auf das 19. Jahrhundert eingegrenzten *Corpus of German-Language Fiction*. Annotiert und analysiert haben wir demnach nicht das vollständige Ausgangskorpus, sondern diese beiden Stichproben (zusammen 724 verschiedene Texte). Sämtliche folgenden Analysen führen wir auf **beiden Korpora parallel** durch und vergleichen die Ergebnisse miteinander – so lässt sich einschätzen, welche Muster robust sind und welche stärker von der konkreten Zufallsauswahl abhängen.


```{figure} ../assets/images/flow-chart_corpus-analysis.png
---
height:
name: Flussdiagramm der Fallstudie
---
Flussdiagramm der Fallstudie, das aktuelle Arbeitspaket ist hervorgehoben.
```
Wir kehren zur Forschungsfrage zurück und besprechen zuerst [konzeptionelle Grundlagen](corpus-analysis_analysis) zur Erstellung eines semantischen Felds, zur Extraktion von Häufigkeiten sowie zur Visualisierung der Häufigkeiten in Form eines Streudiagramms und die Errechnung und Darstellung einer Trend-Linie. 

Anschließend wird die [Analyse des semantischen Felds auf den Korpora ausgeführt](corpus-analysis_semantic-field-analysis) und die Ergebnisse werden anhand der Visualisierungen interpretiert. 

Im nächsten Schritt werden [n-Gramme im Allgemeinen](corpus-analysis_ngrams-intro.md) und dann [syntaktische n-Gramme](corpus-analysis_syntactic-ngrams-intro.md) eingeführt. Daraufhin wird die [Korpusanalyse](corpus-analysis_syntactic-ngram.ipynb) ausgeführt und die Ergebnisse werden wieder anhand von Visualisierungen interpretiert.
