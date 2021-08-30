#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    //input from the file
    ifstream input_file("InFile.txt", ios::in);
    char ch;
    input_file>>ch;
    float x;
    input_file>>x;
    cout<<x<<" "<<ch;
   
    //output from the file
    ofstream output_file("OutFile.txt",ios::out);
    output_file<<x;
    output_file<<ch;

    //output roll. no. and marks of a student into a file.
    char ans;
    ofstream fileout;
    fileout.open("Marks.dat", ios::out | ios::app);
    fileout<<"\nRoll No.\tMarks";
    do 
    {
        int rn,mrks;
        cout<<"\nEnter roll no. :";
        cin>>rn;
        cout<<"\nEnter the marks :";
        cin>>mrks;
        fileout<<"\n"<<rn<<"\t"<<mrks;
        cout<<"Add more records? (y/n): ";
        cin>>ans;
    } while(ans=='Y' || ans=='y');
}