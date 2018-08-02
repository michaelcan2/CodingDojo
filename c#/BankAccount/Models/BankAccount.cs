using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;


namespace BankAccount.Models{
	public class BankAccount:BaseEntity{
		public User owner{get; set;}
	}
	public class User:BaseEntity{
		public string first_name {get;set;}
		public string last_name {get;set;}
		public string email {get;set;}
		public string password {get;set;}
		public double? balance {get;set;}
		// this is the balance of the user
		public List<Transaction> transactions {get; set;}
		// this is just making the relationship
		// one user can have many transactions
		public User(){
			transactions = new List<Transaction>();
			// this is  making the List for the relationship
		}
		
	}
	public class Transaction: BaseEntity{
			public double? amount{get;set;}
			// amount that the transaction was made.
			public int userid{get; set;}
			// in every transaction its gonna have a user id all these transaction are going to be apart ofthis users.
			public User user{get; set;}
		}
		

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
