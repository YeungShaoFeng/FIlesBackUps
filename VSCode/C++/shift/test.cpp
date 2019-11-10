#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    // char* a = "how are you?";
    // int cnt = 0;
    // // char get;
    // // get = getchar();
    // // cout << get << endl;
    // while (a[cnt] != '\0')
    // {
    //     a[cnt] = char(int(a[cnt]) + cnt*1000);
    //     cout << a[cnt] << '\t';
    //     cnt ++;
    // }
    int a[10] = {0,1,2,3,4,5,6,7,8,9};
    int *p = a;
    cout << "sizeof(a) : " << sizeof(a) << endl;
    cout << "sizeof(a[0]):" << sizeof(a[0]) << endl;
    cout << "        a : " << a << endl;
    cout << "    a + 1 : " << a+1 << endl;
    cout << "   &a + 1 : " << &a+1 << endl;
    cout << "&a[0] + 1 : " << &a[0] + 1 << endl;
    cout << "&a[1] + 1 : " << &a[1] + 1 << endl;
    for (int i=0; i<int(sizeof(a)/sizeof(a[0])); i++) {
        cout << *(a+i) << "\t";
    }
    cout << endl;
    for (int i=0; i<int(sizeof(a)/sizeof(a[0])); i++) {
        cout << *(p+i) << "\t";
    }
    cout << endl;
    for (int i=0; i<int(sizeof(a)/sizeof(a[0])); i++) {
        cout << *(a+i) << "\t";
    }
    cout << endl;
    system("pause");
}