
// Pin Definitionen
const int sensorPin = A0;  // Pin, an dem der Feuchtigkeitssensor angeschlossen ist
const int greenLedPin = 2; // Pin, an dem die grüne LED angeschlossen ist
const int redLedPin = 3;   // Pin, an dem die rote LED angeschlossen ist

// Grenzwerte für die Hysterese
const int thresholdHigh = 550; // Oberer Grenzwert für Feuchtigkeit
const int thresholdLow = 450;  // Unterer Grenzwert für Feuchtigkeit

// Variablen zur Steuerung der LED-Zustände
bool isDry = false;

void setup()
{
    // Setze die LED Pins als Ausgang
    pinMode(greenLedPin, OUTPUT);
    pinMode(redLedPin, OUTPUT);

    // Initialisiere die serielle Kommunikation
    Serial.begin(9600);
}

void loop()
{
    // Lese den Wert des Feuchtigkeitssensors
    int sensorValue = analogRead(sensorPin);

    // Gebe den Sensorwert auf der seriellen Schnittstelle aus
    Serial.print("Feuchtigkeitswert: ");
    Serial.println(sensorValue);

    // Überprüfe den Feuchtigkeitswert mit Hysterese
    if (isDry)
    {
        // Wenn es trocken ist und der Wert über den unteren Grenzwert steigt
        if (sensorValue < thresholdLow)
        {
            isDry = false;
        }
    }
    else
    {
        // Wenn es feucht ist und der Wert unter den oberen Grenzwert fällt
        if (sensorValue > thresholdHigh)
        {
            isDry = true;
        }
    }

    // Steuere die LEDs basierend auf dem isDry Zustand
    if (isDry)
    {
        digitalWrite(greenLedPin, LOW);
        digitalWrite(redLedPin, HIGH);
    }
    else
    {
        digitalWrite(greenLedPin, HIGH);
        digitalWrite(redLedPin, LOW);
    }

    // Kurze Pause, um die Werte nicht zu oft zu lesen
    delay(500);
}
