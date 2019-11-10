// draw_get.h

#ifndef _DRAW_GET_h
#define _DRAW_GET_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif

#include "mystructs.h"
void draw_get(sensor* sen, int* index);
void draw_get_step(int* keys, int i);

#endif

