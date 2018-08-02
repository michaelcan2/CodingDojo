using Microsoft.EntityFrameworkCore;


   namespace login.Models
{
    public class logincontext : DbContext
    {
        // base() calls the parent class' constructor passing the "options" parameter along
        public logincontext(DbContextOptions<logincontext> options) : base(options) { }
        // all logincontext must match name of contet file

    public DbSet<User> users { get; set; }
    // above the User will be made in models and users is the name of the table in our database.
}
}
