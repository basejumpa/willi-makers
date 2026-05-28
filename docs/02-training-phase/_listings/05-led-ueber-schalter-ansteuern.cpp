void setup(){
    pinMode(2, INPUT_PULLUP);
    pinMode(3, OUTPUT);
}

void loop() {
    int schalter = digitalRead(2);
    digitalWrite(3, schalter);
}
