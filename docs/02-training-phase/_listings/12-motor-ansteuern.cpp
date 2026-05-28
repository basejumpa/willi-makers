
// Definiere Pin-Verbindungen
const int ENA = 9; // Enable-Pin fUEr Motor A (PWM)
const int IN1 = 8; // Steuer-Pin 1 fUEr Motor A
const int IN2 = 7; // Steuer-Pin 2 fUEr Motor A

// Definiere Konstanten fUEr die Motordrehrichtung
const int VORWAERTS = 1;
const int RUECKWAERTS = -1;
const int STOPP = 0;

void setup() {
    // Setze alle Motorsteuerungs-Pins auf Ausgang
    pinMode(ENA, OUTPUT);
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
}

void loop() {
    // Drehe den Motor im Uhrzeigersinn mit halber Geschwindigkeit
    setMotor(VORWAERTS, 128); // Richtung VORWAERTS, Geschwindigkeit 128 von 255
    delay(2000);             // Laufen fUEr 2 Sekunden

    // Stoppe den Motor
    setMotor(STOPP, 0);
    delay(1000);             // Stoppe fUEr 1 Sekunde

    // Drehe den Motor gegen den Uhrzeigersinn mit viertel Geschwindigkeit
    setMotor(RUECKWAERTS, 64); // Richtung RUECKWAERTS, Geschwindigkeit 64 von 255
    delay(2000);             // Laufen fUEr 2 Sekunden

    // Stoppe den Motor
    setMotor(STOPP, 0);
    delay(1000);             // Stoppe fUEr 1 Sekunde

    // Drehe den Motor im Uhrzeigersinn mit voller Geschwindigkeit
    setMotor(VORWAERTS, 255); // Richtung VORWAERTS, Geschwindigkeit 255 von 255
    delay(2000);             // Laufen fUEr 2 Sekunden

    // Stoppe den Motor
    setMotor(STOPP, 0);
    delay(1000);             // Stoppe fUEr 1 Sekunde
}

// Funktion zur Einstellung der Motordrehrichtung und -geschwindigkeit
void setMotor(int richtung, int geschwindigkeit) {
    if (richtung == VORWAERTS) {
        digitalWrite(IN2, LOW);
        digitalWrite(IN1, HIGH);
    } else if (richtung == RUECKWAERTS) {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
    } else { // STOPP oder anderer Wert
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
    }
    analogWrite(ENA, geschwindigkeit);
}
