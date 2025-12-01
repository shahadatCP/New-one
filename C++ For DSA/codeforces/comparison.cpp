#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a, b;
    char ch;
    cin >> a >> ch >> b;
    if(ch=='<')
    {
        if(a<b){
            cout << "Right\n";
        }
        else{
            cout << "Wrong\n";
        }
    }
    if(ch=='>')
    {
        if(a>b)
        {
            cout << "Right\n";
        }
        else{
            cout << "Wrong\n";
        }
    }
    
    if(ch=='=')
    {
        if(a==b)
        {
            cout << "Right\n";
        }
        else{
            cout << "Wrong\n";
        }
    }
    
    
    return 0;
}