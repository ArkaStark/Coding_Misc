/* This program is on the functioning of an elevator system. The user must enter the number of floors of an apartment and the program will run for 
   5 minutes and randomly generate requests to travel from one floor to another. The Elevator program determines the movement of the elevator efficiently
   The consideration is that the elevator takes 1sec to move from one floor to the next. And it takes 2sec to stop and open it's doors on a particular 
   floor and 0.5 extra sec for each person that boards the elevator on that floor.
*/

#include<iostream>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;
int main()
{
    const int beginTime=clock();
    srand(time(0));
    for(int i=0;i<1000;i++)
        cout<<(int)(rand()/pow(10,8))<<" ";
    cout<<"\n"<<(clock()-beginTime)/CLOCKS_PER_SEC;
}
