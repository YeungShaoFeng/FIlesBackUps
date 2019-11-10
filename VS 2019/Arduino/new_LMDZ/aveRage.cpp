#include "pre_def.h"
#include "sensor_struct.h"
#include "aveRage.h"

void aveRage(sensor* sen1, sensor* sen2) {
	aveRage_step(sen1);
	aveRage_step(sen2);
}

void aveRage_step(sensor* sen) {
	int i;
	for (i = 0; i < length; i++) {
		sen->average_a += sen->values_a[i];
		sen->average_b += sen->values_b[i];
	}
	sen->average_a /= length;
	sen->average_b /= length;
}