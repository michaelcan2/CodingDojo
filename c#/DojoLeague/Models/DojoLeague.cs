using System.ComponentModel.DataAnnotations;
using System;
using System.Collections.Generic;
// System.Collections.Generic is for list.**

namespace DojoLeague.Models{
	public class Ninja:BaseEntity{
		// changed models name which is your class from DojoLeague to Dojo
		// Ninja IS THE NAME OF OUR MODEL
		public int Id{get; set;}
		[Required]
		public string Name {get; set;}
		public string Description {get; set;}
		[Required]
		[Range(1,10,ErrorMessage = "Value for {0} must {1} and {2}.")]
		public int Level {get; set;}
		public Dojo Dojo_Id {get; set;}
		// this is the post link to the dojo
		// means this ninja is apart of that dojo

	}

	public class Dojo:BaseEntity{
		// this is will have a list because one dojo has many ninjas
		public int Id{get; set;}
		[Required]
		public string Name{get;set;}
		[Required]
		public string Location {get;set;}
		[Required]
		public string information {get;set;}
		public List<Ninja> Ninjas {get;set;}
		// makes a variable list of ninjas but its empty it null
		// we create a list of ninjas about of this dojo
		public Dojo(){
			Ninjas = new List<Ninja>();
		}
	}


		// this one actually fills the with all the ninjas in the database.





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
