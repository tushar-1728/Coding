#include <stdio.h>

int isPowerOfTwo(int n){
    int count = 0;
    while(n > 0){
        count += (n&1);
        n = n>>1;
    }
    if(count == 1)
        return 1;
    else
        return 0;
}

int main(){
    printf("%d\n", isPowerOfTwo(5));
}