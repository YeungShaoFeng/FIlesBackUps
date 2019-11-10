#ifndef _SENSOR_H_
#define _SENSOR_H_

typedef struct sensor{
	char sensorName[10];
	int values_a[10], values_b[10];
	int key;
	double average_a, average_b;
	double Q_a, Q_b;
}sensor;

#endif