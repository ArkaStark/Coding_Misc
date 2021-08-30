#include<stdio.h>
int sosq(int n)
{
    int d, s=0;
    while(n!=0)
    {
        d=n%10;
        s=s+d*d;
        n=n/10;
    }
    return s;
}

int main()
{
    int i,j,n=1,m;
    printf("Happy Numbers : ");
    for(i=0;i<10;)
    {
        m=n;
        for(j=0;j<100;j++)
        {
            if(m!=1)
            m=sosq(m);
            else
            {
            printf("%d,",n);
            i++;break;
            }
        }
        n++;
    }
    return 0;
}