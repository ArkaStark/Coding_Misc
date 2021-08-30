#include<stdio.h>
#include<string.h>
int main()
{
    int T,i,j;
    char *N[i];
    scanf("%d",&T);
    for(i=0;i<T;i++)
    scanf("%s",&N[i]);
    for(i=0;i<T;i++)
    {
        int m=0;
        while(*N[i]!='\0')
        {
            switch(*N[i])
            {
                case '0' : m+=6;break;
                case '1' : m+=2;break;
                case '2' : m+=5;break;
                case '3' : m+=5;break;
                case '4' : m+=4;break;
                case '5' : m+=5;break;
                case '6' : m+=6;break;
                case '7' : m+=3;break;
                case '8' : m+=7;break;
                case '9' : m+=6;
            }
            *N[i]++;
        }
        for(j=0;j<m/2;j++)
        printf("%d*",1);
        printf("\n");
    }
    return 0;
}