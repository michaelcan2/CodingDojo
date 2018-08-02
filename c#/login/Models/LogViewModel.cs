using System;
using System.ComponentModel.DataAnnotations;

namespace login.Models{
    public class LogViewModel: BaseEntity{
    
         [Required]
         [EmailAddress]
        //  means needs email regular stuff
        [Display(Name="Email Address")]
         public string email{get; set;}
         [Required]
         [MinLength(8, ErrorMessage="Your name must contain atleast 8 characters.")]
         [Compare("cw_password", ErrorMessage="Passwords don't match.")]
         [DataType(DataType.Password)]
        //  ^^above will make your letters turn to dots
         [Display(Name="Password")]

        public string password{get; set;}
        [Required]
        // compare is method
        [Display(Name="Confirm Password")]

        public string cw_password{get; set;}
        // only copied from models what we are going to validate


    }
}