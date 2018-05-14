using FinalTest.Models;
using System.Collections.Generic;
using System.Linq;
using Dapper;
using System.Data;
using MySql.Data.MySqlClient;
// this is where your query go.
namespace FinalTest.Factory{

    public class TrailFactory{
        // THIS is the information that I will use to coneect to the database I creat n mySQL workbench.


        string Server = "localhost";
        // name of your mysqlworkbench
        // must be double quotes
        string Port = "3306";
        string Database = "Trails";
        string User = "root";
        string Password ="root";
        private string connectionString;
        public TrailFactory()
        // this is the constructor function so everytime a trailfactory is created this will import
        // this information into it. 
        {
            connectionString = $"server={Server};userid={User};password={Password};Port={Port};database={Database};SslMode=None";
        }
       internal IDbConnection Connection
        {
            get {
                return new MySqlConnection(connectionString);
                // take this constuctor informationa and return to me the database assoated to Trail factory.
            }
        }
        public void Add(woodsTrails item){
            using(IDbConnection dbConnection = Connection){
                string query = "INSERT INTO Trails (Name,Description,Length,Elevation,Latitude,Longitude) VALUES (@Name,@Description,@Length,@Elevation,@Latitude, @Longitude)";
                dbConnection.Open();
                dbConnection.Execute(query, item);
            }
        }
        public IEnumerable<woodsTrails> FindAll(){
            using (IDbConnection dbConnection = Connection){
                dbConnection.Open();
                return dbConnection.Query<woodsTrails>("SELECT * FROM Trails");

            }
        }
        public woodsTrails FindByID(int id){
            using (IDbConnection dbConnection = Connection){
                dbConnection.Open();
                return dbConnection.Query<woodsTrails>("SELECT * FROM Trails WHERE id = @id",new{id=id}).FirstOrDefault();
            }
        }

    }
}

//namespace FinalTest.Factory{
//    public interface IFactory<T> where T : BaseEntity{

//    }
//}
