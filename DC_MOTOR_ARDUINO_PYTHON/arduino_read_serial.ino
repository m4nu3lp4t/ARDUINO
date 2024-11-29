#define E1 5 // Enable Pin for motor
#define I1 3 // Control pin 1 for motor 
#define I2 4 // Control pin 2 for motor 
#define LED 13 // Control pin 2 for motor 

char myData[30] = { 0 };

void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
  pinMode(E1, OUTPUT);
  pinMode(I1, OUTPUT);
  pinMode(I2, OUTPUT);
}

void loop() {
  byte n = Serial.available();
  if (n != 0) {
    byte m = Serial.readBytesUntil('\n', myData, 30);
    myData[m] = '\0';  //null-byte
    int y1, y2, y3, y4;
    if (sscanf(myData, "%d,%d,%d,%d", &y1, &y2, &y3, &y4) == 4) {
      Serial.println("parsed four ints ok");
      Serial.print("int y1 = ");
      Serial.println(y1);
      Serial.print("int y2 = ");
      Serial.println(y2);
      Serial.print("int y3 = ");
      Serial.println(y3);
      Serial.print("int y4 = ");
      Serial.println(y4);
    } else Serial.println("error in input!");

if (y1 == 1) {
  digitalWrite(LED, HIGH);
  analogWrite(E1, y2);        //  speed
  digitalWrite(I1, y3);
  digitalWrite(I2, y4);

}
if (y1 == 0) {
  digitalWrite(LED, y1);
  digitalWrite(E1, y1);
}


  }
}
//"125,67,-45"