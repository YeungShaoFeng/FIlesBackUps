#include "pre_def.h"
#include "mystructs.h"
#include "quartileDeviation.h"

int quartileDeviation(sensor* sen1, sensor* sen2) {
	QD A = { 0, 0, 0, 0, 0, 0 };
	
	if ((length + 1) % 4 == 0) {
		A.xq1_1 = (length + 1) / 4;
		A.xq3_1 = A.xq1_1 * 3;
		position1(sen1, &A);
		if (sen2 != EMPTY) {
			position1(sen2, &A);
		}
	}
	else {
		A.xq1_1 = (int)((length + 1) / 4);
		A.xq1_2 = A.xq1_1 + 1;
		A.xq3_1 = (int)(3 * ((length + 1) / 4));
		A.xq3_2 = A.xq3_1 + 1;
		position2(sen1, &A);
		if (sen2 != EMPTY) {
			position2(sen2, &A);
		}
	}
	return 0;
}

void position1(sensor* sen, QD* ptr) {
	ptr->Q1 = sen->values_a[ptr->xq1_1];
	ptr->Q3 = sen->values_a[ptr->xq3_1];
	sen->Q_a = ptr->Q3 - ptr->Q1;
	sen->Q_b = ptr->Q3 - ptr->Q1;
}

void position2(sensor* sen, QD* ptr) {
	ptr->Q1 = 0.25 * sen->values_a[ptr->xq1_1] + 0.75 * sen->values_a[ptr->xq1_2];
	ptr->Q3 = 0.25 * sen->values_a[ptr->xq3_1] + 0.75 * sen->values_a[ptr->xq3_2];
	sen->Q_a = ptr->Q3 - ptr->Q1;
	
	ptr->Q1 = 0.25 * sen->values_b[ptr->xq1_1] + 0.75 * sen->values_b[ptr->xq1_2];
	ptr->Q3 = 0.25 * sen->values_b[ptr->xq3_1] + 0.75 * sen->values_b[ptr->xq3_2];
	sen->Q_b = ptr->Q3 - ptr->Q1;
}