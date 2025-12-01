#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    scanf("%d", &n);
    for (int i = 1; i <= 6 + (n / 2); i++)
    {
        int space = 6 + (n / 2) - i;
        for (int j = 1; j <= space; j++)
        {
            printf(" ");
        }
        int star = (i * 2) - 1;
        for (int j = 1; j <= star; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf(" ");
        }

        for (int j = 0; j < n; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
