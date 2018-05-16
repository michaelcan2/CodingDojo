using System.ComponentModel.DataAnnotations;
namespace BankAccount.Models
{
    public class RegisterViewModel : BaseEntity
    {
        [Required]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z]+$")]
        [Display(Name = "First Name")]
        public string first_name { get; set; }

        [Required]
        [MinLength(2)]
        [RegularExpression(@"^[a-zA-Z]+$")]
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

    public class BalanceViewModel : BaseEntity
{
    [Required]
    [RegularExpression(@"^[+-]?[0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?$", ErrorMessage = "Not Valid Dollar amount!")]
    // this makes it only have two numbers after the decimal that is what {2}^^ just above means
    public double? balance {get;set;}
}



    
}
