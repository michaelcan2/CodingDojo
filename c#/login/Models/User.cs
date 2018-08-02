using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace login.Models
{
    public abstract class BaseEntity{
      public DateTime created_at{get; set;}
        // datetime is a built in method in the database you have actual time 
        // viewbag and datetime maybe enitymethods
        public DateTime updated_at{get; set;}
    }
    public class User : BaseEntity{
        [Key]
        public int userID{get; set;}
        public string first_name {get; set;}
        // public string email{get; set;}
        // public string password{get; set;}
        // all lower CASE!!!
        public User(){
            created_at= DateTime.Now;
            updated_at= DateTime.Now;
        }

      

    }
}