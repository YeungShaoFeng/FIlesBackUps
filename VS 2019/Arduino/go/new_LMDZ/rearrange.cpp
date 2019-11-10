#include "pre_def.h"
#include "mystructs.h"
#include "rearrange.h"

int rearrange(sensor* sen1, sensor* sen2) {
	//rearenge the values in the values array
	//from the least to the greatest
	rearrange_step(sen1);
	if (sen2 != EMPTY) {
		rearrange_step(sen2);
	}

	return 0;
}

void rearrange_step(sensor* sen) {
	int i, j, temp, isSorted;
	//The average_a of the sensor obj
	for (i = 0; i < length - 1; i++) {
		isSorted = 1;
		for (j = 0; j < length - 1 - i; j++) {
			if (sen->values_a[j] > sen->values_a[j + 1]) {
				temp = sen->values_a[j];
				sen->values_a[j] = sen->values_a[j + 1];
				sen->values_a[j + 1] = temp;
				isSorted = 0;
			}
		}
		if (isSorted) break;
	}
	//The average_b of the sensor obj
	for (i = 0; i < length - 1; i++) {
		isSorted = 1;
		for (j = 0; j < length - 1 - i; j++) {
			if (sen->values_b[j] > sen->values_b[j + 1]) {
				temp = sen->values_b[j];
				sen->values_b[j] = sen->values_b[j + 1];
				sen->values_b[j + 1] = temp;
				isSorted = 0;
			}
		}
		if (isSorted) break;
	}
}