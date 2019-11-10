#include <HardwareSerial.h>
#include "draw.h"

void draw(int* keys) {
	step(keys, 0);
	step(keys, 1);
}

void step(int* keys, int i) {
	int p;
	int cnt = 4;
	if (keys[i] == 1) {
		++cnt;
	}
	else if (keys[i] == -1) {
		--cnt;
	}
	else if (keys[i] == 0) {
		cnt = cnt;
	}
	for (p = 0; p < cnt; p++) {
		Serial.print("~");
	}
	Serial.println();
}