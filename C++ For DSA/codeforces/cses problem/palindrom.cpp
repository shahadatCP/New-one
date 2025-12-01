#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long

bool cmp(pair<char, int>& a, pair<char, int>& b) {
	return a.second > b.second;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	string s, ans;
	cin >> s;
	int d = s.size();
	map<char,int> mp;
	for(auto c : s) {
		mp[c]++;
	}
	vector<pair<char,int>> freq(mp.begin(), mp.end());
	vector<int> v;

	sort(freq.begin(), freq.end(), cmp);

	int cnt = 0;
	for(auto it = freq.begin(); it!=freq.end(); ++it) {
		int freq1 = it->second;
		if(freq1%2!=0) cnt++;
	}
	if(cnt>1) {
		cout << "NO SOLUTION\n";
		return 0;
	}
	int ii ;
	char cc;
	for(auto it = freq.begin(); it!=freq.end(); ++it) {
		char ch = it->first;
		int freq1 = it->second;
		if(freq1%2!=0) {
			ii = freq1;
			cc = ch;
			break;
		}
	}

	for (auto it = freq.begin(); it!=freq.end(); ++it) {
		char ch = it->first;
		int freq1 = it->second;
		if(freq1%2==0)
		{
			for(int i=0; i<freq1/2; i++) {
				ans+=ch;
			}
		}
	}

	if(d%2!=0) {
		for(int i=0; i<ii; i++) {
			ans += cc;
		}
	}

	for (auto it = freq.rbegin(); it != freq.rend(); ++it) {
		char ch = it->first;
		int freq1 = it->second;
		if(freq1%2==0)
		{
			for (int i = 0; i < freq1/2; i++) {
				ans += ch;
			}
		}
	}
	cout << ans << endl;

	return 0;
}