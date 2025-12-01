#include <iostream>
#include <stack>
using namespace std;

stack<int> st1, st2;
if(st1.size() != st2.size()) {
    cout << "NO\n";
    return 0;
}

while(!st1.empty()) {
    if(st1.top() != st2.top()) {
        cout << "NO\n";
        return 0;
    }
    st1.pop();
    st2.pop();
}
cout << "YES\n";
