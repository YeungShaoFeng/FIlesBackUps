#include <iostream>
using namespace std;

int main()
{
	char CHAR = 'A';
	for (int i = 0; i < 26; i++) {
		CHAR += 1;
		cout << CHAR << "\t";
		if ((i + 1) % 5 == 0) { cout << endl; }
	}

	return 0;
}