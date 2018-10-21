#include <IRremote.h>

#define on_key 0xFF807F
#define off_key 0xFFA05F
int receiver_pin = 7;

int motor = 3;
IRrecv receiver(receiver_pin);
decode_results output;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  receiver.enableIRIn();
  pinMode(motor, OUTPUT);
}

  // put your main code here, to run repeatedly:
  void loop(){
    if (receiver.decode(&output)){
      unsigned int value = output.value;
        switch(value){
          case on_key: //Keypad button "ON"
          analogWrite(motor, 255);
          }

        switch(value){
          case off_key: //Keypad button "OFF"
          analogWrite(motor, 0);
          }

        receiver.resume(); 
    }
}

