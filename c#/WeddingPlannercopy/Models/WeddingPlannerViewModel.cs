using System.ComponentModel.DataAnnotations;
using System;
namespace WeddingPlanner.Models
{
    public class RegisterViewModel : BaseEntity
    {
        [Required]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z -]+$")]
        [Display(Name = "First Name")]
        public string first_name { get; set; }

        [Required]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z '-]+$")]
        [Display(Name = "Last Name")]
        public string last_name { get; set; }
 
        [Required]
        [EmailAddress]
        [Display(Name = "email")]
        public string email { get; set; }
 
        [Required]
        [MinLength(8)]
        [DataType(DataType.Password)]
        [Display(Name = "Password")]
        public string Password { get; set; }

        [Display(Name = " Confirm Password")]
        [DataType(DataType.Password)]
        [Compare("Password", ErrorMessage = "Password and confirmation must match.")]
        public string PasswordConfirmation { get; set; }
    }
    public class LoginViewModel : BaseEntity{
        [Required]
        [EmailAddress]
        [Display(Name = "email")]
        public string email { get; set; }

         [Required]
        [MinLength(8)]
        [DataType(DataType.Password)]
        [Display(Name = "Password")]
        public string Password { get; set; }
    }

    public class WeddingViewModel : BaseEntity
            {
        [Required]
        [Display(Name = "Title")]
    public string wedderone {get;set;}
        [Required]
        [Display(Name = "Time")]	
   public string weddertwo {get;set;}
    [Required]
    [Display(Name = "Date")]
    [DataType(DataType.Date)]	

	public DateTime? date {get;set;}
    [Display(Name = "Description")]
    public string address {get;set;}
}



    
}

// VIEWMODELS IS WHERE YOUR VALIDATIONS GO