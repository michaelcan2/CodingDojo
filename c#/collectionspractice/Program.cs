using System;
using System.Collections.Generic;


namespace collectionspractice
{
    class Program
    {
        static void Main(string[] args)
        {
    
            int[] numbers = {0,1,2,3,4,5,6,7,8,9};
            // curly brackets means the values in the array 
            string[] names = {"Tim", "Martin", "Nikki", "Sara"};

            bool[] tf = {true, false,true,false,true,false,true,false,true,false};

            System.Console.WriteLine(tf[1]);

        List<string> flavors = new List<string>();

        flavors.Add("Cookie");
        flavors.Add("Vinilla");
        flavors.Add("Strawberry");
        flavors.Add("Mocha");
        flavors.Add("Lemon");
System.Console.WriteLine(flavors.Count);
        
Dictionary<string,string> people = new Dictionary<string,string>();

// in thtlist store all the keys vales of the dictionary people.^^
// making a list of the keys from the peoples dictionary 

        
foreach (string name in names){
    people.Add(name,null);
}   
List <string> keys = new List <string>(people.Keys);
// must do this AFTER YOU ADD THE NAMES
Random rand = new Random();   
        
foreach(string key in keys){
  people[key]= flavors [rand.Next(0,flavors.Count)];
//   either pull a number betweeen zero and all of flavors
System.Console.WriteLine(people[key]);
}
foreach(var person in people){
System.Console.WriteLine(person.Key+" "+ person.Value);
}
        
        
        
        }
    }
}
