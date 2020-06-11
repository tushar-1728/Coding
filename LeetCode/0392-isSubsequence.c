#include <string.h>
#include <stdio.h>

int isSubsequence(char * s, char * t){
	int slen = strlen(s);
	int tlen = strlen(t);
	int i = 0, j = 0;
	while(i < slen && j < tlen){
		if(s[i] == t[j++])
			++i;
	}
	if(i == slen)
		return 1;
	else
		return 0;
}