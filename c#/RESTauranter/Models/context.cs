using Microsoft.EntityFrameworkCore;
 
namespace RESTauranter.Models
// I changed the namespace
{
    public class RESTauranterContext : DbContext
    // I changed from YourContext
    {
        // base() calls the parent class' constructor passing the "options" parameter along
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
    }
}
