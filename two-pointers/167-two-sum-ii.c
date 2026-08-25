#include <stdlib.h>

int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    int l = 0;
    int r = numbersSize - 1;
    
    while (l < r) {
        int total = numbers[l] + numbers[r];
        if (total == target) {
            result[0] = l + 1;
            result[1] = r + 1;
            return result;
        } else if (total < target) {
            l++;
        } else {
            r--;
        }
    }
    
    *returnSize = 0;
    free(result);
    return NULL;
}
