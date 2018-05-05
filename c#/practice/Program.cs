using System;

namespace practice
{
    class Program
    {
        static void Main(string[] args)
        {

          Vehicle myCar = new Vehicle();
          System.Console.WriteLine(myCar.numPassenger);
        
        
        } 
        public class Vehicle{
            public int numPassenger = 4;
        }




    
    }


}
