#include "smallPrint.h"


int smallPrint(sensor* sen1, sensor* sen2 = EMPTY)
{
	smallPrint_step(sen1);
	if (sen2 != EMPTY) {
		smallPrint_step(sen2);
	}
	return 0;
}

int smallPrint_step(sensor* sen)
{
	Serial.println(sen->sensorName);
	Serial.print(SPACES);
	Serial.print(aa);
	Serial.println(sen->average_a);
	Serial.print(SPACES);
	Serial.print(ab);
	Serial.println(sen->average_b);
	Serial.print(SPACES);
	Serial.print(qa);
	Serial.println(sen->Q_a);
	Serial.print(SPACES);
	Serial.print(qb);
	Serial.println(sen->Q_b);
	return 0;
}
