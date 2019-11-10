#include "myhead.h"


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
	//start getting the values from the board
	//compere the two values array's sum
	//in order to find whether pressed or not
	getValue(&sensor1, EMPTY);

	//rearange the values
	rearrange(&sensor1, EMPTY);
	//print the values
	//valuesPrint(&sensor1, EMPTY);
	//get the average of the datas
	aveRage(&sensor1, EMPTY);
	//compare the average of the values
	cmpAve(&sensor1, EMPTY);
	//draw the sen->key to see that 
	//wether the pressure is going up or down
	//draw(&sensor1, EMPTY);
	//Quartile deviation
	QDev(&sensor1, EMPTY);
	//print the smaller results
	//smallPrint(&sensor1, EMPTY);
	
}

