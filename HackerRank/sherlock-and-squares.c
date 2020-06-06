#include <math.h>

// Complete the squares function below.
int squares(int a, int b) {
    int count = 0;
    long temp = sqrt(a);
    long set = temp * temp;
    while(set <= b){
        if(set >= a)
            ++count;
        set += (2*temp + 1);
        ++temp;
    }
    return count;
}
