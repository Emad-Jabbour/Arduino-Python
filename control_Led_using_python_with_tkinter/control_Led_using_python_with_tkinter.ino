
void setup() {
Serial.begin(9600);
pinMode(13,1);
}

void loop() {

if(Serial.available() > 0){
String s = Serial.readStringUntil('\n');
Serial.println(s);
if (s == "on"){
  digitalWrite(13,1);
}else if (s == "off"){
  digitalWrite(13,0);
}
  
}
}
