# IoT-Based-Smart-Warehouse-Management-System

## Open Arduino IDE,
#### Go to File -> Preferences -> add <a href="https://arduino.esp8266.com/stable/package_esp8266com_index.json">https://arduino.esp8266.com/stable/package_esp8266com_index.json</a> in Additional Boards Manager URLs and click OK

## Locate Documents folder in your PC (This is where all the code and libraries are stored by default),
#### Documents -> Arduino -> libraries -> add all the libraries used for the code from <a href="https://github.com/yathin017/IoT-Based-Smart-Warehouse-Management-System/tree/main/Warehouse_NodeMCU/Libraries_Used">Libraries_Used</a>

## Hardware Connections,

* Node-MCU ESP8266 (to breadboard)
  + Vin -> Vcc line
  + GND -> GND line
  
* DHT-11 (to Node MCU and bread board)
  + Vcc ('+') -> Vcc
  + GND ('-') -> GND
  + Out       -> D1
  
* LDR (to Node MCU and bread board)
  + Vcc -> Vcc
  + GND -> GND
  + DO  -> D7
  
* MQ3 (to Node MCU and bread board)
  + Vcc -> Vcc
  + GND -> GND
  + AO  -> A0
  
* Relay module (to Node MCU and bread board)
  + Vcc    -> Vcc
  + JD-Vcc -> Vcc
  + GND    -> GND
  + IN1    -> D8
  + IN2    -> D5
  + IN3    -> D4
  + IN4    -> D6
* Relay module (to appliances)
  + Battery ('-') -> Relay Common (COM)
  + Battery ('+') -> Pin1 (any one of the pin of the appliance)
  + Pin2 (another pin of the appliance) -> Relay Normally closed (NC)
  
* Load Cell (to HX-711)
  + Red   -> E+
  + Black -> E-
  + White -> A-
  + Green -> A+
  
* HX-711 (to Node MCU and bread board)
  + Vcc -> Vcc
  + GND -> GND
  + DT  -> D3 
  + SCK -> D2
  
