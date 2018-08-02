using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using System.Linq;
using MyIdeas.Models;
using System.Collections.Generic;

namespace MyIdeas.Controllers{
    [Route("/MyIdeas")]
	
    public class MyIdeasController:Controller{
    	private MyIdeasContext _context;

    	public MyIdeasController(MyIdeasContext context){
        _context = context;
    }

    [HttpGet]

    [Route("Index")]
    public IActionResult Index(){
        int? userId = HttpContext.Session.GetInt32("Id");
        User currentUser = _context.users.SingleOrDefault(u => u.userId == userId);
        if(userId == null){
            return RedirectToAction("Register", "Login");
        }
        List<User> mainList = _context.users.ToList();
        List<Post> ideasList = _context.posts.Include(p => p.creator).Include(p => p.likes).OrderByDescending(p => p.likes.Count).ToList();
        foreach (var i in ideasList)
        {
            foreach (var u in currentUser.liked)
            {
                if(u.postId == i.postId){
                    i.currentUser = true;
                }
            }
        }

        ViewBag.ideas = ideasList;
        ViewBag.user = currentUser;

        return View("Index");
    }
        [HttpPost]
        [Route("create")]
        public IActionResult Create(string content){

            int? userId = HttpContext.Session.GetInt32("Id");

            if(userId == null){
                return RedirectToAction("Register", "Login");
            }

            Post newPost = new Post(){
                content = content,
                creatorId = (int)userId,
            };

            _context.Add(newPost);
            _context.SaveChanges();

            return RedirectToAction("Index");
        }
        [HttpGet]
        [Route("delete/{postId}")]
        public IActionResult Delete(int postId){ 
            System.Console.WriteLine("ITS NOT");
            int? userId = HttpContext.Session.GetInt32("Id");

            if(userId == null){
                return RedirectToAction("Register", "Login");
            }

            Post removePost = _context.posts.SingleOrDefault(p => p.postId == postId);

            if((int)userId == removePost.creatorId){
                _context.posts.Remove(removePost);
                _context.SaveChanges();
            }
            return RedirectToAction("Index");
        }
        [HttpGet]
        [Route("like/{postId}")]
        public IActionResult Like(int postId){
            int? userId = HttpContext.Session.GetInt32("Id");

            if(userId == null){
                return RedirectToAction("Register", "Login");
            }

            Like newLike = new Like(){
                userId = (int) userId,
                postId = postId,
                };

            _context.Add(newLike);
            _context.SaveChanges();

            return RedirectToAction("Index");
        }
        [HttpGet]
        [Route("show/{userId}")]
        public IActionResult UserPage(int userId){
            
            int? uId = HttpContext.Session.GetInt32("Id");

            if(uId == null){
                return RedirectToAction("Register", "Login");
            }
            User thisUser = _context.users.Include(u => u.liked).Include(u => u.created).SingleOrDefault(u => u.userId == userId);
            ViewBag.ThisUser = thisUser;

            return View("User");
        }
        [HttpGet]
        [Route("idea/{postId}")]
        public IActionResult IdeaPage(int postId){
            int? userId = HttpContext.Session.GetInt32("Id");

            if(userId == null){
                return RedirectToAction("Register", "Login");
            }
            
            Post thisPost = _context.posts.Include(p => p.creator).Include(p => p.likes).ThenInclude(like => like.user).SingleOrDefault(p => p.postId == postId);

            var likers = _context.likes.Where(l => l.postId == postId).Include(l => l.user).GroupBy(l => l.userId);

            ViewBag.thisPost = thisPost;
            ViewBag.likers = likers; 

            return View("Post");
        }



}
}