#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;  // Input the string
    
    bool isPalindrome = true;
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
        if (s[i] != s[j]) {
            isPalindrome = false;  // Mismatch found, break early
            break;
        }
    }

    if (isPalindrome) {
        cout << "YES\n";  // It's a palindrome
    } else {
        cout << "NO\n";  // It's not a palindrome
    }
    
    return 0;
}
