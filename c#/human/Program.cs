using System;

namespace human
// have the name space and the class be a different name
{
    public class Human 
    // dont save your project as the same name as the class your going to make
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
    public void Attack(Human Enemy)
    {
        Enemy.health -= 5 * this.strength;
        // the health is minus this 
    }
    // function
     }

    public class Wizard : Human 
    {
       public Wizard(string name) : base(name, 3,25,3,50)
       {

       }
        // public void Heal(Wizard Josh)
        // {
        //     Josh.intelligence += 10 * this.intelligence;
        // here the wizard can help other wizard
        // }

        public void Heal()
        {
            intelligence += 10 * this.intelligence;
            // wizard only heals himself
        }

        public void Fireball(Human Enemy)
        // if its wizard then only hitting wizard but if itsHUMAN you can hurt any object cause they are all humans,,
        {
            Random injury = new Random();
           
           Enemy.health -= injury.Next(20,50);
        }
 
     
    }

    public class Ninja : Human 
    {
        public Ninja(string name) : base (name, 3,3,175,100)
        {

        }

        public void steal()
        {
            this.health += 10;
            // this health means the health of the ninja you are making that you have stated above, all ninjas health will be increase
            // by 10 when stealing.
        }

        public void get_away()
        {
            this.health -= 15;
        }


    }

    public class Samurai : Human
    {
        public Samurai(string name) : base (name, 3,3,3,200)
        {
            count++;

        }
        public static int count =0; 

        public void death_blow(Human Enemy)
        {
            if(Enemy.health < 50)
            {
                Enemy.health = 0;
                // the curly brackets replace the semicolon when doing it
            }

        }
        public void meditate()
        {
            health = 200;
        }

        public void how_many()
        {
            System.Console.WriteLine(count);
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

            // Josh.Heal(Josh);
            // when a wizard heals itself
            Josh.Heal();
            System.Console.WriteLine(Josh.intelligence);

        //    main is where you call the humans 
        // call your functions and make the people in name.

        Josh.Fireball(Mike);
        System.Console.WriteLine(Mike.health);
        Josh.Fireball(Harry);
        System.Console.WriteLine(Harry.health);


        Ninja Rob = new Ninja("Rob");
        Rob.steal();
        System.Console.WriteLine(Rob.health);

        Rob.get_away();
        System.Console.WriteLine(Rob.health);
        
        Samurai Net = new Samurai("net");
        Net.death_blow(Mike);
        System.Console.WriteLine(Mike.health);
        // will only work to people whose health is les then 50 like Mike.

        Net.meditate();
        System.Console.WriteLine(Net.health);

        Net.how_many();

        }
    }
}
