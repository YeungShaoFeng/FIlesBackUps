#include "valuesPrint.h"


int valuesPrint(sensor *sen1, sensor *sen2) {
	stepPrint_a(sen1);
	stepPrint_b(sen1);
	if (sen2 != EMPTY) {
		stepPrint_a(sen2);
		stepPrint_b(sen2);
	}
	return 0;
}

int stepPrint_a(sensor* sen) {
	int i;
	Serial.println(sen->sensorName);
	Serial.print(SPACES);
	Serial.println("values_a: ");
	Serial.print(SPACES);
	Serial.print(SPACES);
	for (i = 0; i < length; i++) {
		Serial.print(sen->values_a[i]);
		Serial.print(", ");
		if (i%5==4) {
			Serial.println();
			Serial.print(SPACES);
			Serial.print(SPACES);
		}
	}
	Serial.println();
	return 0;
}

int stepPrint_b(sensor* sen) {
	int i;
	Serial.print(SPACES);
	Serial.println("values_b: ");
	Serial.print(SPACES);
	Serial.print(SPACES);
	for (i = 0; i < length; i++) {
		Serial.print(sen->values_b[i]);
		Serial.print(", ");
		if (i % 5 == 4) {
			Serial.println();
			Serial.print(SPACES);
			Serial.print(SPACES);
		}
	}
	Serial.println();
	return 0;
}