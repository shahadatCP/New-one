#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int* arr = new int[n];
    for(int i=0; i<n; i++)
    {
        cin >> arr[i];
    }
    int m;
    cin >> m;
    int *arr_2 = new int [m];
    for(int i=0; i<n; i++)
    {
        arr_2[i] = arr[i];
    }
    for(int i=n; i<m; i++)
    {
        cin >> arr_2[i];
    }

    for(int i=0; i<m; i++)
    {
        cout << arr_2[i] << " " ;
    }
    return 0;
}