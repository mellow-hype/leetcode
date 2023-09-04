#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>


// merge and sort two arrays
void merge(int* nums1, int nums1_arrsize, int nums1Size, int* nums2, int nums2Size, int n){
    // merge
    for (int i = 0; i < nums2Size; i++) {
        nums1[nums1Size + i] = nums2[i];
    }

    int other;
    for (int i = 1; i < nums1_arrsize; i++) {
        while (nums1[i] < nums1[i-1]) {
            other = nums1[i-1];
            nums1[i-1] = nums1[i];
            nums1[i] = other;
            if (i > 1)
                i--;
        }
    }
}


void do_testcase_2() {
    int EXPECTED[] = {1};
    int LIST1[] = {0};
    int arr1_size = sizeof(LIST1) / sizeof(int);
    int LIST2[] = {1};
    int arr2_size = sizeof(LIST2) / sizeof(int);

    int *l1 = malloc(arr1_size * sizeof(int));
    memcpy(l1, LIST1, arr1_size * sizeof(int));

    int *l2 = malloc(arr2_size * sizeof(int));
    memcpy(l2, LIST2, arr2_size * sizeof(int));

    merge(l1, arr1_size, 0, l2, arr2_size, arr2_size);

    for (int i = 0; i < arr1_size; i++) {
        assert(EXPECTED[i] == l1[i]);
    }
    printf("testcase 2 PASSED\n");
    free(l1);
    free(l2);
}

void do_testcase_1() {
    int EXPECTED[] = {1, 2, 2, 3, 5, 6};
    int LIST1[] = {1, 2, 3, 0, 0, 0};
    int arr1_size = sizeof(LIST1) / sizeof(int);
    int LIST2[] = {2, 5, 6};
    int arr2_size = sizeof(LIST2) / sizeof(int);

    int *l1 = malloc(arr1_size * sizeof(int));
    memcpy(l1, LIST1, arr1_size * sizeof(int));

    int *l2 = malloc(arr2_size * sizeof(int));
    memcpy(l2, LIST2, arr2_size * sizeof(int));

    merge(l1, arr1_size, 3, l2, arr2_size, arr2_size);

    for (int i = 0; i < arr1_size; i++) {
        assert(EXPECTED[i] == l1[i]);
    }

    printf("testcase 1 PASSED\n");
    free(l1);
    free(l2);
}


int main() {
    do_testcase_1();
    do_testcase_2();
    return 0;
}
