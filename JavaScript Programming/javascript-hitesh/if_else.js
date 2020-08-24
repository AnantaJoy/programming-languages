// User account info 
//
let user_account = false;
let user_password;
if(user_account){
    console.log("Enter Your Password:");
    if(user_account=true){
        console.log("Log In Successful.");
    }
    else{
        console.log("Incorrect Password. Try Again.");
    }
}

else{
    console.log("There is no account with this name.");
}

/////////////////////////////
// Find the largest number //
/////////////////////////////

let userInput = 8;
let guessNumber = 7;

if (userInput==guessNumber) {
    console.log("You Win");
}
else{
    console.log("You Lose");
}