#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n, l=0; cin >> n;
  map<int,int> mp;
  int mx=0;
  for(int i=0; i<n; i++){
    int x; cin >> x;
    if(mp.find(x)!=mp.end() && mp[x]>=l){
      l = mp[x]+1;
    }
    mp[x] = i;
    mx = max(mx, i-l+1);
  }
  cout << mx << '\n';
}