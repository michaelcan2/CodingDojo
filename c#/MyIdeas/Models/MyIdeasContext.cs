using Microsoft.EntityFrameworkCore;

namespace MyIdeas.Models{
    public class MyIdeasContext:DbContext{
        public MyIdeasContext(DbContextOptions<MyIdeasContext> options):base(options){}
	    public DbSet<User> users { get; set; }
        public DbSet<Post> posts {get; set;}
        public DbSet<Like> likes {get; set;}
    }
}
