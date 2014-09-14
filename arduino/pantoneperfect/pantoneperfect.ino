#include <Adafruit_NeoPixel.h>

/*
   WHAT DOES THIS PROGRAM DO?
   
   Author: Evan Gillespie
*/

int neopixel_pin = 6;

int num_neopixels = 60;
Adafruit_NeoPixel led_strip = Adafruit_NeoPixel(num_neopixels, neopixel_pin);

void setup(){
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  
  led_strip.begin();
  led_strip.show();
}

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
    
  }
  delay(500);
}

void light_strip(int red, int green, int blue) {
  // TODO: validation
  for (int i = 0; i < 10; i++) {
    led_strip.setPixelColor(i, led_strip.Color(green, red, blue));
  }
  led_strip.show();
}
