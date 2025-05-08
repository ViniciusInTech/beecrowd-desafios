#include <stdio.h>
#define PI 3.14159

double pow(double x, double b){
    double result = 1.0;
    for(int i = 0; i < b; i++){
        result *= x;
    }
    return result;
}

int main(){
    double A, B, C, right_triangle_area, circle_area,
    trapezium_area, square_area, rectangle_area;

    scanf("%lf %lf %lf", &A, &B, &C);

    right_triangle_area = (A * C)/2;
    circle_area = PI * (pow(C, 2));
    trapezium_area = ((A + B) * C)/2;
    square_area = pow(B, 2);
    rectangle_area = A * B;

    printf("TRIANGULO: %.3lf\n", right_triangle_area);
    printf("CIRCULO: %.3lf\n", circle_area);
    printf("TRAPEZIO: %.3lf\n", trapezium_area);
    printf("QUADRADO: %.3lf\n", square_area);
    printf("RETANGULO: %.3lf\n", rectangle_area);
    return 0;

}