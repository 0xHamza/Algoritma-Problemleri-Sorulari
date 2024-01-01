using System;
    
    class HelloWorld {
        
        static void Main() {
            int fib0 =0;
            int fib1 =1;
            int sonuc = 0;
            
            for (int fib2 =0; fib2 < 4000000 ;){
                fib2 = fib0 + fib1;
                fib0 =fib1;
                fib1 =fib2;
 
                if(fib2%2 == 0){
                    sonuc = fib2 + sonuc;
                    Console.WriteLine(sonuc);
                }
            }
        }
    }
