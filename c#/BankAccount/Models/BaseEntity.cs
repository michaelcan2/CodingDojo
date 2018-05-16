using System;

namespace BankAccount.Models{
	public abstract class BaseEntity{

		public int id {get;set;}

		public DateTime created_at = DateTime.Now;
		// put DateTime.Now so that in database does not just return 0000000000
		public DateTime updated_at = DateTime.Now;

	}
}
