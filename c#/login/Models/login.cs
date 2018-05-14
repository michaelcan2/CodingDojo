using System;
using System.ComponentModel.DataAnnotations;

namespace login
{
    public class User
    {
        [Required]
        [MinLength(3)]
        public string first {get; set;}

        [Required]
        [MinLength(3)]
        public string last {get; set;}

        [Required]
        [EmailAddress]
        public string Email { get; set; }

        [Required]
        [DataType(DataType.Password)]
        public string Password { get; set; }

        [Required]
        [DataType(DataType.Password)]
        [Compare("Password", ErrorMessage = "Your passwords does not match")]
        // passing Compare through a string called pasword.
        public string ConfirmPassword { get; set; }

    }
}