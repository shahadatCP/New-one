#include<bits/stdc++.h>
using namespace std;
char grid[1005][1005];
bool vis[1005][1005];
vector<pair<int,int>> d = {{0,1},{0,-1},{1,0},{-1,0}};
int row, col;
bool valid(int x, int y)
{
  if(x<0 || x>=row || y<0 || y>=col)
    return false;
  return true;
}
void dfs(int si, int sj)
{
  vis[si][sj] = true;
  for(int i=0; i<4; i++)
  {
    int ci = si + d[i].first;
    int cj = sj + d[i].second;
    if(valid(ci,cj) && !vis[ci][cj] && grid[ci][cj] == '.')
    {
      dfs(ci,cj);
    }
  }
}
int main()
{
  cin >> row >> col;
  for(int i=0; i<row; i++)
  {
    for(int j=0; j<col; j++)
    {
      cin >> grid[i][j];
    }
  }
  memset(vis, false, sizeof(vis));
  int count = 0;
  for(int i=0; i<row; i++)
  {
    for(int j=0; j<col; j++)
    {
      if(grid[i][j] == '.')
      {
        if(!vis[i][j])
        {
          count ++;
          dfs(i,j);
        }
      }
    }
  }
  cout << count << endl;
  return 0;
}