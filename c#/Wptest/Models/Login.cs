using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System;

namespace Wptest.Models{
	public class User:BaseEntity{
		public string first_name{get;set;}
		public string last_name{get;set;}
		public string email{get;set;}
		public string password{get;set;}

		public List <Wedding> = New List

		public User(){
			
		}
	
	public class Wedding:BaseEntity{
		public string wedderone{get; set;}
		public string weddertwo{get; set;}

		public DateTime? Date { get; set;}
		public string address{get; set;}
	}
	}
}