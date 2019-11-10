#include <io.h>
//#include <board.cpp>
#include <wirish_time.h>
#include "pre_def.h"
#include "mystructs.h"
#include "getValue.h"

int getValue(sensor* sen1, sensor* sen2) {
	int i;
	int value = 0;
	for (i = 0; i < length; i++) {
		sen1->values_a[i] = analogRead(SEN1_INPUT_PIN);
		value = sen1->values_a[i];
		if (sen2 != EMPTY) {
			sen2->values_a[i] = analogRead(SEN2_INPUT_PIN);	
		}
		delay(Delay);
		sen1->values_b[i] = analogRead(SEN1_INPUT_PIN);
		if (sen2 != EMPTY) {
			sen2->values_b[i] = analogRead(SEN1_INPUT_PIN);
		}
	}
	return value;
}