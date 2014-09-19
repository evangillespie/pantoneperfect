#include <Adafruit_NeoPixel.h>

/*
   WHAT DOES THIS PROGRAM DO?
   
   Author: Evan Gillespie
*/

int neopixel_pin = 6;

int num_neopixels = 60;
Adafruit_NeoPixel led_strip = Adafruit_NeoPixel(num_neopixels, neopixel_pin);

void setup(){
  Serial.begin(9600);
  pinMode(13, HIGH);
  digitalWrite(13, LOW);
  
  led_strip.begin();
  led_strip.show();
}

int state = 0;
unsigned long timer = 0;
void loop(){
  if (Serial.available() >= 3)  {
    // expect communications in the form: RRRGGGBBB
    int red;
    int green;
    int blue;
    
    red = Serial.read();
    green = Serial.read();
    blue = Serial.read();
    
    Serial.write(255); // send confirmation message back
    
    light_strip(red, green, blue);
    
    digitalWrite(13, !digitalRead(13));
  }
  else if (Serial.available() > 0){
    if ( timer == 0 ){
      timer = millis();
    }

    if ( ( millis() - timer ) > 10*1000 ) {
      // clear the read buffer
      timer = 0;
      while( Serial.available() > 0 ) {
        Serial.read();
      }
    }
  }
  delay(50);
  
}

void light_strip(int red, int green, int blue) {
  // TODO: validation
  for (int i = 0; i < led_strip.numPixels(); i++) {
    led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
  }
  led_strip.show();
}
