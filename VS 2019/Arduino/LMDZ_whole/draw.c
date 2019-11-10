void draw(int* keys) {
	int cnt = 4;

	step(keys, &cnt, 0);
	step(keys, &cnt, 1);
}

void step(int* keys, int* cnt, int i) {
	int p;
	if (keys[i] == 1) {
		++cnt;
	}
	else if (keys[i] == -1) {
		--cnt;
	}
	else if (keys[i] == 0) {
		cnt = cnt;
	}
	for (p = 0; p < *cnt; p++) {
		Serial.print("~");
	}
	Serial.println();

}