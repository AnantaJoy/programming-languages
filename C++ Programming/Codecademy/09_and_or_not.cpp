///////////////////////////////
// Truth Table
//  Turn on and off light
//leap year or not
///////////////////////////////
#include <iostream>

int main() {
  
  int year;
  std::cout << "Enter a year: ";
  std::cin >> year; 
  if(year % 4 == 0 && year % 100 !=0 || year % 400==0)
  {
      std::cout << "Leap Year";
  }
  else
  {
    std::cout << "Not a Leap Year\n";
  }

} 