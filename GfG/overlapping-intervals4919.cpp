// { Driver Code Starts
//Initial function template for C++

#include<bits/stdc++.h>
using namespace std;

vector<pair<int,int>> overlappedInterval(vector<pair<int,int>> , int );

// User code will be pasted here

int main()
{
    
    int t;
    cin>>t;
    while(t--)
    {
        vector<pair<int,int> > arr,res;
        int n,x,y;
        cin>>n;

        for(int i=0;i<n;i++)
        {
            cin>>x>>y;
            arr.push_back(make_pair(x,y));
        }
        
        res = overlappedInterval(arr,n);
        
        
        for(int i=0;i<res.size();i++)
            cout << res[i].first << " " << res[i].second << " " ;
            
        cout<<endl;
    }
}
// } Driver Code Ends


//User function template for C++

void merge(vector<pair<int,int>> vec, int l, int m, int r){
    int i = l, j = m+1, k = 0;
    
}

void mergesort(vector<pair<int,int>> vec, int l, int r){
    if(l < r){
        int m = (l+r)/2;
        mergesort(vec, l, m);
        mergesort(vec, m+1, r);
        merge(vec, l, m, r);
    }
}

vector<pair<int,int>> overlappedInterval(vector<pair<int,int>> vec, int n) {
    
}