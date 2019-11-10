void aveRage(sensor* sen1, sensor* sen2) {
	int i;
	for (i = 0; i < length; i++) {
		sen1->average_a += sen1->values_a[i];
		sen1->average_b += sen1->values_b[i];
		sen2->average_a += sen2->values_a[i];
		sen2->average_a += sen2->values_a[i];
	}
	sen1->average_a /= length;
	sen1->average_b /= length;
	sen2->average_a /= length;
	sen2->average_a /= length;
}