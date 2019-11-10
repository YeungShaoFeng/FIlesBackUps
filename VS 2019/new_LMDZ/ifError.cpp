// 
// ERRORS HANDLING
// 

#include "ifError.h"


int iferror = 0;

void errorGO(void)
{
	switch (ifError) {
	
	case ( AVERAGE ): Serial.println("aveRage()Error");

	case ( COMPAVE ): Serial.println("ampAve()Error");
	
	case (CMPVALUES): Serial.println("ampValues()Error");
	
	case DRAW: Serial.println("draw()Error");
	
	case GETVALUE: Serial.println("getValue()Error");
	
	case QDEV: Serial.println("QDev()Error");
	
	case REARANGE: Serial.println("rearange()Error");
	
	case SMALLPRINT: Serial.println("smallPrint()Error");
	
	case VALUESPRINT:Serial.println("valuesPrint()Error");
	}
}