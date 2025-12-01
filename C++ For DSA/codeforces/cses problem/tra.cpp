#include<bits/stdc++.h>
using namespace std;
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  int x,n; cin >> x >> n;
  set<int> pos;
  multiset<int> len;
  pos.insert(0), pos.insert(x);
  len.insert(x-0);
  for(int i=0; i<n; i++){
    int val; cin >> val;
    pos.insert(val);
    auto it = pos.find(val);
    int prev_val = *prev(it);
    int next_val = *next(it);
    len.erase(len.find(next_val - prev_val));
    len.insert(val - prev_val);
    len.insert(next_val - val);
    cout << *len.rbegin() << " ";
  }
}