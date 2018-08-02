using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System;

namespace MyIdeas.Models{

    public class Like:BaseEntity{
        public int likeId{get; set;}
        public int userId {get; set;}
        public User user { get;set; }
        public Post post {get; set;}
        public int postId {get; set;}


    }
	
}