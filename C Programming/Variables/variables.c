#include <stdio.h>
#include <string.h>

int main() {
    int num1 = 21;
    int num2 = 3;
    printf("21 - 3 = %d\n",num1,num2,+num2);
    num1 = 30;
    printf("%d - %d = %d\n",num1,num2,num1+num2);
    //char user_name = "Rahim";
    //printf("%c",user_name);
    char msg[] = "Happy Birthday";
    printf(msg);
    return 0;
}
