#include <Small.h>
#include <iostream>
#include <string>
// mode = 1: live e and d;
Small::Small(int mode)
{
    if (mode) {
        // live e and d;
        if (mode == 1) {
            getinputs(1);
            getinputs(2);
        } else if(mode == 2) {

        }
    }
}

void Small::smallIn(int inMode, int printMode)
{
	int length = 0, i = 0;
	int len_plaintext = getstringlength(plaintext);
	int len_password = getstringlength(password);
	if (len_plaintext >= len_password) {
		length = len_password;
        while(plaintext[i] != '\0')
        {
            plaintext[i] = char(int(plaintext[i]) + int(password[i%length]));
            i++;
        }
	} else {
        length = len_plaintext;
        while(plaintext[i] != '\0')
        {
            plaintext[i] = char(int(plaintext[i]) + int(password[i]));
            i++;
        }    
    }
    if (printMode) {printString();}
}

void Small::smallOut(int outMode, int printMode)
{
    int length = 0, i = 0;
	int len_plaintext = getstringlength(plaintext);
	int len_password = getstringlength(password);
	if (len_plaintext >= len_password) {
		length = len_password;
        while(plaintext[i] != '\0')
        {
            plaintext[i] = char(int(plaintext[i]) - int(password[i%length]));
            i++;
        }
	} else {
        length = len_plaintext;
        while(plaintext[i] != '\0')
        {
            plaintext[i] = char(int(plaintext[i%length]) - int(password[i]));
            i++;
        }    
    }
    if (printMode) {printString();}
}

void Small::printString(void)
{
    cout << endl;
    cout << "Plaintext: " << plaintext << endl;
    cout << "password: " << password << endl;
}

//plaintext: 1 password: 2
void Small::setString(int which, string text)
{
    if (which == 1) {plaintext = text;}
    else if (which == 2) {password = text;}
}

int Small::getstringlength(string text)
{
    int cnt = 0;
    while(text[cnt] != '\0') {cnt ++;}
	return cnt;
}

void Small::getinputs(int mode)
{
	if (mode == 1) { 
		cout << "PlainText: ";
        getline(cin, plaintext);
	} else if (mode == 2) {
		cout << "Password: ";
        getline(cin, password);
	} else if (mode == 3) {
		cout << "File route: ";
		cin >> fileroute;
	} else if (mode == 4) {
		cout << "Dir route: ";
		cin >> dirrout;
	} else {
		cout << "getinputs()'s down. ";
	}
}