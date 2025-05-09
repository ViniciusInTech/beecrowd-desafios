//
// Created by vinicius on 5/8/25.
//
#include <stdio.h>
#include <math.h>

int main(){
    double x, y, x_2, y_2, distance;
    scanf("%lf %lf", &x, &y);
    scanf("%lf %lf", &x_2, &y_2);

    distance = sqrt((pow(x_2 - x, 2))+(pow(y_2 - y, 2)));
    printf("%.4lf\n", distance);
    return 0;

}