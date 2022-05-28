void setup() {
Serial.begin(9600);
}
int x = 0;
void loop() {
Serial.println(x++);
delay(1000);
}
