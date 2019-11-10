#ifndef _SENSOR_H_
#define _SENSOR_H_


typedef struct {
	char valName[10];
	int values_a[100], values_b[100];
	double average_a, average_b;
	double Q_a, Q_b;
}sensor;


#endif
