#include <iostream>
using namespace std;

int main()
{
	int N = 0;
	cout << "Input N: ";
	cin >> N;

	long long *p = new long long[N];
	p[0] = 0;p[1] = 1;

	int n;
	for (n = 2; n < N; n++) {
		p[n] = p[n - 1] + p[n - 2];
	}
	for (n = 0; n < N; n++) {
		cout << p[n] << "\a\b";
		if ((n + 1) % 10 == 0) { cout << endl; }
	}

	delete[]p;

	return 0;
}
