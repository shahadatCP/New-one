#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
  ll n; cin >> n;
  ll mx = 0, sum = 0;
  for(int i=0; i<n; i++){
    ll x; cin >> x;
    sum += x; 
    mx = max(x, mx);
  }
  if(mx*2>=sum){
    cout << mx*2 << endl;
  }
  else cout << sum << endl;
}
