#include <stdio.h>
int main() 
{
    int n, m;
    scanf("%d %d", &n, &m);
    int matrix[n][m];
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++) 
        {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    int peakCount = 0;
    
    for (int i = 0; i < n; i++) 
    {
        for (int j = 0; j < m; j++) 
        {
              int isPeak = 1;
            
            if (i > 0 && matrix[i][j] <= matrix[i - 1][j]) 
            {
                isPeak = 0;
            }
            if (i < n - 1 && matrix[i][j] <= matrix[i + 1][j]) 
            {
                isPeak = 0;
            }
            if (j > 0 && matrix[i][j] <= matrix[i][j - 1]) 
            {
                isPeak = 0;
            }
            if (j < m - 1 && matrix[i][j] <= matrix[i][j + 1]) 
            {
                isPeak = 0;
            }
            
            if (isPeak) 
            {
                peakCount++;
                printf("%d %d\n", i + 1, j + 1); 
            }
        }
    }
    
    if (peakCount == 0) 
    {
        printf("0\n");
    } 
    else 
    {
        printf("%d\n", peakCount);
    }