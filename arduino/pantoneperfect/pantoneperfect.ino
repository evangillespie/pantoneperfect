#include <Adafruit_NeoPixel.h>

/*
   WHAT DOES THIS PROGRAM DO?
 
 Author: Evan Gillespie
 */

int neopixel_pin = 6;
int numstrip_neopixels = 3;
int num_neopixels = numstrip_neopixels*60;
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
   
  int red = 185;
  int green = 204;
  int blue = 195;

  light_strip(red, green, blue);
}

void light_strip(int red, int green, int blue) {
  int colrnum;
  int pixsize = 15;
  int pixstart;
  int pixend;
  // TODO: validation
  //Colour 0
  if (red == 223 && green == 213 && blue == 190)
  {
    colrnum = 0;
    pixstart = colrnum*pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();

  }
  //Colour 1
  else if (red == 216 && green == 212 && blue == 194)
  {
    colrnum = 1;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 2
  else if (red == 216 && green == 194 && blue == 194)
  {
    colrnum = 2;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 3
  else if (red == 215 && green == 211 && blue == 215)
  {
    colrnum = 3;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 4
  else if (red == 198 && green == 207 && blue == 193)
  {
    colrnum = 4;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 5
  else if (red == 196 && green == 194 && blue == 185)
  {
    colrnum = 5;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 6
  else if (red == 188 && green == 196 && blue == 191)
  {
    colrnum = 6;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 7
  else if (red == 184 && green == 192 && blue == 187)
  {
    colrnum = 7;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 8
  else if (red == 181 && green == 191 && blue == 187)
  {
    colrnum = 8;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 9
  else if (red == 185 && green == 204 && blue == 195)
  {
    colrnum = 9;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 10
  else if (red == 185 && green == 204 && blue == 195)
  {
    colrnum = 10;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 11
  else if (red == 160 && green == 185 && blue == 188)
  {
    colrnum = 11;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 12
  else if (red == 173 && green == 187 && blue == 173)
  {
    colrnum = 12;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 13
  else if (red == 164 && green == 188 && blue == 191)
  {
    colrnum = 13;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 14
  else if (red == 164 && green == 188 && blue == 191)
  {
    colrnum = 14;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 15
  else if (red == 143 && green == 177 && blue == 171)
  {
    colrnum = 15;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 16
  else if (red == 143 && green == 177 && blue == 172)
  {
    colrnum = 16;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 17
  else if (red == 129 && green == 158  && blue == 168)
  {
    colrnum = 17;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 18
  else if (red == 125 && green == 154 && blue == 170)
  {
    colrnum = 18;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 19
  else if (red == 118 && green == 154 && blue == 159)
  {
    colrnum = 19;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 20
  else if (red == 120 && green == 159 && blue == 168)
  {
    colrnum = 20;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 21
  else if (red == 95 && green == 141 && blue == 159)
  {
    colrnum = 21;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 22
  else if (red == 97 && green == 137 && blue == 152)
  {
    colrnum = 22;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = 30; i < 60; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 23
  else if (red == 90 && green == 128 && blue == 147)
  {
    colrnum = 23;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 24
  else if (red == 75 && green == 119 && blue == 135)
  {
    colrnum = 24;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 25
  else if (red == 71 && green == 115 && blue == 136)
  {
    colrnum = 25;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 26
  else if (red == 94 && green == 120 && blue == 143)
  {
    colrnum = 26;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 27
  else if (red == 68 && green == 105 && blue == 125)
  {
    colrnum = 27;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 28
  else if (red == 79 && green == 105 && blue == 132)
  {
    colrnum = 28;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 29
  else if (red == 52 && green == 101 && blue == 127)
  {
    colrnum = 29;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 30
  else if (red == 65 && green == 116 && blue == 141)
  {
    colrnum = 30;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 31
  else if (red == 24 && green == 41 && blue == 57)
  {
    colrnum = 31;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 32
  else if (red == 52 && green == 101 && blue == 127)
  {
    colrnum = 32;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 33
  else if (red == 52 && green == 101 && blue == 127)
  {
    colrnum = 33;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 34
  else if (red == 52 && green == 101 && blue == 127)
  {
    colrnum = 34;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 35
  else if (red == 48 && green == 88 && blue == 121)
  {
    colrnum = 35;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 36
  else if (red == 50 && green == 84 && blue == 119)
  {
    colrnum = 36;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 37
  else if (red == 57 && green == 87 && blue == 117)
  {
    colrnum = 37;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 38
  else if (red == 50 && green == 84 && blue == 119)
  {
    colrnum = 38;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 39
  else if (red == 34 && green == 65 && blue == 101)
  {
    colrnum = 39;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 40
  else if (red == 56 && green == 79 && blue == 107)
  {
    colrnum = 40;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 41
  else if (red == 37 && green == 54 && blue == 89)
  {
    colrnum = 41;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 42
  else if (red == 42 && green == 55 && blue == 79)
  {
    colrnum = 42;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 43
  else if (red == 47 && green == 54 && blue == 84)
  {
    colrnum = 43;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 44
  else if (red == 50 && green == 67 && blue == 84)
  {
    colrnum = 44;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 45
  else if (red == 47 && green == 51 && blue == 73)
  {
    colrnum = 45;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 46
  else if (red == 47 && green == 51 && blue == 73)
  {
    colrnum = 46;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 47
  else if (red == 38 && green == 49 && blue == 69)
  {
    colrnum = 47;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 48
  else if (red == 61 && green == 64 && blue == 77)
  {
    colrnum = 48;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 49
  else if (red == 49 && green == 53 && blue == 62)
  {
    colrnum = 49;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 50
  else if (red == 46 && green == 50 && blue == 56)
  {
    colrnum = 50;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 51
  else if (red == 51 && green == 50 && blue == 53)
  {
    colrnum = 51;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = 0; i < led_strip.numPixels(); i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 52
  else if (red == 19 && green == 3 && blue == 3)
  {
    colrnum = 52;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  //Colour 53 Middle Grey
  else if (red == 199 && green == 201 && blue == 199)
  {
    colrnum = 53;
    pixstart = colrnum*pixsize;
    pixend=pixstart+pixsize;
    for (int i = pixstart; i < pixend; i++) {
      led_strip.setPixelColor(i, led_strip.Color(red, green, blue));
    }
    led_strip.show();
  }
  else
  {
    for (int i = 0; i < led_strip.numPixels(); i++) {
      led_strip.setPixelColor(i, led_strip.Color(255, 255, 255));
    }
    led_strip.show();
  }

}


