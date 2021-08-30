#include<stdio.h>
int main()
{
    FILE *fs,*ft;
    char s[100];
    int c=0;
    fs=fopen("Input.txt","r");
    ft=fopen("Desolation.txt","w");
    if(fs==NULL)
    {
        printf("Input File could not be opened");
        exit(1);
    }
    if(ft==NULL)
    {
        printf("Output File could not be opened");
        exit(2);
    }
    while(fgets(s,99,fs)!=NULL)
    {
        fputs(s,ft);
        c++;
        if(c==6)
        {
            fputs("\n",ft);
            c=0;
        }
    }
    fputs("\n\n\t\t\t-Bob Dylan",ft);
    fclose(ft);
    fclose(fs);
    return 0;
}