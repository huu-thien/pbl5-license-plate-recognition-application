#include <cvzone.h>
#include <Servo.h>
int servo = 9;
int goc=0 ;
const int trigPin = 10;
const int echoPin = 9;
unsigned long duration;
int distance;
Servo myServo;

SerialData serialData(1,1); //(numOfValsRec,digitsPerValRec)
/*0 or 1 - 1 digit
0 to 99 -  2 digits 
0 to 999 - 3 digits 
 */
int valsRec[1];


void setup() {
  serialData.begin();
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myServo.attach(servo);
  // put your setup code here, to run once:

}

void loop() {
  // digitalWrite(trigPin, LOW);
  // delayMicroseconds(2);
  // digitalWrite(trigPin, HIGH);
  // delayMicroseconds(10);
  // digitalWrite(trigPin, LOW);
  // duration = pulseIn(echoPin, HIGH);
  // distance = duration * 0.034 / 2;

  //myServo.write(goc);
  serialData.Get(valsRec);
  // put your main code here, to run repeatedly:
  if (valsRec[0] ==1){
    goc = 90;
    myServo.write(goc);
  }
  else  {
    // if(distance >20) {
       goc =0;
       myServo.write(goc);
    // }
  }
  delay(20);
}
