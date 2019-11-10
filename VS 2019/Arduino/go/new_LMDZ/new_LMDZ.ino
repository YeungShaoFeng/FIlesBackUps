#include "myhead.h"

sensor sensor1 = { "sensor1", 0, 0, 0, 0, 0, 0 };
sensor sensor2 = { "sensor2", 0, 0, 0, 0, 0, 0 };
QD A = { 0, 0, 0, 0, 0, 0 };
int length = sizeof(sensor1.values_a) / sizeof(sensor1.values_a[0]);
int Delay = 1000 / length;

void setup()
{
	pinMode(SEN1_INPUT_PIN, INPUT_ANALOG);
	pinMode(SEN1_OUTPUT_PIN, OUTPUT);
	pinMode(SEN2_INPUT_PIN, INPUT_ANALOG);
	pinMode(SEN2_OUTPUT_PIN, OUTPUT);
	Serial.begin(115200);
}

void loop()
{
	int value = 0;
	//start getting the values from the board
	//compere the two values array's sum
	//in order to find whether pressed or not
	value = getValue(&sensor1, EMPTY);
	//int keys[2] = { 0 , 0};
	//cmpValues(&sensor1, &sensor2, keys);
	//draw(keys);
	//rearange the values
	rearrange(&sensor1, EMPTY);
	valuesPrint(&sensor1, EMPTY);

	//get the average of the datas
	aveRage(&sensor1, EMPTY);

	//Quartile deviation
	quartileDeviation(&sensor1, EMPTY);
}

