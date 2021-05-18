# TBD-Natalia

Ich habe "Irony Detection" als Aufgabe gewählt und benutze folgende Daten dafür: Ironic Corpus, https://www.kaggle.com/rtatman/ironic-corpus.

Die 2 Klassen für die Klassifizierung sind: ironisch vs. nicht ironisch, die durch Label "1" oder "-1" abgebildet sind. 

In meinem Repository gibt es jetzt folgende relevanten Files zum Projekt: 
1. abstract_feature_class.py
2. feature_class_punctuation.py
3. word_based_features.py
4. preprocess.py
5. split_data.py
6. get_features.py

Hier ist noch eine Instruktion zum File split_data.py

Man muss zuerst noch einen File "preprocess" haben, der dann die Daten zuerst einliest, verarbeitet und aufräumt. Dann muss man das Skript "split_data.py" so verändern, dass die Variable "DATAPATH" den aktuellen Pfad zu den Daten enthält. Dann ruft man einfach das Skript auf. 

Vorverarbeitung von Daten in preprocess.py:

Ich habe die Namen der Spalten geändert. Jetzt gibt es in dem DataFrame 3 Spalten: ID, Text und Label. 
Dann habe ich doppelte und leere Texte entfernt und das neue DataFrame zurückgegeben. 
