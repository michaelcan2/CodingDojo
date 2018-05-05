using System;

namespace first_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("It worked!!!");

           int favoriteNum=9;
           Console.WriteLine("You can Print numbers...");
           Console.WriteLine(favoriteNum);
           Console.WriteLine("the {0} cow, jumped over the {1}, {2} times!", "brown", "Moon", 8);

       
for (int i =1; i<255; i++)
{
    System.Console.WriteLine(i);
}


for(int j=1; j<100; j++)
{
    if(j%3==0 && j%5==0)
    {
        continue;
    } else if(j%5==0 || j%3==0)
    {
        System.Console.WriteLine(j);
    }
}

 void num1()
  {
   for(int i = 1; i <= 255; i++)
   {
     Console.WriteLine(i);
   }
  }






        }
    }
}
