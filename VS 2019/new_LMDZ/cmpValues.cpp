 #include "cmpvalues.h"


void cmpValues(sensor* sen1, sensor* sen2) {
	cmpValues_step(sen1);
	if (sen2 != EMPTY) {
		cmpValues_step(sen2);
	}
}

void cmpValues_step(sensor* sen) {
	int i;
	unsigned int sum_a = 0, sum_b = 0;
	for (i = 0; i < length; i++) {
		sum_a += sen->values_a[i];
		sum_b += sen->values_b[i];
	}
	if (sum_b > sum_a) {
		sen->key = 1;
	}
	else if (sum_b < sum_a) {
		sen->key = -1;
	}
	else if (sum_a == sum_b) {
		sen->key = 0;
	}
}