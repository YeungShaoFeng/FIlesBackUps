#ifndef _VALUESPRINT_H_
#define _VALUESPRINT_H_

#include <HardwareSerial.h>
#include "sensor-s.h"
#include "pre_def.h"
#include "mystructs.h"

int valuesPrint(sensor *sen1, sensor *sen2);
int stepPrint_a(sensor* sen);
int stepPrint_b(sensor* sen);

#endif
