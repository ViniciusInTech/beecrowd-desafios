#include <stdio.h>

#define BONUS 0.15

int main(){
    char name[25];
    double salary, sold, total_salary;

    scanf("%s", &name);
    scanf("%lf", &salary);
    scanf("%lf", &sold);

    total_salary = salary + (sold * BONUS);

    printf("TOTAL = R$ %.2lf\n", total_salary);
    return 0;
}