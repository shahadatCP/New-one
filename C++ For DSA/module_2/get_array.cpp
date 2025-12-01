#include<bits/stdc++.h>
using namespace std;

int* get_array(int n) {
    int* a = new int[n];  // Dynamically allocate memory for an array
    for(int i=0; i<n; i++) {
        cin >> a[i];  // Input values into the array
    }
    return a;  // Return the dynamically allocated array
}

int main() {
    int n;
    cin >> n;  // Read the size of the array

    int* x = get_array(n);  // Get the dynamically allocated array

    // Output the array values
    for(int i=0; i<n; i++) {
        cout << x[i] << " ";  
    }

    delete[] x;  // Free the dynamically allocated memory
    return 0;
}
