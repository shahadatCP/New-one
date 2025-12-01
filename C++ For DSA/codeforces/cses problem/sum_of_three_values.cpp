#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n,x; cin >> n >> x;
  vector<pair<int,int>>v(n);
  for(int i=0; i<n; i++){
    int x; cin >> x;
    v[i] = {x,i};
  }
  sort(v.begin(), v.end());
  for(int i=0; i<n-2; i++){
    int need = x - v[i].first;
    int l=i+1, r=n-1;
    while(r>l){
      int val = v[l].first+v[r].first;
      if(val == need){
        cout << v[i].second+1 << " " << v[l].second+1 << " " << v[r].second+1 << endl;
        return 0;
      }
      else if(val<need){
        l++;
      } else r--;
    }
  }
  cout << "IMPOSSIBLE\n";
  return 0;
}