/*
 Name:		iomanip.ino
 Created:	4/20/2019 8:55:32 AM
 Author:	Linxi
*/

#include <iomanip>

int fmt(int w);


void setup() {
	Serial.begin(115200);
}

void loop() {
	fmt(1);	
	delay(500);
}

int fmt(int w = 1)
{
	std::setw(30*w);
	std::setfill("*");
	Serial.println("Hello There!");

	return 0;
}