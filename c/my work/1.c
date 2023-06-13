
#include <stdio.h>
/*int main()
{       float x, y, sum;
        printf("please inter value 1\n");
        scanf("%f", &x );
        printf("please inter value 2\n");
        scanf("%f", &y );
        sum= x + y ;
        printf( "result= %4.1f", sum);
        getch();
}*/

/*int main()
{
    int max=0 ;

    if (max==0){
        printf("max= %i",max);
        max = max + 1 ;
    };

    return 0;
}*/

/*int main(){

    int  use='1' , pas=15 ;
    int  usee ,  pase ;

    printf("enter use : ");
    scanf("%i",&usee);

    printf("enter pas : ");
    scanf("%i",&pase);

    if (use==usee && pas==pase){
        printf("yas");
    }

    else{
        printf("no");
    };
}*/

/*int main(){

    float sum,sub,mul,x, y,div ;
    char c ;
    printf("enter x valre :");
    scanf(" %f" , &x);
    printf("enter y valre :");
    scanf(" %f" , &y);
    sum = x + y;
    sub = x - y;
    mul = x * y;
    div = x / y;

    float sumr1 , subr1 , mulr1, divr1 ;
    float sumr2 , subr2 , mulr2, divr2 ;
    int mem1=0 ;
    int mem2=0 ;

    printf("mem1\n");

    printf("plese enter the sum : \n");
    scanf(" %f",&sumr1);
    if(sumr1==sum){
        mem1=mem1+1 ;
    }else{};

    printf("plese enter the subtarctr : \n");
    scanf(" %f",&subr1);
    if(subr1==sub){
        mem1= mem1 + 1 ;
    }else{};

    printf("plese enter the multiply : \n");
    scanf(" %f",&mulr1);
    if(mulr1==mul){
        mem1= mem1 + 1 ;
    }else{};

    printf("plese enter the division : \n");
    scanf(" %f",&divr1);
    if(divr1==div){
        mem1= mem1 + 1 ;
    }else{};



    printf("mem2\n");
    printf("plese enter the sum : \n");
    scanf(" %f",&sumr2);
    if(sumr2==sum){
        mem2= mem2 + 1 ;
    }
    else{};

    printf("plese enter the subtarctr : \n");
    scanf(" %f",&subr2);
    if(subr2==sub){
        mem2= mem2 + 1 ;
    }else{};

    printf("plese enter the multiply : \n");
    scanf(" %f",&mulr2);
    if(mulr2==mul){
        mem2= mem2 + 1 ;
    }else{};

    printf("plese enter the division : \n");
    scanf(" %f",&divr2);
    if(divr2==div){
        mem2= mem2 + 1 ;
    };
    if(mem1>mem2){
        printf("\nwiner is member1\n");
    }
    else{
       if(mem1==mem2){
        printf("\ncompetitors are equal\n");
       }
       else{
            printf("\nwiner is member2\n");
       };
    };

    printf("\nresult of member1 =%i/4\n",mem1);
    printf("result of member2 =%i/4\n",mem2);

    printf("\nvalue of sum = %.2f \n",sum );
    printf("value of subtarctr = %.2f \n",sub );
    printf("value of multiply = %.2f\n",mul );
    printf("value of division = %.2f\n",div );

    printf("c:");
    scanf(" %c",&c );
    switch(c)
    {
        case'a':
            printf("good choice (a)");
            break;

        case'c':
            printf("good choice (c)");
            break;

        default:
            printf("ooops");
            break;
    }

    double i;
    i=2;
    while(i>-10){
        printf("%lf\n", i);
        i= i *1.01;
    };

    char array_mo[7] = "mohamed";
    printf("%s",array_mo);

    return 0;
}
*/

int main()
{

    /*
    int degree ;
    printf("enter your degree :");
    scanf("%i",&degree);
    if (degree>=85 && degree<=100){
            printf("excllant");
    }
    else if(degree>=75 && degree<85 ){
        printf("very good");
    }
    else if(degree>=65 && degree<75 ){
        printf("good");
    }
    else if(degree>=50 && degree<65 ){
        printf("pass");
    }
    else{
        printf("fall");
    }
*/
    int f, fl;
    printf("enter the final salary :");
    scanf("%i", &f);
    if (f >= 5000)
    {
        printf("we will add a tax : 20% \n");
        fl = f - f * 0.2;
        printf("final value is : %i", fl);
    }
    else if (f < 5000 && f >= 3000)
    {
        printf("we will add a tax : 10% \n");
        fl = f - f * 0.1;
        printf("final value is : %i", fl);
    }
    else if (f < 3000)
    {
        printf("we will add a tax : 5%\n");
        fl = f - f * 0.05;
        printf("final value is : %i", fl);
    }
    return 0;
}
