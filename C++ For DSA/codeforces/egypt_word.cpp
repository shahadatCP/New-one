#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "egypt";
    int f[26] = {0};
    for(int i=0; i<s.size(); i++)
    {
        int index = s[i] - 'a';
        f[index] = 1;
    }
    string s2;
    cin >> s2;
    for(auto& x : s2)
    {
        x = tolower(x);
    }
    int f2[26] = {0};
    for(int i=0; i<s2.size(); i++)
    {
        int index = s2[i] - 'a';
        f2[index] +=1;
    }
    int time = 0;
    for(int i=0; i<26; i++)
    {
        if(f[i]!=0)
        {
            if(f[i]!=f2[i])
            {
                f2[i]--;
            }
            
        }
    }
    cout << time << endl;
    return 0;
}