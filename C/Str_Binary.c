#include<stdio.h>
#include<stdlib.h>
int main()
{
    FILE *fs,*ft;
    char s;
    fs=fopen("Sentence.txt","r");
    ft=fopen("RoboLanf.txt","w");
    if(fs==NULL)
    {
        printf("File could not be opened");
        exit(2);
    }
    if(ft==NULL)
    {
        printf("File could not be opened");
        exit(3);
    }
    while()
    {
        s=fgetc(fs);
        if(s==EOF)
            break;
        int c=-1,bi[100],n;
        n=(int)s;
        
        while(n>=0)
        {
            ++c;
            bi[c]=n%2;
            n=n/2;
        }
        for(;c>=0;c--)
            printf("%d",bi[c]);
    }
    fclose(fs);
    return 0;
}