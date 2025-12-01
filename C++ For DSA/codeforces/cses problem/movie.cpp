#include<bits/stdc++.h>
using namespace std;
bool cmp(pair<int,int> p1, pair<int,int> p2){
  return p1.second<p2.second;
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n; cin >> n;
  vector<pair<int,int>> a(n);
  for(int i=0; i<n; i++){
    int x,y; cin >> x >> y;
    a[i] = {x,y};
  }
  sort(a.begin(), a.end(), cmp);
  //for(auto [x,y] : a)cout << x << " "<< y << endl;
  int cnt = 1;
  auto prev = a[0];
  for(int i=1; i<n; i++){
    auto val = a[i];
    if(val.first>=prev.second){
      cnt++;
      prev = a[i];
    }
  }
  cout << cnt << endl;
  return 0;
}