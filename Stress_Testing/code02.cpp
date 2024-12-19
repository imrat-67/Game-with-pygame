#include<bits/stdc++.h>
using namespace std;

int main(){
    string h[9],v[9];

    for(int i=0; i<9; i++)
        for(int j=0; j<9; j++){
            char c; cin>>c;
            h[i] += c;
            v[j] += c;
        }

    auto lamda = [](string s){return set<char>(s.begin(),s.end()).size()==9;};
    if(all_of(h,h+9,lamda) and all_of(v,v+9,lamda)) cout<<"Print Congratulations!"<<endl;
    else cout<<"Oh No!"<<endl;;
}