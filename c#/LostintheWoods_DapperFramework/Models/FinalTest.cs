using System.ComponentModel.DataAnnotations;
// models

namespace FinalTest.Models{
	public class woodsTrails{
		public int id {get; set;}
		[Required]
		[MinLength(3)]
		[MaxLength(255)]
		public string Name {get; set;}
		[Required]
		[MinLength(3)]
		[MaxLength(255)]

		public string Description {get; set;}
		[Required]
		[RegularExpression("([0-9]+)",ErrorMessage = "Please enter a valid number")]
		public int? Length{get; set;}
		// must be nullable int? 

		[Required]
		[RegularExpression("([0-9]+)",ErrorMessage = "Please enter a valid number")]
		public int? Elevation{get; set;}
		// must be nullable int? in order to display correct error messge for an empty error 
		// field which will give you better error messages.
		[Required]
		[RegularExpression(@"^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$", ErrorMessage = "Please enter a valid Number")]
		public double? Latitude{get; set;}
		// 
		[Required]
		[RegularExpression(@"^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$", ErrorMessage = "Please enter a valid Number")]
		public double? Longitude{get; set;}
		// 

		
		

/*
	Useful Annotations and Examples:

	[Required] - Makes a field required.
	[RegularExpression(@"[0-9]{0,}\.[0-9]{2}", ErrorMessage = "error Message")] - Put a REGEX string in here.
	[MinLength(100)] - Field must be at least 100 characters long.
	[MaxLength(1000)] - Field must be at most 1000 characters long.
	[Range(5,10)] - Field must be between 5 and 10 characters.
	[EmailAddress] - Field must contain an @ symbol, followed by a word and a period.
	[DataType(DataType.Password)] - Ensures that the field conforms to a specific DataType
*/
	}
}
