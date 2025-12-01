#include<bits/stdc++.h>
using namespace std;
int *p;
void fun()
{
    int *x = new int;
    *x = 25;
    p = x;
    cout<< "Fun ->" << *p << endl;
    return; 
}
int main()
{
    fun();
    cout<< "Main ->" << *p << endl;
    return 0;
}