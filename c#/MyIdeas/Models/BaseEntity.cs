using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System;

namespace MyIdeas.Models{
	public abstract class BaseEntity{
		public DateTime created_at {get; set;}
		public DateTime updated_at {get; set;}
		public BaseEntity (){
			updated_at = DateTime.Now;
			created_at = DateTime.Now;
		}
	}
}
