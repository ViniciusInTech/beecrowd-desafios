#include <stdio.h>

#define PESO_A 2
#define PESO_B 3
#define PESO_C 5

int main() {
    double A, B, C, average;

    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);

    average = (A * PESO_A + B * PESO_B + C * PESO_C) / (PESO_A + PESO_B + PESO_C);

    printf("MEDIA = %.1lf\n", average);
}