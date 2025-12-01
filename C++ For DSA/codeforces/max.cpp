#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int arr[n+4];
    for(int i=0; i<n; i++)
    {
        cin >> arr[i];
    }
    int arr_max = 0;
    for(int i=0; i<n; i++)
    {
        arr_max = max(arr_max, arr[i]);
    }
    cout << arr_max << endl;
}