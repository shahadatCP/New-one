#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  map<ll, ll> mp;
  ll n,x; cin >> n >> x;
  ll sum = 0, cnt = 0;
  mp[sum] = 1;
  for(int i=0; i<n; i++){
    int val; cin >> val;
    sum += val;
    cnt += mp[sum-x];
    mp[sum]++;
  }
  cout << cnt << endl;
  return 0;
}