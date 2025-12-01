#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;  // Input size of the array
    vector<int> v(n);
    int sum = 0;

    // Input array elements
    for(int i=0; i<n; i++) {
        cin >> v[i];
    }

    // Check for each element if its consecutive number exists in the array
    for(int i=0; i<n; i++) {
        auto it = find(v.begin(), v.end(), v[i] + 1);
        if(it != v.end()) {
            sum++;  // Increment sum if the consecutive number is found
        }
    }

    cout << sum << endl;  // Output the result
    return 0;
}
