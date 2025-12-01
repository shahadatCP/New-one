#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n; cin >> n;
  vector<int> a(n);
  for(int i=0; i<n; i++) cin >> a[i];
  
  stack<int> st;
  vector<int> ans(n, 0);
  
  for(int i=0; i<n; i++){
    while(!st.empty() && a[st.top()]>=a[i]){
      st.pop();
    }
    if(!st.empty()){
      ans[i] = st.top() + 1;
    }
    st.push(i);
  }
  for(auto i : ans) cout << i << " ";
  cout << endl;
  return 0;
}