// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>

using namespace std;



long int primeFactory(long int sayi){
    
    long int enBuyuk = 1;
    long int orjSayi = sayi;
    long int bolen = 2;
    
    do{
        if(sayi % bolen == 0){
            
            sayi = sayi / bolen;
            
            cout<<"Bolundu "<<bolen<<" = "<<sayi<<"\n";
            
            if(bolen > enBuyuk)
                enBuyuk = bolen;
            
        }else if(bolen != 2){
            bolen +=2;
        }else{
            bolen += 1;
        }
        
    }while(bolen < sqrt(orjSayi));
    
    return enBuyuk;
}

int main() {
    
    cout<<"En buyuk: \n"<<primeFactory(600851475143); //600851475143
    
    return 0;
    
}
