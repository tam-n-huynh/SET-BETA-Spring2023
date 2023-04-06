#include <Servo.h>

Servo servo;
int angle = 0;

void setup() {
  Serial.begin(9600);
  servo.attach(9); // Set the servo pin to 9
}

void loop() {
  if (Serial.available() > 0) {
    angle = Serial.parseInt();
    servo.write(angle);
  }
}