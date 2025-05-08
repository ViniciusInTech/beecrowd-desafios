#include <stdio.h>

int main(){
    int distance;
    float spent_fuel;

    scanf("%d", &distance);
    scanf("%f", &spent_fuel);

    printf("%.3f km/l\n", distance/spent_fuel);
    return 0;
}