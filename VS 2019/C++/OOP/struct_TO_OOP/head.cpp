#include "heah.h"
#define PI 3.1415926


double Circle::CArea()
{
	return PI * r* r;
}
double Circle::CLen()
{
	return 2 * PI* r;
}

double Rectangle::RArea()
{
	return (length * width);
}
double Rectangle::RLen()
{
	return (2 * (length + width));
}