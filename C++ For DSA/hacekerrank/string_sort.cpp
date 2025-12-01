#include <bits/stdc++.h>

using namespace std;



int main()
{
    // Write your code here
    string s;
    
    while(getline(cin, s))
    {
        sort(s.begin(), s.end());
        
        for(char ch : s)
        {
            if(ch!=' ')
            {
                cout << ch;
            }
        }
        cout << endl;
    }

    return 0;
}