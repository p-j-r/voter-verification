/*    SD card Module - Arduino UNO

              MOSI - Pin 11

              MISO - Pin 12

              SCK  - Pin 13

              CS   - Pin 4

              RX-5, TX-6


*/




#include <SPI.h>
#include <SD.h>
#include "SoftwareSerial.h"


SoftwareSerial device(5,6);     //  RX|TX
File store;                     // Store IDs
File read_store;                // Read 'em
int ctr=0;                      // All voters
int vtr=0;                      // Valid voters

int validate();
int fstore();

void setup() {
  // put your setup code here, to run once:
  
Serial.begin(9600); 
device.begin(9600);  

 if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    while (1);
  }

 // write to file...
 store=SD.open("data.txt",FILE_WRITE);
 store.println("11bbbb000");      // Keep this line! It doesn't show up in file but is essential for validate() to work...
 Serial.println("11bbbb000:::");
}

void loop() {
  // put your main code here, to run repeatedly:
  
//from bluetooth to Terminal. 
 if (device.available()) 
 {
   String aid=device.readString();    // Alleged ID
   ctr++;
   Serial.println(String(ctr)+=String("  ")+=aid); 
   validate(aid);
   //Serial.println(vtr+"  "+ctr);
   
 }
 }

void validate(String vid)     // Validates id and calls fstore
{
  vid.trim();     // Trim extra whitespace
  
  read_store = SD.open("data.txt"); 
  String s;  
  int flag=0;
  read_store.seek(0);
  if (read_store) {
    
    // read from the file until there's nothing else in it:
    while (read_store.available()) 
    {
      s=String(read_store.readStringUntil('\n'));
      s.trim();
      if (vid.equals(s))
      {
        flag=1;
        break;
      }
      
     }
        
     read_store.close();
  
      if (flag==1)
      {
        Serial.println(vid+" repeats...");
        //beep or maybe LED as tone() interferes with pin 3 & 11!
        // red And blue LEDs
      }
      else 
      {
        vtr++;
        int status_code=fstore(vid);    
        
        
      }     
    
   }
   else {
    Serial.println("error opening DATA.txt");
    Serial.print(read_store);
 
}
 
}


int fstore(String id)   // File-store
{
  store = SD.open("data.txt", FILE_WRITE);

  if (store) {
    store.println(id);    
    store.close();
     } 
     else {
    Serial.println("error writinopening DATA.txt");
    }
  return(0);
}
