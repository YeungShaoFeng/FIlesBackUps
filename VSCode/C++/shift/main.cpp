#include "Small.h"

int main()
{
    bool stop = false;
    while(stop)
    {
        cout << "> q/quit/exit to quit.";
        Small A(1);
        clock_t start, moddle, end;
        start = clock();

        A.smallIn(1, YES);

        moddle = clock();

        A.smallOut(1, YES);

        end = clock();

        cout << "total IN time = " << (double)(moddle - start) * 10 / CLOCKS_PER_SEC << endl;
        cout << "total OUT time = " << (double)(end - moddle) * 10 / CLOCKS_PER_SEC << endl;
        if ()
    }
	system("pause");
}
    // test codes
    // string plaintext = "how are you today?";
    // string password = "Linxi";
    // A.setString(1, plaintext);
    // A.setString(2, password);
	// cout << A.getstringlength("how are you?") << endl;
    // A.printString();

