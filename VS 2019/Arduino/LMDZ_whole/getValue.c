int getValue(sensor* sen1, sensor* sen2) {
	int i;
	for (i = 0; i < length; i++) {
		sen1->values_a[i] = analogRead(PB0);
		sen2->values_a[i] = analogRead(PA0);
		delay(Delay);
		sen1->values_b[i] = analogRead(PB0);
		sen2->values_b[i] = analogRead(PA0);
	}
	return 0;
}