using System.Collections.Generic;
using System.Linq;
using Dapper;
using System.Data;
using MySql.Data.MySqlClient;
using League.Models;

namespace League.Factories{
    public class LeagueFactory:IFactory<League>{
        private string info;

        public LeagueFactory(){
            info = "server=localhost;userid=root;password=root;port=3306;database=yourdb;SslMode=None";
        }

        internal IDbConnection Connection{
            get{
                return new MySqlConnection(info);
            }
        }

        public void Add(League item){
            using (IDbConnection dbConnection = Connection){
                string query =  "INSERT INTO Leagues (field1,field2,field3) VALUES (@field1, @field2, @field3)";
                dbConnection.Open();
                dbConnection.Execute(query, item);
            }
        }

        public IEnumerable<League> FindAll(){
            using (IDbConnection dbConnection = Connection){
                dbConnection.Open();
                return dbConnection.Query<League>("SELECT * FROM Leagues");
            }
        }

        public League FindByID(int id){
            using (IDbConnection dbConnection = Connection){
                dbConnection.Open();
                return dbConnection.Query<League>("SELECT * FROM Leagues WHERE id = @Id", new { Id = id }).FirstOrDefault();
            }
        }
    }
}
