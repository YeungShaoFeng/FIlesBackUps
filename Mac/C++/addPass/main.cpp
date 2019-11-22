#include <iostream>
#include <fstream>
using namespace std;

int addPass(string passPath, int argc, const char *argv[]);
int join(string *ifilePath, string *ofilePath);

int test()
{
    ifstream f("./addPass/passwords/unzip.txt");
    string line;

    while (getline(f, line))
    {
        cout << line << endl;
    }

    return 0;
}

int main(int argc, const char *argv[])
{
    int status = 0;
    string ip = "./addPass/passwords/unzip.txt";
    string op = "./addPass/passwords/unzip01.txt";
    string *ifilePath = &ip;
    string *ofilePath = &op;

    status = join(ifilePath, ofilePath);

    string passPath = "/Users/linxi/Documents/passwords/unzip/unzipEinse.txt";

    // status = addPass(passPath, argc, argv);

    return 0;
}

int addPass(string passPath, int argc, const char *argv[])
{
    int status = 0;
    fstream pf;
    char data[128] = {char(NULL)};
    if (passPath == "")
    {
        passPath = "/Users/linxi/Documents/passwords/unzip/unzipEinse.txt";
    }

    pf.open(passPath, ios::app);
    if (!pf)
    {
        status = -1;
        cout << "Failed to open " + passPath << endl;
        return status;
    }

    for (int i = 1; i < argc; i++)
    {
        pf << argv[i] << endl;
    }

    pf.close();
    return status;
}

int join(string *ifilePath, string *ofilePath)
{
    int status = 0;
    string line;
    fstream ifile, ofile;
    ifile.open(*ifilePath, ios::in);
    ofile.open(*ofilePath, ios::app);

    if (ifile && ofile)
    {
        while (getline(ifile, line))
        {
            {
                cout << line << endl;
            }
            ofile << line << endl;
        }
    }
    else
    {
        if (!ifile)
        {
            cout << "Failed to open " << *ifilePath << endl;
        }
        if (!ofile)
        {
            cout << "Failed to open " << *ofilePath << endl;
        }
        status = -1;
    }
    f

    ifile.close();
    ofile.close();

    return status;
}
