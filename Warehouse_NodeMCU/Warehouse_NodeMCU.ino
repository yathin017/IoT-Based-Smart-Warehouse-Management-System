#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include <ArduinoJson.h>
#include <ESP8266HTTPClient.h>

#define loopdelay 3000
#define setupdelay 20000
#define freq 4

// Relay variables
int isac=0;
int isfan=0;
int islight=0;
int iswaterflow=0;

// Relay setup
#define acstate D8
#define fanstate D5
#define lightstate D4
#define waterflowstate D6

// Load-cell setup
#include "HX711.h"
#define calibration_factor 895000
#define DOUT D3
#define CLK D2
float Weight; //variable to store sensor value
HX711 scale(DOUT, CLK);

// DHT-11 setup
#include "DHT.h"

// MQ3 setup
#define MQ3pin A0
int Alcohol;  //variable to store sensor value

// LDR setup
#define LDR D7
int ldrval=0;

// FireBase setup
#define FIREBASE_HOST " " //--> URL address of Firebase Realtime Database.
#define FIREBASE_AUTH " " //--> database secret code.

//DHT-11 Setup
#define DHTTYPE DHT11 //--> Defines the type of DHT sensor used (DHT11, DHT21, and DHT22), in this project the sensor used is DHT11.
const int DHTPin = 5; //--> The pin used for the DHT11 sensor is Pin D1 = GPIO5
DHT dht(DHTPin, DHTTYPE); //--> Initialize DHT sensor, DHT dht(Pin_used, Type_of_DHT_Sensor);

// Wifi setup
const char* ssid = "Srija"; //--> Your wifi name or SSID.
const char* password = "7207842318"; //--> Your wifi password.
#define ON_Board_LED 2  //--> Defining an On Board LED, used for indicators when the process of connecting to a wifi router

void setup() {
// Serial Setup
  Serial.begin(9600);
  
//Relay Setting
  pinMode(acstate,OUTPUT);
  pinMode(fanstate,OUTPUT);
  pinMode(lightstate,OUTPUT);
  pinMode(waterflowstate,OUTPUT);

//Wifi Setup
  WiFi.begin(ssid, password); //--> Connect to your WiFi router
  Serial.println("");
  pinMode(ON_Board_LED,OUTPUT); //--> On Board LED port Direction output
  digitalWrite(ON_Board_LED, HIGH); //--> Turn off Led On Board

// Wait for connection
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
// Make the On Board Flashing LED on the process of connecting to the wifi router.
    digitalWrite(ON_Board_LED, LOW);
    delay(250);
    digitalWrite(ON_Board_LED, HIGH);
    delay(250);
  }
    digitalWrite(ON_Board_LED, HIGH); //--> Turn off the On Board LED when it is connected to the wifi router.
// If successfully connected to the wifi router, the IP Address that will be visited is displayed in the serial monitor
  Serial.println("");
  Serial.print("Successfully connected to : ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();

// Load-cell setup
Serial.println("Calibrate");
  scale.set_scale(calibration_factor);
  scale.tare();
  Serial.println("OK");

// DHT-11 setup
  dht.begin();  //--> Start reading DHT-11 sensors
    
  // Firebase Realtime Database Configuration.
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  
  delay(setupdelay);
  Serial.println("Setup Complete");
}

void loop() {

// Load-cell
Weight = scale.get_units()*200;
Serial.print("Reading: ");
  Serial.print(Weight);
  Serial.println("gms");
  if(Weight<0){
    Weight = 0;
  }
  if(Weight>=100){
    Weight=100;
  }

// DHT-11
  int h = dht.readHumidity(); //--> Read humidity.
  float t = dht.readTemperature(); //--> Read temperature as Celsius (the default). 
  
// Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(" Failed to load DHT sensor !");
    delay(1000);
    return;
  }

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.println(F("°C "));

// MQ3
  Alcohol = analogRead(MQ3pin); // read digital output pin
  Serial.print("Digital Output: ");
  Serial.print("Alcohol level: ");
  
// Determine the status
  if (Alcohol) {
    Serial.println("  |  Fresh");
  } else {
    Serial.println("  |  Rotten!");
  }

// LDR

  if(digitalRead(LDR)==LOW)
  {
    Serial.println("Bright");
    ldrval=100;
  }
  else
  {
    Serial.println("Dark");
    ldrval=0;
  }



// Send Humidity data to the Firebase Realtime Database.
  Firebase.setFloat("Humidity",h); //--> Command or code for sending data (Integer data type) to the Firebase Realtime Database.

// Conditions for handling errors.
  if (Firebase.failed()) { 
      Serial.print("setting Humidity failed :");
      Serial.println(Firebase.error());  
      delay(500);
      return;
  }

  Firebase.setFloat("Weight",Weight); //--> Command or code for sending data (Integer data type) to the Firebase Realtime Database.

// Conditions for handling errors.
  if (Firebase.failed()) { 
      Serial.print("setting Weight failed :");
      Serial.println(Firebase.error());  
      delay(500);
      return;
  }

// Send Temperature data to the Firebase Realtime Database.
  Firebase.setFloat("Temp",t); //--> Command or code for sending data (Float data type) to Firebase Realtime Database.

// Conditions for handling errors.
  if (Firebase.failed()) { 
      Serial.print("setting Temperature failed :");
      Serial.println(Firebase.error());  
      delay(500);
      return;
  }

if (Alcohol>1000){
  Alcohol=1000;
  }
if (Alcohol<620){
  Alcohol=100;
}
  
  Firebase.setFloat("Alcohol",Alcohol/10); //--> Command or code for sending data (Float data type) to Firebase Realtime Database.
// Conditions for handling errors.
  if (Firebase.failed()) { 
      Serial.print("setting Alcohol failed :");
      Serial.println(Firebase.error());  
      delay(500);
      return;
  }

  Firebase.setFloat("Light",ldrval); //--> Command or code for sending data (Float data type) to Firebase Realtime Database.
// Conditions for handling errors.
  if (Firebase.failed()) { 
      Serial.print("setting Light failed :");
      Serial.println(Firebase.error());  
      delay(500);
      return;
  }
  
  Serial.println("Setting successful");
  Serial.println();
  delay(1000);

for(int x=0;x<freq;x++){

 isac=Firebase.getInt("isac");
 isfan=Firebase.getInt("isfan");
 islight=Firebase.getInt("islight");
 iswaterflow=Firebase.getInt("iswaterflow");
 Serial.print("Fan State: ");
 Serial.println(isfan);
 Serial.print("AC State: ");
 Serial.println(isac);
 Serial.print("Light State: ");
 Serial.println(islight);
 Serial.print("waterflow State: ");
 Serial.println(iswaterflow);
 Serial.println(" ");
 Serial.println(" ");

 if(isac==0){digitalWrite(acstate,LOW);}
 else{digitalWrite(acstate,HIGH);}

 if(isfan==0){digitalWrite(fanstate,LOW);}
 else{digitalWrite(fanstate,HIGH);}
 
 if(islight==0){digitalWrite(lightstate,LOW);}
 else{digitalWrite(lightstate,HIGH);}
 
 if(iswaterflow==0){digitalWrite(waterflowstate,LOW);}
 else{digitalWrite(waterflowstate,HIGH);}

  delay(loopdelay/freq);

}
  
}
