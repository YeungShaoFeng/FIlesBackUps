#include <HardwareSerial.h>
#include "draw_cmp.h"

void draw_cmp(int* keys) {
	draw_cmp_step(keys, 0);
	draw_cmp_step(keys, 1);
}

void draw_cmp_step(int* keys, int i) {
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