#ifndef _MYHEAD_H_
#define _MYHEAD_H_


#include "myStructs.h"
#include "heads.h"

sensor sensor1 = { "sensor1", 0, 0, 0, 0, 0, 0 };
sensor sensor2 = { "sensor2", 0, 0, 0, 0, 0, 0 };
extern int length;
int length = sizeof(sensor1.values_a) / sizeof(sensor1.values_a[0]);
int Delay = 100 / length;

#include "mylib.h"


#endif
