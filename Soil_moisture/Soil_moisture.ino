int sensorPin = A0; 
int sensorValue;  
int limit = 300; 

void setup() {
 Serial.begin(9600);
 //pinMode(13, OUTPUT);
}

void loop() {

 sensorValue = analogRead(sensorPin); 
 Serial.println("Analog Value : ");
 Serial.println(sensorValue);
 if (sensorValue<limit) {
 digitalWrite(LED_BUILTIN,HIGH);
 //digitalWrite(13, HIGH); 
 }
 else {
 digitalWrite(LED_BUILTIN,LOW);
 //digitalWrite(13, LOW); 
 }
 
 delay(1000); 
}
