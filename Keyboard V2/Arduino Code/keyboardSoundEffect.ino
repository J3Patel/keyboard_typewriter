#include <AccelStepper.h>
//#include "Keyboard.h"
int currentRandm = 0;
AccelStepper stepper(1, 9, 10);
char dataString[1] = {'5'};
boolean iseofnot = false;
boolean onlyonce = false;
void setup() {
  // open the serial port:
  Serial.begin(9600);
    pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(13, OUTPUT);
  
  digitalWrite(2, HIGH); 
  digitalWrite(3, HIGH); 
  digitalWrite(4, HIGH); 
  digitalWrite(5, HIGH); 
  digitalWrite(6, HIGH); 
  digitalWrite(7, HIGH); 
  digitalWrite(8, HIGH); 
  digitalWrite(13, LOW); 

  pinMode(12, INPUT);
  pinMode(11, INPUT);
//  sprintf(dataString,"%02X","5"); // convert a value to hexa 
  stepper.setMaxSpeed(10000);//1100
  stepper.setAcceleration(11000);
  stepper.moveTo(0);
  stepper.setPinsInverted(true);
}

void loop() {
  
  bool gear = digitalRead(11);
  bool senseifReady = digitalRead(12);

// stepper.currentPosition() > 800 && 
  if (stepper.currentPosition() > 700 && senseifReady == true && !iseofnot) {
    stepper.setCurrentPosition(0);
    Serial.println("5");
    iseofnot = true;
    onlyonce = false;
//    Serial.println("sensei check");
//    Serial.write("5");
  }

  if (senseifReady == false) {
    iseofnot = false;
    
  }

    digitalWrite(13, gear); 
  
  // check for incoming serial data:
  if (Serial.available() > 0) {
    // read incoming serial data:
    char inChar = Serial.read();
    
    if (stepper.currentPosition() > 700 ) {
      if(!onlyonce){
        onlyonce = true;
        digitalWrite(8, LOW); 
        delay(40);
        digitalWrite(8, HIGH);
      }
         
        return;
    }
    if(inChar == '2') {
//        Serial.println("in if");
        digitalWrite(8, LOW); 
        delay(40);
        stepper.moveTo(stepper.currentPosition() + 10);
        stepper.runToPosition();
        digitalWrite(8, HIGH); 
    } else {
//      Serial.println("else");
      currentRandm = random(2,8);
        
        digitalWrite(currentRandm, LOW); 
        delay(40);
         stepper.moveTo(stepper.currentPosition() + 10);
        stepper.runToPosition();
        digitalWrite(currentRandm, HIGH); 
     
    }

//    Serial.println(stepper.currentPosition());
    // Type the next ASCII value from what you received:
//    Keyboard.write(inChar + 1);
  }
}
