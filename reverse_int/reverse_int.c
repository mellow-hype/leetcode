#include <stdio.h>
#include <math.h>
#include <time.h>

#define MAX_32 2147483647
#define MIN_32 -2147483648
#define MAX_NUM_STR 11

int reverse(int x) {
    int final_reversed_int = 0;
    int negate = 1;
    char int_string[MAX_NUM_STR];    // 11 because max int32 is 10 digits long, +1 for the null byte terminator

    printf("input number: %d\n", x);

    // if the number is negative, convert it to a positive
    if (x < 0) {
		if (x == MIN_32) { x++; }
        x = x * -1;
        negate = -1;
    }

    // convert the number to it's string representation
    int num_len = snprintf(int_string, MAX_NUM_STR, "%d", x)-1;
    if (num_len+1 == MAX_NUM_STR) {
        return 0;
    }

    // use the length of the str version and count down, so we start with the last digit in the str and work
    // backwards to reverse the outcome as we iterate
    int num_power = 0;
    for (;num_len > -1; num_len--) {
        // convert char version of number into an int by subtracting 0x30 (assuming std ascii)
        // curr_num * 10^num_len accounts for the digit's place, i.e. a 3 digit number is in the hundreds, so the first
        // digit is multiplied to it's hundreds version, the second is multiplied to it's tens version, etc.
        num_power = ((int_string[num_len] - 0x30) * ((pow(10, num_len))));
		if (num_power < 0) {
			return 0;
		}
        // if we would overflow a signed 32-bit int, just return 0
        if (MAX_32 - final_reversed_int < num_power) {
            return 0;
        }
        final_reversed_int += num_power;
    }

	if (final_reversed_int == MAX_32 && negate == -1) {
    	return (final_reversed_int * negate) - 1;
	}
    return final_reversed_int * negate;
}

int main() {
    int test_nums[6] = {120, 644, -34, 1534236469, MAX_32, MIN_32};
    int result;
    for (int i = 0; i < 6; i++) {
        clock_t tic = clock();
        result = reverse(test_nums[i]);
        clock_t toc = clock();
        printf("reversed: %d\n", result);
        printf("Elapsed: %f seconds\n\n", (double)(toc - tic) / CLOCKS_PER_SEC);
    }
    return 0;
}
