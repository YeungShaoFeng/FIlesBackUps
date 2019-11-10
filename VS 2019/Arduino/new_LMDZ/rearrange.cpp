#include "pre_def.h"
#include "mystructs.h"

int rearrange(sensor* sen1, sensor* sen2) {
	//rearenge the values in the values array from the least to the greatest
	int i, j, temp, isSorted;
	for (i = 0; i < length - 1; i++) {
		isSorted = 1;
		for (j = 0; j < length - 1 - i; j++) {
			if (sen1->values_a[j] > sen1->values_a[j + 1]) {
				temp = sen1->values_a[j];
				sen1->values_a[j] = sen1->values_a[j + 1];
				sen1->values_a[j + 1] = temp;
				isSorted = 0;
			}
		}
		if (isSorted) break;
	}
	for (i = 0; i < length - 1; i++) {
		isSorted = 1;
		for (j = 0; j < length - 1 - i; j++) {
			if (sen1->values_b[j] > sen1->values_b[j + 1]) {
				temp = sen1->values_b[j];
				sen1->values_b[j] = sen1->values_b[j + 1];
				sen1->values_b[j + 1] = temp;
				isSorted = 0;
			}
		}
		if (isSorted) break;
	}
	for (i = 0; i < length - 1; i++) {
		isSorted = 1;
		for (j = 0; j < length - 1 - i; j++) {
			if (sen2->values_a[j] > sen2->values_a[j + 1]) {
				temp = sen2->values_a[j];
				sen2->values_a[j] = sen2->values_a[j + 1];
				sen2->values_a[j + 1] = temp;
				isSorted = 0;
			}
		}
		if (isSorted) break;
	}
	for (i = 0; i < length - 1; i++) {
		isSorted = 1;
		for (j = 0; j < length - 1 - i; j++) {
			if (sen2->values_b[j] > sen2->values_b[j + 1]) {
				temp = sen2->values_b[j];
				sen2->values_b[j] = sen2->values_b[j + 1];
				sen2->values_b[j + 1] = temp;
				isSorted = 0;
			}
		}
		if (isSorted) break;
	}
	return 0;
}