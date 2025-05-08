#include <stdio.h>

int abs(int x) {
    return x < 0 ? -x : x;
}

int main() {
    int a, b, c, greatest;
    scanf("%d %d %d", &a, &b, &c);

    greatest = a > b ? a : b;
    greatest = greatest > c ? greatest : c;

    printf("%d eh o maior\n", greatest);
    return 0;
}
