//
// Created by vinicius on 5/21/25.
#include <stdio.h>

int main() {
    int time, seconds, minutes, hours;
    scanf("%d", &time);
    hours = time / 3600;
    time %= 3600;
    minutes = time / 60;
    seconds = time % 60;
    printf("%d:%d:%d\n", hours, minutes, seconds);
    return 0;
}
