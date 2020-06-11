void sortColors(int* nums, int numsSize){
    int count[3] = {0,0,0};
    for(int i = 0; i < numsSize; ++i){
        if(nums[i] == 0)
            ++count[0];
        else if(nums[i] == 1)
            ++count[1];
        else if(nums[i] == 2)
            ++count[2];
    }
    int temp = 0;
    int i = 0;
    while(temp < 3){
        while(count[temp]--){
            nums[i++] = temp;
        }
        ++temp;
    }
}