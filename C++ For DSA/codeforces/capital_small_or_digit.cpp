#include<bits/stdc++.h>
using namespace std;
int main()
{
    char ch;
    cin >> ch;

    if(ch>='0' && ch<='9')
    {
        cout << "IS DIGIT" << endl;
    }
    else
    {
        if(ch>= 'a' && ch <= 'z')
        {
            cout << "ALPHA" << endl << "IS SMALL" << endl; 
        }
        else if(ch >= 'A' && ch <='Z')
        {
            cout << "ALPHA" << endl << "IS CAPITAL" << endl;
        }
    }
    return 0;
}