/*
DS18B20 Digital Temperature Sensor Test

Basic code to establish communication with the DS18B20 and retrieve temperature measurement data. 

Requires OneWire and DallasTemperature Libraries
*/

#include <OneWire.h> 
#include <DallasTemperature.h> 

const int ONE_WIRE_BUS = 4;  // Define a pin for communicating to the DS18B20 device via the oneWire bus.
OneWire oneWireLocal(ONE_WIRE_BUS);   // Setup a oneWire instance to communicate with the DS18B20 device
DallasTemperature sensorsLocal(&oneWireLocal);  // Pass this oneWire reference to DallasTemperature

float tempLocal = 0.0;    // Variable for holding the temperature returned from the sensor

//===============================================================================
//  Initialization
//===============================================================================
void setup() 
{ 
  Serial.begin (9600);      // Set output window comm rate
  sensorsLocal.begin();
}

//===============================================================================
//  Main
//===============================================================================
void loop() 
{
  CheckTemps();   // Call the routine that actually does the work
  Serial.print("Current Temp: ");  // Printout the results
  Serial.println(tempLocal);
   
  delay(100);
}

//===============================================================================
//  Subroutines
//===============================================================================
void CheckTemps()
{
  sensorsLocal.requestTemperatures();   // Send command to get temperature from the DS18B20
  // The sensor will return reading from previous request unless a delay is used to give it time to
  // complete the reading request.  If polling every second like we are doing here, the delay can be ignored.
  delay(100);  
  tempLocal = sensorsLocal.getTempCByIndex(0);  // There can be more than one device on this same bus
                                                // so we need to use the first index of (0)
}
