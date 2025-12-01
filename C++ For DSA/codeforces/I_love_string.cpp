#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        string s, s2;
        cin >> s;
        //cin.ignore();
        cin >> s2;
        int len = s.size();
        int len2 = s2.size();
        int mx = max(len, len2);
    
            for(int i=0; i<mx; i++)
            {
                if(i<s.size())
                	cout<<s[i];
                if(i<s2.size())
                	cout << s2[i];

            }

            cout << endl;
              
        
    }
    return 0;
}



/*
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        string s, t;
        cin >> s;
        cin.ignore();
        cin >> t;
        if(s.size() < t.size())
        {
            for(int i=0, j=0; i<s.size(), j<t.size()-1; i++,j++)
            {
                cout << s[i] << t[j];
            }
            cout << t.back();
            cout << endl;
        }
        else
        {
            for(int i=0, j=0; i<s.size(), j<t.size(); i++, j++)
            {
            		if(i<s.size())
                	cout<<s[i];
                if(i<t.size())
                	t[i];
                cout << s[i] << t[i] ;
            }

            cout << endl;
        }
        
        
    }
    return 0;
}


include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        string s, t;
        cin >> s;
        cin.ignore();
        cin >> t;
        if(s.size() < t.size())
        {
            for(int i=0, j=0; i<s.size(), j<t.size()-1; i++,j++)
            {
                cout << s[i] << t[j];
            }
            cout << t.back();
            cout << endl;
        }
        else
        {
            for(int i=0, j=0; i<s.size(), j<t.size(); i++, j++)
            {
            		if(i<s.size())
                	cout<<s[i];
                if(i<t.size())
                	t[i]
                cout << s[i] << t[i] ;
            }

            cout << endl;
        }
        
        
    }
    return 0;
}
*/