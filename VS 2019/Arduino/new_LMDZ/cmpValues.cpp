#include "pre_def.h"
#include "sensor_struct.h"
#include "cmpValues.h"


void cmpValues(sensor* sen1, sensor* sen2, int *key) {
	key[1] = cmp(sen1);
	key[2] = cmp(sen2);
}

int cmp(sensor* sen) {
	int i;
	int ret = 0;
	unsigned int sum_a = 0, sum_b = 0;
	for (i = 0; i < length; i++) {
		sum_a += sen->values_a[i];
		sum_b += sen->values_b[i];
	}
	if (sum_b > sum_a) {
		ret = 1;
	}
	else if (sum_b < sum_a) {
		ret = -1;
	}
	else if (sum_a == sum_b) {
		ret = 0;
	}

	return ret;
}