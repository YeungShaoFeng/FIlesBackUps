#include <iostream>
#define N 5
using namespace std;

int main()
{
	int i = 0, r, n, a[100];
	char HEX[16] = {'0','1','2','3','4','5','6','7',
					'8','9','A','B','C','D','E','F',};
	cin >> n >> r;
	do {
		a[i] = n % r;
		n = n / r;
		i++;
	} while (n != 0);
	for (--i; i >= 0; --i) {
		n = a[i];
		cout << HEX[n];
	}
	return 0;
}