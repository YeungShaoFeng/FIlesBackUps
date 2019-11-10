/*
 Name:		test.ino
 Created:	2019/4/2 18:12:40
 Author:	Linxi
*/
#include "aveRage.h"
#include "externs.h"

int values_a[100] = { 0 };
int values_b[100] = { 0 };
double average_a, average_b = 0;
int length = sizeof(values_a) / sizeof(values_a[0]);

void setup() {
	pinMode(PB1, OUTPUT);
	Serial.begin(115200);
}


void loop() {

	aveRage(values_a, &average_a, length);
}
