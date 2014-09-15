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
void loop(){
  if (Serial.available())  {
    // expect communications in the form: RRRGGGBBB
    char red[] = "000";
    char green[] = "000";
    char blue[] = "000";
    
    Serial.readBytes(red, 3);
    Serial.readBytes(green, 3);
    Serial.readBytes(blue, 3);
    
    light_strip(atoi(red), atoi(green), atoi(blue));
    
     if ( state == 0 ){
       state = 1;
       digitalWrite(13, HIGH);
     }
     else {
       state = 0;
       digitalWrite(13, LOW);
     }
  }
  delay(500);
  
//  light_strip(255, 0, 0);
//  delay(5000);
//  light_strip(0, 255, 0);
//  delay(5000);
//  light_strip(0, 0, 255);
//  delay(5000);
  
}

void light_strip(int red, int green, int blue) {
  // TODO: validation
  for (int i = 0; i < led_strip.numPixels(); i++) {
    led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
  }
  led_strip.show();
}
