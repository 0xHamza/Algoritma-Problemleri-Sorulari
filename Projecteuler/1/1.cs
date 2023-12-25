using System;

class HelloWorld 
{  
  static void Main(){
      int x;
      int sum = 0;
      for(x = 0; x <=1000; x++){
          if(x%5 == 0 || x%3 == 0){
            sum += x;  
        }
      }
    Console.WriteLine(sum);
  }
}
