using System.ComponentModel.DataAnnotations;
using System;
namespace MyIdeas.Models

{
    public class RegisterViewModel
    {
        [Required]
        [MinLength(2)]
        [Display(Name = "First Name")]
        [RegularExpression(@"^[a-zA-Z -]+$")]
        [MaxLength(255)]
        public string first_name { get; set; }

        [Required]
        [MinLength(2)]
        [Display(Name = "Last Name")]
        [RegularExpression(@"^[a-zA-Z '-]+$")]
        [MaxLength(255)]
        public string last_name { get; set; }
 
        [Required]
        [EmailAddress]
        [Display(Name = "E-Mail")]
        [RegularExpression(@"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", ErrorMessage="Not a valid email address.")]
        [MaxLength(255)]
        public string email { get; set; }
 
        [Required]
        [MinLength(8,ErrorMessage="Passwords must be atleast 8 letters.")]
		[MaxLength(18)]
        [DataType(DataType.Password)]
        [RegularExpression(@"(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,18})$", ErrorMessage="Password must be 8-18 characters long and must contain at least 1 number and 1 letter.")]
        [Display(Name = "Password")]
        public string password { get; set; }
 
        [Display(Name = "Confirm Password")]
        [DataType(DataType.Password)]
        [Compare("password", ErrorMessage = "Password and confirmation must match.")]
        public string passwordconfirmation { get; set; }
    }

    public class LoginViewModel
    {
        [Required]
        [EmailAddress]
        [Display(Name = "E-Mail")]
        [RegularExpression(@"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", ErrorMessage="Not a valid email address.")]
        public string email { get; set; }

        [Required]
        [DataType(DataType.Password)]
        [Display(Name = "Password")]
        public string password { get; set; }
    }
}