#include<iostream>
using namespace std;
int main()
{
    int x;
    char c;
    double d;

    cin >> x >> c >> d;
    cout << x << endl << c << endl << d <<endl;

    // a er ascii value
    cout << (char)x << endl;
    cout << (char)d << endl; 
    cout << (int)c << endl;

    return 0;
}