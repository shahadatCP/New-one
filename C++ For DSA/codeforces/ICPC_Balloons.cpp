#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        int f[26] = {0};
        
        // Count frequencies of each character in the string
        for(int i = 0; i < n; i++) {
            int index = s[i] - 'A';
            f[index] += 1;
        }
        
        int total = 0;
        // Calculate the total based on frequency conditions
        for(int i = 0; i < 26; i++) {
            if(f[i] != 0) {
                if(f[i] > 1) {
                    total += f[i] + 1;  // Add frequency + 1 if more than 1 occurrence
                } else {
                    total += 2;  // Add 2 for characters that appear exactly once
                }
            }
        }
        cout << total << endl;  // Output the result for each test case
    }
    return 0;
}
