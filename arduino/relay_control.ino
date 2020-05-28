 /*
* This is the Arduino code for Dual Channel 5V Relay
 * to control turn ON or OFF AC or DC load
 * Watch the video https://youtu.be/58XWVDnB7Ss
 *  * 
 * Written by Ahmad Nejrabi for Robojax Video
 * Date: Dec 26, 2017, in Ajax, Ontario, Canada
 * Permission granted to share this code given that this
 * note is kept with the code.
 * Disclaimer: this code is "AS IS" and for educational purpose only.
 * 
 */

void setup() {
  pinMode(7, OUTPUT);// connected to S terminal of Relay

}

void loop() {

  digitalWrite(7,HIGH);// turn relay ON
  delay(3000);// keep it ON for 3 seconds

  digitalWrite(7, LOW);// turn relay OFF
 delay(5000);// keep it OFF for 5 seconds

}
