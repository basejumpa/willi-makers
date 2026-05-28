void setup(){
    pinMode(2, OUTPUT);
    Serial.begin(9600);
}

int licht = 0;
void loop() {
    licht = analogRead(A0);

    if(licht <= 195){
        digitalWrite(2, HIGH);
    }else{
        digitalWrite(2, LOW);
}

Serial.println(licht);
}
