#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for(int i=0; i<t; i++)
	{
		int n, sum;
		cin >> n >> sum;
		int arr[n];
		if(n<3)
		{
			cout << "NO\n";
			continue;
		}
		for(int i=0; i<n; i++)
		{
			cin >> arr[i];
		}
		sort(arr,arr+n);
		bool found = false;

		for(int i=0; i<n-2; i++)
		{
			int left = i+1, right = n-1;

			while(left<right)
			{
				int new_sum = arr[i] + arr[left] + arr[right];
				if(new_sum == sum)
				{
					found = true;
					break;
				}
				else if(new_sum < sum)
				{
					left++;
				}
				else
				{
					right--;
				}
			}

			if(found)
			{
				break;
			}
		}

		if(found)
		{
			cout << "YES\n";
		}
		else {
			cout << "NO\n";
		}

	}
	return 0;
}