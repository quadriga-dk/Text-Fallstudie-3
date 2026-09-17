(introduction_requirements)=
# Technische Voraussetzungen

Die Fallstudie umfasst erklärende Texte, ausführbaren Code und Übungen zur Selbstüberprüfung. Der Code liegt in "<a href="https://jupyterbook.org/"  class="external-link" target="_blank">Jupyter Notebooks</a>" vor und kann einerseits hier im "Jupyter Book" gelesen, andererseits mit dem Dienst "Colab" oder lokal auf dem eigenen Computer ausgeführt werden. Diese drei Nutzungsszenarien nennen wir Nutzungs-Modi. 

```{admonition} "Jupyter Book" und "Jupyter Notebook" – was ist der Unterschied?
:class: keypoint
- Ein **"Jupyter Notebook"** ist eine interaktive Seite, die erklärenden Text mit ausführbarem Code und dessen Ergebnissen (z.B. Tabellen oder Grafiken) verbindet – zum Beispiel die Seite [„Korpusverarbeitung – Annotation mit spaCy"](../corpus_processing/corpus-processing_nlp-annotation.ipynb). Solche Notebook-Seiten erkennen Sie in der Menüleiste links an der Rakete (🚀) im Titel.
- Ein **"Jupyter Book"** bündelt alle Notebook-Seiten mit den reinen Textseiten zu einer zusammenhängenden, im Browser lesbaren Website – einer Art Online-Buch. Diese gesamte Fallstudie mit all ihren Kapiteln und Unterkapiteln, die Sie gerade lesen, *ist* ein solches "Jupyter Book".
```

## Modi der Nutzung
- Im **"Book-Only Mode"** lesen Sie in Ihrem Internet-Browser unser "Jupyter Book" und haben eingeschränkte Möglichkeiten, etwa mit Visualisierungen zu interagieren. Sie können den Code und seine bereits erzeugten Ausgaben zwar sehen, ihn aber nicht selbst ausführen. Dieser Modus erfordert keine Programmierkenntnisse und keine Erfahrungen im Umgang mit der interaktiven Programmierumgebung "Jupyter Notebook".
- Im **"Cloud Mode"** können Sie darüber hinaus die in diesem "Jupyter Book" enthaltenen "Jupyter Notebooks" über den webbasierten Dienst "Colab" von Google aktiv ausführen, den Code verändern und ggf. auch für eigene Forschungsfragen adaptieren. Unterkapitel dieser Fallstudie, die in Form von "Jupyter Notebooks" vorliegen und die Sie entsprechend im "Cloud Mode" ausführen können, weisen oben rechts eine Rakete auf. Klicken Sie auf die Rakete und öffnen Sie das "Jupyter Notebook" auf "Colab". Um ein "Jupyter Notebook" in Colab auszuführen, benötigen Sie einen Google-Account. Wenn Sie bei ihrem Account eine institutionelle E-Mail-Adresse angegeben haben, kann es zu Problemen beim Login kommen. Sie müssen dann ein neues Browser-Fenster öffnen und auf einen privaten Google-Account wechseln. 
- Im **"Local Mode"** laden Sie das "Jupyter Notebook" auf Ihren eigenen Computer und führen es dort in einer entsprechenden Umgebung aus (z.B. im <a href="https://www.anaconda.com/products/navigator" class="external-link" target="_blank">"Anaconda Navigator"</a>). Hier haben Sie ebenfalls die Möglichkeit, den Code aktiv auszuführen, ihn zu verändern und ggf. auch für eigene Forschungsfragen zu adaptieren. Dabei können Sie auch Daten nutzen, die Sie lokal auf Ihrem Computer vorhalten.

```{admonition} Wie führe ich den Code in einem "Jupyter Notebook" aus?
:class: tip
Der Code eines "Jupyter Notebooks" ist in einzelne **Code-Zellen** unterteilt, die Sie nacheinander von oben nach unten ausführen. Eine einzelne Zelle starten Sie, indem Sie links neben der Zelle auf das dreieckige **„Play"-Symbol** (▶) klicken. In "Colab" wird dieses Symbol erst sichtbar, wenn Sie die Maus über die Zelle bewegen (oder die Zelle anklicken). Alternativ führen Sie die gerade ausgewählte Zelle mit der Tastenkombination **Umschalt + Eingabe** (`Shift` + `Enter`) aus.
```

Weitere Hinweise zur Arbeit mit "Jupyter Book", "Jupyter Notebooks" und zur Installation von Anaconda für die Nutzung im "Local Mode" vermitteln die unten verlinkten Tutorials.

## Ressourcen
Die Fallstudie lässt sich vollständig in jedem gängigen Browser auf einem einfachen Computer oder Tablet (zur Not auch auf einem Smartphone) durcharbeiten. Dies gilt auch für das Ausführen der "Jupyter Notebooks" mittels "Colab". Für das lokale Ausführen der "Jupyter Notebooks" auf dem eigenen Computer reicht ein handelsüblicher Laptop bereits aus. Sofern das gesamte Forschungsprojekt der Fallstudie auf dem eigenen Computer reproduziert oder die Pipeline (die Abfolge der einzelnen Verarbeitungsschritte) für ein eigenes Korpus adaptiert werden soll, empfehlen wir einen aktuellen und möglichst ressourcenstarken Computer, um die Rechenzeiten so gering wie möglich zu halten.

`````{admonition} Tutorials
:class: seealso
- <a href="https://digital-history-berlin.github.io/Python-fuer-Historiker-innen/ch00-preface/04-nutzung.html" class="external-link" target="_blank">Tutorial zur Arbeit mit Jupyter Books</a>
- <a href="https://www.elab2go.de/demo-py1/jupyter-notebooks.php#1WasisteinJupyterNotebook" class="external-link" target="_blank">Tutorial zur Arbeit mit Jupyter Notebooks</a> 
- <a href="https://www.elab2go.de/demo-py1/installation-python-anaconda.php" class="external-link" target="_blank">Tutorial zur Installation und Nutzung von Anaconda</a>
`````
