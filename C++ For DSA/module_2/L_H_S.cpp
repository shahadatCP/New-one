#include<bits/stdc++.h>
using namespace std;


int *p;
void fun()
{
    int x=30;
    p = &x;
    cout << "Fun ->" << *p << endl;
    return;
}

int main()
{
    fun();
    cout << "Fun ->" << *p << endl;
    return 0;
}