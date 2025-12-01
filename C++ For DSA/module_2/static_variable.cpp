#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x = 10; // static variable
    cout << x << endl;
    int *y = new int; // dynamic variable
    *y = 200;
    cout << *y << endl;
}