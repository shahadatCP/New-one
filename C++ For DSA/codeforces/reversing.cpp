#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;  // Input the number of elements
    int arr[n+3];  // Declare an array with a little extra space for safety

    // Input array elements
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Reverse the array using two pointers
    for(int i = 0, j = n - 1; i < n / 2; i++, j--) {
        swap(arr[i], arr[j]);
    }

    // Output the reversed array
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
