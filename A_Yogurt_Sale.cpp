#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    while(n--){
        int a,b,c;
    cin>>a>>b>>c;
    int ans=0;
    if(b*2 >c){
        int tmp = a/2;
        if(a%2==0){
            
            ans+= (tmp*c);
        }
        else{
            ans+= (tmp*c)+b;
        }
    }
    else{
        ans+=(a*b);
    }
    cout<<ans<<endl;
    }
    return 0;
}