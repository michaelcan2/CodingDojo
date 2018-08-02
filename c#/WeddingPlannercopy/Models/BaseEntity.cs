using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System;

namespace WeddingPlanner.Models{
	public abstract class BaseEntity{
		
		public int id{get; set;}
		public DateTime created_at {get; set;}
		// no getter or setter so it just does it one time.

		public DateTime updated_at {get; set;}

		public BaseEntity (){
			updated_at = DateTime.Now;
			created_at = DateTime.Now;
			// we need in Baseentity the current and updated datetime to keep track in the database.
		}
	}
}
