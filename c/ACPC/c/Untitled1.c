
// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
#include <cmath>
int main() {
    int a,b,c;
    cin>>a>>b>>c;
    if(a>6 || a<2){
        cout<<max(b,c);
    }
    else if(b>6 || b<2){
        cout<<max(a,c);
    }
    else if(c>6 || c<2){
        cout<<max(a,c);
    }
    else {
        cout<<max(max(b,c),a);
    }
    return 0;
}
