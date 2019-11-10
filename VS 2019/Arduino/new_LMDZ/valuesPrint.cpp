#include <HardwareSerial.h>
#include "pre_def.h"
#include "mystructs.h"
#include "valuesPrint.h"

void valuesPrint(sensor *sen1, sensor *sen2) {
	Serial.print("  ");
	stepPrint_a(sen1);
	stepPrint_b(sen1);
	if (sen2 != NULL) {
		stepPrint_a(sen2);
		stepPrint_b(sen2);
	}
	
	
}

void stepPrint_a(sensor* sen) {
	int i;
	for (i = 0; i < length; i++) {
		Serial.print(sen->values_a[i]);
		Serial.print(",");
	}
	Serial.println();
}

void stepPrint_b(sensor* sen) {
	int i;
	for (i = 0; i < length; i++) {
		Serial.print(sen->values_b[i]);
		Serial.print(",");
	}
	Serial.println();
}