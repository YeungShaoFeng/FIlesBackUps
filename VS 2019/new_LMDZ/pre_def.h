#ifndef _PREDEF_H_
#define _PREDEF_H_

#ifndef EMPTY
#define EMPTY 0
#endif

#ifndef SEN1_INPUT_PIN
#define SEN1_INPUT_PIN PA0
#endif

#ifndef SEN1_OUTPUT_PIN
#define SEN1_OUTPUT_PIN PA1
#endif

#ifndef SEN2_INPUT_PIN
#define SEN2_INPUT_PIN PB0
#endif

#ifndef SEN2_OUTPUT_PIN
#define SEN2_OUTPUT_PIN PB1
#endif

#ifndef SPACES
#define SPACES  "    "
#endif

extern const int length;
extern const int Delay;

enum ERRORS {
	AVERAGE = 2,
	COMPAVE,
	CMPVALUES,
	DRAW,
	GETVALUE,
	QDEV,
	REARANGE,
	SMALLPRINT,
	VALUESPRINT,
	ERROR_NUMS = 9,
};

#endif