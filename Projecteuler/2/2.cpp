//KOTU ZAMAN KARMASIKLIGI OLAN COZUM

#include <iostream>
using namespace std;

int fibo(int n){
    
    if(n <=0 )
        return 0;
    else if( n == 1)
        return 1;
        
    return fibo(n-1) + fibo(n-2);
    
}

int main() {

    int toplam = 0;
    int sonuc = 0;
    
    for(int i = 0; sonuc < 4000000; i++ )
    {
        sonuc = fibo(i);
        
        if(sonuc%2 == 0)
        {
            toplam +=sonuc;
            cout<<"\nfib("<< i <<") = "<< sonuc << " -> "<<toplam;
        }
    }
    
    cout<<"\nsonuc: "<<toplam;
    
    return 0;
}
