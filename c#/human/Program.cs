using System;

namespace human
{
    public class Human 
    {
    public string name;
    public int strength = 3;
    public int intelligence = 3;
    public int dexterity = 3; 
    public int health = 100;

    public Human(string person)
    {
        name = person;
        // name on left is string name
    }

    public Human (string n, int s, int i, int d, int h)
    {
    name = n;
     strength=s;
     intelligence=i;
     dexterity=d;
     health=h;

    }
    public void Attack(Human Mike)
    {
        Mike.health -= 5 * this.strength;
        // the health is minus this 
    }
    // function
     }

    public class Wizard : Human 
    {
       public Wizard(string name) : base(name, 3,25,3,50)
       {

       }
        public void Heal(Wizard Josh)
        {
            Josh.intelligence += 10 * this.intelligence;
        }
     
    }
    

    // method overloading you have name and then it will default its own weapons
    class Program
    {

        static void Main(string[] args)
        {
            Human Mike = new Human("Mike");
            Human Konrad = new Human("Konrad");
            Human Tony = new Human("Tony", 10,1,2,150);

            Konrad.Attack(Mike);
            System.Console.WriteLine($"{Mike.name} was attacked by {Konrad.name}, His Health is now:{Mike.health}");
            
            Wizard Josh = new Wizard("Josh");
            System.Console.WriteLine(Josh.health);

            Wizard Harry = new Wizard("Harry");
            System.Console.WriteLine(Harry.name);
            System.Console.WriteLine(Harry.intelligence);
            // prints 25

            Josh.Heal(Josh);
            System.Console.WriteLine(Josh.intelligence);

        //    main is where you call the humans 
        // call your functions and make the people in name.
        }
    }
}
