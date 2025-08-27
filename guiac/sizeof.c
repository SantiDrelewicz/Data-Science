#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

int main(){
    char c = 'a';
    int n = 1;
    long l = 10000;

    printf("%lu: %d \n", sizeof(c),c);
    printf("long(%lu): %ld \n", sizeof(l),l);
}