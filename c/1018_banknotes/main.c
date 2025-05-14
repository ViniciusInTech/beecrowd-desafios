//
// Created by vinicius on 5/14/25.
//

#include <stdio.h>

int main() {
    int value, bill_100, bill_50, bill_20, bill_10,
    bill_5, bill_2, bill_1;

    scanf("%d", &value);

    bill_100 = value / 100;

    printf("%d\n", value);
    printf("%d nota(s) de R$ 100,00\n", bill_100);
    value = value % 100;
    bill_50 = value / 50;

    printf("%d nota(s) de R$ 50,00\n", bill_50);
    value = value % 50;

    bill_20 = value / 20;
    printf("%d nota(s) de R$ 20,00\n", bill_20);
    value = value % 20;

    bill_10 = value / 10;
    printf("%d nota(s) de R$ 10,00\n", bill_10);
    value = value % 10;

    bill_5 = value / 5;
    printf("%d nota(s) de R$ 5,00\n", bill_5);
    value = value % 5;

    bill_2 = value / 2;
    printf("%d nota(s) de R$ 2,00\n", bill_2);
    value = value % 2;

    bill_1 = value / 1;
    printf("%d nota(s) de R$ 1,00\n", bill_1);
    value = value % 1;
    return 0;
}
