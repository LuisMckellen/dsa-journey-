int maxArea(int* height, int heightSize) {
    int l = 0;
    int r = heightSize - 1;
    int max_water = 0;
    
    while (l < r) {
        int h = height[l] < height[r] ? height[l] : height[r];
        int water = h * (r - l);
        
        if (water > max_water) {
            max_water = water;
        }
        
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }
   
