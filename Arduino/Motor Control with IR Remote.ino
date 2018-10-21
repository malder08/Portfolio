#include <IRremote.h>

#define on_key 0xFF807F
#define off_key 0xFFA05F

int receiver_pin = 8;
int in1 = 7;
int in2 = 6;
int enA = 10;

IRrecv receiver(receiver_pin);
decode_results output;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  receiver.enableIRIn();
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enA, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (receiver.decode(&output)){
      unsigned int value = output.value;
        switch(value){
          case on_key: //Keypad button "ON"
          digitalWrite(in1, HIGH);
          digitalWrite(in2, LOW);
          analogWrite(enA, 255);
          }

        switch(value){
          case off_key: //Keypad button "OFF"
          digitalWrite(in1, LOW);
          digitalWrite(in2, HIGH);
          analogWrite(enA, 255);
          }

        receiver.resume();
  }
}
