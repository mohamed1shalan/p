#include <iostream>

using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    int a,b,c;
    cin>>a>>b>>c;
    if(a<6 || a>2){
        cout<<max(b,c);
    }
    else if(b<6 || b>2){
        cout<<max(a,c);
    }
    else{
        cout<<max(b,a);
    }
    return 0;
}
