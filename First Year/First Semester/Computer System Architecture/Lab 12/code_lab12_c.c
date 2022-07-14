#include <studio.h>

int _min(int x, int y)

int main()
{
    int n=0 , i;
    scanf("%d" ,&n) 'read n'
    int s[n];
    for (i = 0 ; i<n-1 ; i++)
        scanf("%d" ,&s[i]) 'read the numbers'
        
    min = s[0]
    for( i = 0 ; i< n - 1; i++)
        min = _min(min,s[i])
    printf("%d\n" , min)
}