//
// Created by vinicius on 5/10/25.
//
#include <stdio.h>

#define GAS_MILEAGE 12

int main() {
    double hours, car_speed;
    double liters;

    scanf("%lf", &hours);
    scanf("%lf", &car_speed);

    liters = (hours * car_speed)/GAS_MILEAGE;
    printf("%.3lf\n", liters);
    return 0;
}