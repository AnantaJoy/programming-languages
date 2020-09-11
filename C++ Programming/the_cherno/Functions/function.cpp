#include <iostream>
using namespace std;

int Multiply(int x,int y) {
    return x*y;
}

int main(int argc, char const *argv[])
{
    cout << "Multiplication of 2 and 4 is: ";
    int z = Multiply(2,4);
    cout << z <<endl;
    return 0;
}
