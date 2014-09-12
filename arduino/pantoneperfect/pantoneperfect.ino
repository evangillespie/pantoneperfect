#include <Adafruit_NeoPixel.h>

/*
   WHAT DOES THIS PROGRAM DO?
   
   Author: Evan Gillespie
*/

int neopixel_pin = 6;

int num_neopixels = 120;
Adafruit_NeoPixel led_strip = Adafruit_NeoPixel(num_neopixels, neopixel_pin);

void setup(){
  led_strip.begin();
  led_strip.show();
}

void loop(){
  for (int i=0; i < num_neopixels; i++){
    led_strip.setPixelColor(i, led_strip.Color(255,0,0));
    led_strip.show();
    delay(10); 
  }
  for (int i=0; i < num_neopixels; i++){
    led_strip.setPixelColor(i, led_strip.Color(0,255,0));
    led_strip.show();
    delay(10); 
  }
}
