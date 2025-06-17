#include <stdio.h>
#include "comp2.h"

int main() {
    int num1 = 10, num2 = 20;
    printf("Result of %d + %d = %d\n", num1, num2, comp2_add(num1, num2));
    return 0;
}
