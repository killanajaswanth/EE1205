#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("date.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     x(n)\n");

    // Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
    for (int n = -10; n <= 10; n++) {
        // Calculate and write to file, set x(n) to 0 if n < 0
        double x_n = (n >= 0) ? 6.25 * (1 + n) : 0.0;
        fprintf(file, "%d %lf\n", n, x_n);
    }

    fclose(file);

    return 0;
}
