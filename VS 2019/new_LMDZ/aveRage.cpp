#include "aveRage.h"

int aveRage(sensor* sen1, sensor* sen2) {
	aveRage_step(sen1);
	if (sen2 != EMPTY) {
		aveRage_step(sen2);	
	}
	return AVERAGE;
}

int aveRage_step(sensor* sen) {
	int i;
	for (i = 0; i < length; i++) {
		sen->average_a += sen->values_a[i];
		sen->average_b += sen->values_b[i];
	}
	sen->average_a /= length;
	sen->average_b /= length;
	return 0;
}