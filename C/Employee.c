#include<stdio.h>
int main()
{
    struct em{
        long id;
        int age;
        char name[10],gen,doj[10];

    };
    struct em *emp;
    int i;
    printf("ID, Name, Age, Gender, Date of joining\n");
    for(i=0;i<5;i++)
    scanf("%ld%s%d%c%s",&emp[i]->id,emp[i]->name,&emp[i]->age,&emp[i]->gen,emp[i]->doj);
    printf("\n Details :\n\n");
    for(i=0;i<5;i++)
    printf("Name : %s\tDate of joining : %s\n",emp[i]->name,emp[i]->doj);
    return 0;
}