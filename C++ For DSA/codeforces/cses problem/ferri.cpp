#include<bits/stdc++.h>
using namespace std;
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  long long n, x; cin >> n >> x;
  vector<long long> a(n);
  for(int i=0; i<n; i++)cin >> a[i];
  sort(a.begin(), a.end());
 
  long long cnt = 0, sum=0;
  for(int i=0, j=n-1; i<=j;){
    if(a[i]+a[j]<=x){
      cnt++, i++, j--;
    }
    else{
      cnt++, j--;
    }
  }
  cout << cnt << endl;
  return 0;
}