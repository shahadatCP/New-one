#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c;
    cin >> a >> b >> c;
    int O_min = min({a,b,c});
    int O_max = max({a,b,c});
    cout << O_min << " " << O_max << endl;
    return 0;
}