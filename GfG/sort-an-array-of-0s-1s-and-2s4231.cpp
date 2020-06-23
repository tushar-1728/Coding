// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
void sort012(int[],int);

int main() {

    int t;
    cin >> t;

    while(t--){
        int n;
        cin >>n;
        int a[n];
        for(int i=0;i<n;i++){
            cin >> a[i];
        }

        sort012(a, n);

        for(int i=0;i<n;i++){
            cout << a[i]  << " ";
        }

        cout << endl;
        
        
    }
    return 0;
}

// } Driver Code Ends


void sort012(int a[], int n)
{
	int b, c, d, i;
    b = c = d = 0;
    for (i = 0; i < n; ++i){
    	if(a[i] == 0)
    		++b;
    	else if(a[i] == 1)
    		++c;
    	else if(a[i] == 2)
    		++d;
    }
    i = 0;
    while(b--){
    	a[i] = 0;
    	++i;
    }
    while(c--){
    	a[i] = 1;
    	++i;
    }
    while(d--){
    	a[i] = 2;
    	++i;
    }
}