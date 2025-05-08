#include <stdio.h>

#define PI 3.14159

double pow(double x, int y) {
    double result = x;
    for (int i=1; i < y; i++) {
        result = result * x;
    }
    return result;
}

int main(){
    double r, volume_sphere;

    scanf("%lf", &r);

    volume_sphere = (4.0/3.0) * PI*pow(r, 3);
    printf("VOLUME = %.3lf\n", volume_sphere);
    return 0;
}