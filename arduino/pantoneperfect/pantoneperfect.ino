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
  if (Serial.available() >= 3)  {
    pulse_led(Serial.available());
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
  delay(50);
  
//  light_strip(255, 0, 0);
//  delay(5000);
//  light_strip(0, 255, 0);
//  delay(5000);
//  light_strip(0, 0, 255);
//  delay(5000);
  
}

void pulse_led(int n) {
  digitalWrite(13, LOW);
  delay(500);
  for ( int i = 0; i < n; i++ ){
    digitalWrite(13, HIGH);
    delay(500);
    digitalWrite(13, LOW);
    delay(500);
  }
}
  
void blink_led() {
  digitalWrite(13, !digitalRead(13));
  delay(10);
  digitalWrite(13, !digitalRead(13));
} 

void light_strip(int red, int green, int blue) {
  // TODO: validation
  for (int i = 0; i < led_strip.numPixels(); i++) {
    led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
  }
  led_strip.show();
}
