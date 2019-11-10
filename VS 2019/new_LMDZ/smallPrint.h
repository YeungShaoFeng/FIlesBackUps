#ifndef _SMALLPRINT_H_
#define _SMALLPRINT_H_

#include <HardwareSerial.h>
#include "pre_def.h"
#include "sensor-s.h"

constexpr extern char aa[12] = "average_a: ";
constexpr static char ab[12] = "average_b: ";
constexpr static char qa[6] = "Q_a: ";
constexpr static char qb[6] = "Q_b: ";

int smallPrint(sensor* sen1, sensor* sen2);
int smallPrint_step(sensor* sen);

#endif