4. Übung: Schalter einlesen
###########################

Wir stecken die auf dem folgenden Bild gezeigte Schaltung. Während der Schalter gedrückt ist, verbindet er Pin D2 mit GNG (Ground). Während der Schalter nicht gedrückt ist, ist der D2 offen.

.. figure:: _figures/04-schalter-einlesen.png

Folgendes Programm tippen wir ein und laden es auf den Arduino.

.. literalinclude:: _listings/04-schalter-einlesen.cpp
    :language: cpp
    :linenos:

Wir schauen uns auf dem seriellen Monitor und auch auf dem seriellen Plotter an was passiert, wenn wir mit dem Schalter spielen. Wir sehen eine 1 während der Schalter unbetätigt ist; während wir ihn gedrückt halten sehen wir eine 0.

Wir modifizieren das Program, indem wir ein Ausrufezeichen zwischen die öffnende Klammer und das digitalRead einsetzen.

Nach Hochladen des Programmes ist es mit Zahlen und Betätigen umgekehrt.

