#include <string.h>
#include <stdlib.h>

char* appendAndDelete(char* s, char* t, int k) {
    char *res = (char*)calloc(4, sizeof(char));
    int slen = strlen(s);
    int tlen = strlen(t);
    if(k >= slen+tlen){
        strcpy(res, "Yes");
    }
    else{
        int min, max, target;
        int count = 0;
        if(slen < tlen){
            min = slen;
            max = tlen;
        }
        else{
            min = tlen;
            max = slen;
        }
        for(int i = 0; i <= min; ++i){
            if(s[i] == t[i])
                ++count;
            else
                break;
        }
        target = 2*(min-count) + max-min;
        if(k >= target && (k-target)%2 == 0)
            strcpy(res, "Yes");
        else
            strcpy(res, "No");
    }
    return res;
}