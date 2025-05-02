#include <stdio.h>

#define PESO_A 3.5
#define PESO_B 7.5

int main() {
    double A, B, MEDIA;

    scanf("%lf", &A);
    scanf("%lf", &B);

    MEDIA = (A * PESO_A + B * PESO_B) / (PESO_A + PESO_B);

    printf("MEDIA = %.5lf\n", MEDIA);
    return 0;
}