#include <stdlib.h>
#include <string.h>

char* angryProfessor(int k, int a_count, int* a) {
	int count = 0;
	char *res = (char*)calloc(4, sizeof(char));
	for (int i = 0; i < a_count; ++i)
	{
		if(a[i] <= 0)
			++count;
	}
	if(count >= k)
		strcpy(res, "NO");
	else
		strcpy(res, "YES");
	return res;
}