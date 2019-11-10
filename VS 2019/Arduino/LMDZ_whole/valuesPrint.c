void valuesPrint(int* values) {
	int i;
	Serial.print("  ");
	for (i = 0; i < length; i++) {
		Serial.print(values[i]);
		Serial.print(",");
	}
	Serial.println();
}
