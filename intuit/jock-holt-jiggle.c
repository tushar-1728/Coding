#include <stdio.h>

int main(){
    int curr, jock, holt, jiggle;
    scanf("%d", &curr);
    jock = holt = curr / 14;
    if (jock >= 1){
        jiggle = (curr % 14) * 34;
        printf("%d %d %d\n", jock, holt, jiggle);
    }
    else{
        printf("-1 -1 -1\n");
    }
}