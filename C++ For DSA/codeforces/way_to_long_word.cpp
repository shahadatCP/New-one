#include<bits/stdc++.h>
using namespace std; 
int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        string s;
        cin >> s;
        s.size();
        if(s.size() < 10)
        {
            cout << s << endl;
        }
        else
        {
            cout << s[0] << s.size()-2 << s[s.size()-1] << endl;
        }   
    }
    return 0;
}