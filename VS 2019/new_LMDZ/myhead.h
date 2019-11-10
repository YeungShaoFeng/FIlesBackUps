#ifndef _MYHEAD_H_
#define _MYHEAD_H_

#include "pre_def.h"
#include "mystructs.h"
#include "getValue.h"
#include "aveRage.h"
#include "cmpValues.h"
#include "cmpAve.h"
#include "draw.h"
#include "QDev.h"
#include "rearrange.h"
#include "smallPrint.h"
#include "valuesPrint.h"
//#include "ifError.h"

//THESE ARE THE DECLARATIONS OF THE TWO SENSOR, LENGTH AND THE DELAY TIME. 
sensor sensor1 = { "sensor1", 0, 0, 0, 0, 0, 0 ,0, };
sensor sensor2 = { "sensor2", 0, 0, 0, 0, 0, 0 ,0, };
const int length = sizeof(sensor1.values_a) / sizeof(sensor1.values_a[0]);
const int Delay = 1000 / length;

#endif