#include<stdio.h>

int main(){
    int sum=0;
    int n=1 ;
    while(n<=50){

        sum=sum+n;
        n = n + 2;
        printf("%i\n",sum);
    }
    printf("%i",sum);

}
