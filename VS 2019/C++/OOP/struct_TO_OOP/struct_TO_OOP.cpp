#include <iostream>
#include "head.h"
using namespace std;



int main()
{
	Circle Cobj; Rectangle Robj;

	Cobj.r = 3; Robj.length = 4; Robj.width = 5;
	// cin >> Cobj.r >> Robj.length >> Robj.width;

	cout << "The area of the circle is: " << Cobj.CArea() << ". " << endl;
	cout << "The perimeter of the circle is: " << Cobj.CLen() << ". " << endl;

	cout << "The area of the rectangel is: " << Robj.RArea() << ". " << endl;
	cout << "The perimeter of the rectangle is: " << Robj.RLen() << ". " << endl;

	return 0;
}