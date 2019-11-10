#ifndef _DRAW_H_
#define _DRAW_H_

#include "pre_def.h"
#include "mystructs.h"
#include <HardwareSerial.h>

int draw(sensor* sen1, sensor* sen2);
int draw_all(sensor* sen1, sensor* sen2);
int draw_one(sensor* sen);

#endif