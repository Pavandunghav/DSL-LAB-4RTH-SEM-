/*Department maintains a student information. The file contains roll number, name,
division and address. Allow user to add, delete information of student. Display
information of particular employee. If record of student does not exist an appropriate
message is displayed. If it is, then the system displays the student details. Use sequential
file to main the data.



*/

#include <iostream>
#include <fstream>

using namespace std;

class info
{
public:
    int roll;
    char name;
    char div;

    void get()
    {
        cout << "\n\n\nENTER THE ROLL NO.  :" << endl;
        cin >> roll;

        cout << "ENTER THE NAME :" << endl;
        cin >> name;

        cout << "ENTER THE DIVISION  :" << endl;
        cin >> div;
    }

    void display()
    {
        fstream f;

        f.open("x.text", ios::in);

        info i1;

        cout << "THIS IS THE DATA OF THE STUDENT :" << endl;

        while (f.read((char *)&i1, sizeof(i1)))
        {

            i1.put();
        }

        f.close();
    }

    void put()
    {

        // cout<<"THIS IS THE DATA OF THE STUDENT :"<<endl;

        cout << "ROLL :" << roll << endl;
        cout << "NAME :" << name << endl;
        cout << "DIVISION :" << div << endl;
    }

    void write()
    {
        fstream f;

        f.open("x.text", ios::out);

        info i1;

        int n;

        cout << "ENTER THE NO. OF THE STUDENTS :" << endl;
        cin >> n;

        for (int i = 0; i < n; i++)
        {

            i1.get();
            f.write((char *)&i1, sizeof(i1));
        }

        // f.write((char*)&i1,sizeof(i1));

        f.close();
    }

    int getroll()
    {

        return roll;
    }

    void search()
    {
        fstream f2;

        int r;
        info i2;

        cout << "ENTER THE ROLL.NO. THAT YOU WANT TO DELETE :";
        cin >> r;

        f2.open("x.text", ios::out);

        while (f2.read((char *)&i2, sizeof(i2)))
        {

            if (i2.getroll() == r)
            {

                i2.put();
                break;
            }
        }

        f2.close();

    }



};

int main()
{

    info i0;

    // for(int i=0;i<=n;i++){

    string flag = "Y";

    while (flag == "Y")
    {

        int ch;

        cout << "1]WRITE \n 2]DISPLAY  \n 3]SEARCH  \n 4]EXIT \n ";
        cout<<"ENTER YOUR CHOICE :";


        cin >> ch;

        switch (ch)
        {

        case 1:
            i0.write();

        case2:
            i0.display();

        case 3:
            i0.search();

        case 4:
            break;
        }

        cout << "DO YOU WANT TO CONTINUE (Y/N)?";
        cin >> flag;
    }

    return 0;
}
