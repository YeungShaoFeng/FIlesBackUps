#ifndef _AVERAGE_H_
#define _AVERAGE_H_


int aveRage(int* values, double* average, int length) {
	int i;
	for (i = 0; i < length; i++) {
		*average += values[i];
	}
	*average /= length;
	return 0;
}

#endif // !_AVERAGE_H_v
