#include <stdio.h>

int main(){
    int product_code_0, product_code_1, product_unit_0, product_unit_1;
    double product_price_0, product_price_1, total_product;

    scanf("%d %d %lf", &product_code_0, &product_unit_0, &product_price_0);
    scanf("%d %d %lf", &product_code_1, &product_unit_1, &product_price_1);

    total_product = (product_unit_0 * product_price_0) + (product_unit_1 * product_price_1);
    printf("VALOR A PAGAR: R$ %.2lf\n", total_product);

    return 0;
}