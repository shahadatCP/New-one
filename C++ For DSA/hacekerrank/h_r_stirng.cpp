#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string a, b;
    getline(cin, a);
    getline(cin, b);
    int a_sz = a.size();
    int b_sz = b.size();
    cout << a_sz << " " << b_sz << endl;
    cout << a + b << endl;
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;
    
    cout << a << " " << b << endl;
    return 0;
}
