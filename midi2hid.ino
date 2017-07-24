#include "Mouse.h"
#include "Keyboard.h"

int mouseLeft  = 0;
int mouseRight = 0;
int mouseUp    = 0;
int mouseDown  = 0;

void setup() {
    delay(90000); // wait until linux side finishes to boot
    Serial1.begin(115200);
}

void loop() {
    if (Serial1.available() >= 2) {   
        char command = Serial1.read();
        char value   = Serial1.read();
         
        switch (command) {
            case 'L': mouseLeft  = value;    break;
            case 'R': mouseRight = value;    break;
            case 'U': mouseUp    = value;    break;
            case 'D': mouseDown  = value;    break;
            case 'M':  
                if(value ==1){ Mouse.press(); } else { Mouse.release(); }
                break;    
          
            case 'w':  
            case 's':  
            case 'a':  
            case 'd':  
            case 'j':  
            case '1':  
            case '2':  
            case '3':  
            case '4':  
            case '5':  
            case '6':  
            case '7':  
            case '8':  
            case '9':  
            case '0':  
                if(value ==1){ Keyboard.press(command); } else { Keyboard.release(command); }
                break;    
          
            case 'X':  
                mouseLeft  = 0;
                mouseRight = 0;
                mouseUp    = 0;
                mouseDown  = 0;
                Keyboard.releaseAll();
                break;    
        }
    }

    if (mouseLeft  != 0 or mouseUp   != 0) { Mouse.move(mouseLeft,  mouseUp);   }
    if (mouseRight != 0 or mouseDown != 0) { Mouse.move(mouseRight, mouseDown); }
}
