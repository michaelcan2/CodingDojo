using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System;

namespace MyIdeas.Models{
	public class User:BaseEntity{
		 
		public int userId {get; set;}
		public string first_name{get;set;}
		public string last_name{get;set;}
		public string email{get;set;}
		public string password{get;set;}
		[InverseProperty("creator")]
		public List<Post> created {get; set;}
		public List<Like> liked {get; set;}

		public User(){
			created=new List<Post>();
			liked=new List<Like>();
			
		}
	}
}