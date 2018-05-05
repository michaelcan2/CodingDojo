using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            var Artist1 = 
                from artist in Artists 
                where artist.Hometown == "Mount Vernon"
                // give me one artist home town equal Mount Vernon
                select artist;

            foreach(var artist in Artist1)
            {
                System.Console.WriteLine(artist.ArtistName + " " + artist.Age);
            }
            

            //Who is the youngest artist in our collection of artists?
            var youngestArtist = 
                from artist in Artists
                orderby artist.Age ascending
                // go through all the artists 
                select artist;

            var youngest = youngestArtist.Take(1);

            foreach(var artist in youngest)
            {
                System.Console.WriteLine(artist.ArtistName);
            }

            //Display all artists with 'William' somewhere in their real name
            var williams =
            from artist in Artists 
            where artist.RealName.Contains("William")
            select artist;

            foreach(var artist in williams)
            {
                System.Console.WriteLine("The real name of this artist is William(s):" + artist.ArtistName);
            }

            //Display the 3 oldest artist from Atlanta
            var AtlantaOldest =
            from artist in Artists
            where artist.Hometown == "Atlanta"
            orderby artist.Age descending 
            select artist;

            var oldest3 = AtlantaOldest.Take(3);

            foreach( var artist in oldest3)
            {
                System.Console.WriteLine("The oldest artist from Atlanta is " + artist.ArtistName);
            }

            //(Optional) Display the Group Name of all groups that have members that are not from New York City
            var notNy

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
        }
    }
}
