// 
// 
// 

#include "draw_get.h"

void draw_get(sensor* sen, int* index) {
	
}

void draw_get_step(int* keys, int i) {
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


