const int PIN_SENSOR_LINKS  = A0;
const int PIN_SENSOR_RECHTS = A1;

const int PIN_MOTOR_LINKS = 6;
const int PIN_MOTOR_RECHTS = 5;

int helligkeit_links;
int helligkeit_rechts;

String untergrund_links = "Unbekannt";
String untergrund_rechts = "Unbekannt";

String untergrund_neu(String untergrund_alt, int helligkeit) {
  if(helligkeit > 910)
    return "SCHWARZ";
  else if (helligkeit < 880)
    return "WEISS";
  else
    return untergrund_alt;
}

String ort = "ende";

String ort_neu(String ort_alt, String untergrund_links, String untergrund_rechts){
  if (untergrund_rechts == "SCHWARZ" && untergrund_links == "SCHWARZ")
    return "ende";
  else if (untergrund_rechts == "SCHWARZ")
      return "links";
  else if (untergrund_links == "SCHWARZ")
      return "rechts";
  else
      return ort_alt;
}

const int GESCHWINDIGKEIT_NORMAL = 150;
const int GESCHWINDIGKEIT_UNTERSCHIED = 30;

void fahre(String ort){
  if (ort == "ende") {
    analogWrite(PIN_MOTOR_LINKS, 0);
    analogWrite(PIN_MOTOR_RECHTS, 0);
  } else if (ort == "links"){
    analogWrite(PIN_MOTOR_LINKS, GESCHWINDIGKEIT_NORMAL + GESCHWINDIGKEIT_UNTERSCHIED);
    analogWrite(PIN_MOTOR_RECHTS, GESCHWINDIGKEIT_NORMAL - GESCHWINDIGKEIT_UNTERSCHIED);
  } else if (ort == "rechts") {
    analogWrite(PIN_MOTOR_LINKS, GESCHWINDIGKEIT_NORMAL - GESCHWINDIGKEIT_UNTERSCHIED);
    analogWrite(PIN_MOTOR_RECHTS, GESCHWINDIGKEIT_NORMAL + GESCHWINDIGKEIT_UNTERSCHIED);
  } else {
    analogWrite(PIN_MOTOR_LINKS, GESCHWINDIGKEIT_NORMAL);
    analogWrite(PIN_MOTOR_RECHTS, GESCHWINDIGKEIT_NORMAL);
  }
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  helligkeit_links = analogRead(PIN_SENSOR_LINKS);
  helligkeit_rechts = analogRead(PIN_SENSOR_RECHTS);

  Serial.print(helligkeit_links);
  Serial.print(" ");
  Serial.println(helligkeit_rechts);

  untergrund_links = untergrund_neu(untergrund_links, helligkeit_links);
  untergrund_rechts = untergrund_neu(untergrund_rechts, helligkeit_rechts);

  Serial.print(untergrund_links);
  Serial.print(" ");
  Serial.println(untergrund_rechts);

  ort = ort_neu(ort, untergrund_links, untergrund_rechts);

  Serial.println(ort);
  Serial.println();

  fahre(ort);

  delay(100);


}

