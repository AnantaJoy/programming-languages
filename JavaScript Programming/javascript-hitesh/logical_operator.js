// OR(||)
// AND(&&)
// NOT(!)

let leapYear = 2022;

if (leapYear%4==0 && leapYear%100 !=0 || leapYear%400==0) {
    console.log("Leap Year");
}

else{
    console.log("Not a Leap Year");
} 