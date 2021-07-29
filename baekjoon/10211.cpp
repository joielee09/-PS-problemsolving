#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int arr[1002];
        int pSum[1002];
        for(int i=0; i<n; i++){
            int tmp;
            cin>>tmp;
            arr[i]=tmp;
            if(i==0){
                pSum[0]=tmp;
            }
            else{
                pSum[i]=pSum[i-1]+tmp;
            }
        }
        int max_val=INT_MIN;
        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                max_val = max(max_val, pSum[j]-pSum[i]+arr[i]);
            }
        }
        cout<<max_val<<'\n';
    }
    return 0;
};