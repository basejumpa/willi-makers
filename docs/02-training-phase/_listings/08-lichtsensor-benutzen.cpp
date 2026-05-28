void setup(){
    Serial.begin(9600);
}

int licht = 0;
void loop() {
    licht = analogRead(A0);
    Serial.println(licht);
}
