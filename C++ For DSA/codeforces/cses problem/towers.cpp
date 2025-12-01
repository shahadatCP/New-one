#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n; cin >> n;
  multiset<int> ml;
  for(int i=0; i<n; i++){
    int x; cin >> x;
    auto it = ml.upper_bound(x);
    if(it == ml.end()){
      ml.insert(x);
    }
    else{
      ml.erase(it);
      ml.insert(x);
    }
  }
  cout << ml.size() << '\n';
}