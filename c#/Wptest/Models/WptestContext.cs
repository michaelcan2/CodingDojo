using Microsoft.EntityFrameworkCore;

namespace Wptest.Models{
    public class WptestContext:DbContext{
        public WptestContext(DbContextOptions<WptestContext> options):base(options){}
	    public DbSet<User> Users { get; set; }

        public DbSet<Wedding> Wedding { get; set; }
    }
}
