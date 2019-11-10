#include "myhead.h"

sensor sensor1 = { "sensor1", 0, 0, 0, 0, 0, 0 };
sensor sensor2 = { "sensor2", 0, 0, 0, 0, 0, 0 };
int length = sizeof(sensor1.values_a) / sizeof(sensor1.values_a[0]);
int Delay = 1000 / length;

void setup()
{
	pinMode(PB0, INPUT);
	pinMode(PB1, OUTPUT);
	pinMode(PA0, INPUT);
	pinMode(PA1, OUTPUT);
	Serial.begin(115200);
}

void loop()
{
	//start getting the values from the board
	//compere the two values array's sum
	//in order to find whether pressed or not
	getValue(&sensor1, &sensor2);
	int keys[2] = { 0 , 0};
	cmpValues(&sensor1, &sensor2, keys);
	draw(keys);

	//rearange the values
	rearrange(&sensor1, &sensor2);
	
	//get the average of the datas
	aveRage(&sensor1, &sensor2);

	//Quartile deviation
	quartileDeviation(&sensor1, &sensor2);
}

