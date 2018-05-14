using System.Collections.Generic;
using System.Linq;
using Dapper;
using System.Data;
using MySql.Data.MySqlClient;
using DojoLeague.Models;
using System;
// I manually added, using System

namespace DojoLeague.Factory{
    // factories only contain query functions which we connect to our controller
    public class DojoLeagueFactory:IFactory<Dojo>{
        // change the dojo title from dojo league to dojo that was next to ifactory
        // because mandycan made the model title the sameas the namespace which 
        // cannot happen.
        // 
        private string info;

        public DojoLeagueFactory(){
            info = "server=localhost;userid=root;password=root;port=3306;database=DojoLeague;SslMode=None";
            // change the database name to DojoLeague
        }

        internal IDbConnection Connection{
            get{
                return new MySqlConnection(info);
            }
        }

        public void AddDojo(Dojo item){
            // had to change from auto dojo to dojoleague
            using (IDbConnection dbConnection = Connection){
                string query =  "INSERT INTO Dojo (Name,Location,Information) VALUES (@Name, @Location, @Information)";
                dbConnection.Open();
                dbConnection.Execute(query, item);
            }
        }

        public void AddNinja(Ninja item){
            // had to change from auto dojo to dojoleague
            using (IDbConnection dbConnection = Connection){
                string query =  "INSERT INTO Ninja (Name,Description,level) VALUES (@Name, @Description, @level)";
                dbConnection.Open();
                dbConnection.Execute(query, item);
            }
        }


        public IEnumerable<Dojo> FindAll(){
            using (IDbConnection dbConnection = Connection){
                dbConnection.Open();
                return dbConnection.Query<Dojo>("SELECT * FROM DojoLeagues");
                // had to change from auto dojo to dojoleague
            }
        }

        public Dojo FindByID(int id){
            using (IDbConnection dbConnection = Connection){
                dbConnection.Open();
                return dbConnection.Query<Dojo>("SELECT * FROM DojoLeagues WHERE id = @Id", new { Id = id }).FirstOrDefault();
                // had to change from auto dojo to dojoleague
            }
        }
    }
}
