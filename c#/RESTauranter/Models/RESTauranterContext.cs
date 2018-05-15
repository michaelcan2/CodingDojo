using Microsoft.EntityFrameworkCore;
 
namespace RESTauranter.Models
{
    public class ReviewsContext : DbContext
    {
        // base() calls the parent class' constructor passing the "options" parameter along
        public ReviewsContext(DbContextOptions<ReviewsContext> options) : base(options) { }
        public DbSet<Reviews> reviews{get; set;}
        // connecting the database table to the models that you can see.
    }
}
