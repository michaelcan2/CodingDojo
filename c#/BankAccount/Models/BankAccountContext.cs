  using Microsoft.EntityFrameworkCore;

    namespace BankAccount.Models
    {
        public class BankAccountContext : DbContext
        {
            // base() calls the parent class' constructor passing the "options" parameter along
            public BankAccountContext(DbContextOptions<BankAccountContext> options) : base(options){}
                public DbSet<User> Users { get; set; }
                public DbSet<Transaction> Transactions  { get; set; }
            
        }
    }
