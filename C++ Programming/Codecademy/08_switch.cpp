#include <iostream>
using namespace std;

int main(){

    double marks;
    cout << "Enter your marks(0-100):";
    cin >> marks;
    int grade = marks/10;
    // cout << grade;
    switch (grade)
    {
    case 10: case 9:case 8:
        cout << "Your GPA is A+";
        break;
    case 7:
        cout << "Your GPA is A";
        break;
    case 6:
        cout << "Your GPA is A-";
        break;
    case 5:
        cout << "Your GPA is B";
        break;
    case 4:
        cout << "Your GPA is C";
        break;
    default:
        cout << "You Failed. Try Next time";
        break;
    } 

}
/////////////////////
/// Grade or CGPA //
///////////////////