/*
 Name:		Sketch_demo.ino
 Created:	2019/3/26 11:34:55
 Author:	Linxi
 NOT GOOD NOT GOOD NOT GOOD :<
*/


#include "myHead.h"


/*
//func prototype
void aveRage(sensor* sen1, sensor* sen2);
int cmpValues(sensor* sen1, sensor* sen2);
	int cmp(sensor* sen);
void draw(int* keys);
	void step(int* keys, int* cnt, int i);
void draw(int* keys);
int getValue(sensor* sen1, sensor* sen2);
int quartileDeviation(sensor* sen1, sensor* sen2);
	void position1(sensor* sen, QD* ptr);
	void position2(sensor* sen, QD* ptr);
int rearrange(sensor* sen1, sensor* sen2);  */


void setup()
{
	pinMode(PB0, INPUT);
	pinMode(PB1, OUTPUT);
	pinMode(PA0, INPUT);
	pinMode(PA1, OUTPUT);
	Serial.begin(9600);
}


void loop()
{
	//start getting the values from the board
	//compere the two values array's sum
	//in order to find whether pressed or not
	getValue(&sensor1, &sensor2);
	int keys[2] = { 0 , 0};
	cmpValues(&sensor1, &sensor2);
	draw(keys);

	//rearange the values
	rearrange(&sensor1, &sensor2);
	
	//get the average of the datas
	aveRage(&sensor1, &sensor2);

	//Quartile deviation
	quartileDeviation(&sensor1, &sensor2);
}
