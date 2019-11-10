#include "draw.h"

int draw(sensor* sen1, sensor* sen2) {
	int go = 0;
	if (sen2 != EMPTY) {
		go = 1;
	}
	switch (go) {
		case 0:draw_all(sen1, sen2);
		case 1:draw_one(sen1);
	}
		
	return 0;
}

int draw_one(sensor* sen) {
	int p;
	int cnt = 4;
	if ((sen->key) == 1) {
		++cnt;
	}
	else if ((sen->key) == -1) {
		--cnt;
	}
	else if ((sen->key) == 0) {
		cnt = cnt;
	}
	for (p = 0; p < cnt; p++) {
		Serial.print(" ");
	}
	Serial.print("0");
	Serial.println();
	return 0;
}

int draw_all(sensor* sen1, sensor* sen2)
{
	return 0;
}