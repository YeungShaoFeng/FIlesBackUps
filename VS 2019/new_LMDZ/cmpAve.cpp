#include "cmpAve.h"

int cmpAve(sensor* sen1, sensor* sen2)
{
	cmpAve_step(sen1);
	if (sen2 != EMPTY) {
		cmpAve_step(sen2);
	}
	return 0;
}


int cmpAve_step(sensor* sen)
{
	if ((sen->average_a) > (sen->average_b)) {
		sen->key = 1;
	}
	else if ((sen->average_a) < (sen->average_b)) {
		sen->key = -1;
	}
	else {
		sen->key = 0;
	}
	return 0;
}