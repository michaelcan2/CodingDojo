using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using WeddingPlanner.Models;
using Microsoft.AspNetCore.Identity;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System;

namespace WeddingPlanner.Controllers{

    public class WeddingPlannerController:Controller{
    	private WeddingPlannerContext _context;

    	public WeddingPlannerController(WeddingPlannerContext context){
    		_context = context;
    	}

         [HttpGet]
        [Route("")]
        public IActionResult Index(){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id !=null)
            {
                return RedirectToAction("Dashboard");
            }
            return View("Index");
        }
        [HttpPost]
        [Route("")]
        public IActionResult Register(RegisterViewModel model)
        {
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id !=null)
            {
                return RedirectToAction("Dashboard");
            }
            if(ModelState.IsValid){
                if(_context.Users.Any(u => u.email == model.email)){
                    ModelState.AddModelError("Email", "A user with this email already exists.");
                    return View("Index");
                }
                 PasswordHasher<RegisterViewModel> Hasher = new PasswordHasher<RegisterViewModel>();
                model.Password = Hasher.HashPassword(model, model.Password);
                User user = new User{
                    // now inputting a new user
                    first_name = model.first_name,
                    last_name = model.last_name,
                    email= model.email,
                    password = model.Password
                };
                _context.Users.Add(user);
                _context.SaveChanges();
                HttpContext.Session.SetInt32("Id", user.id);

                return RedirectToAction("Dashboard");
            }
            return View("Index");
        }
         [HttpGet]
        [Route("login")]
        public IActionResult login1()
        {
        int? Id=HttpContext.Session.GetInt32("Id");
            if(Id != null)
            {
                return RedirectToAction("Dashboard");
            }
            return View("login");
        }
        [HttpPost]
        [Route("login")]
        public IActionResult login(LoginViewModel model){
            // everything in the parenthesis deals with the modelstate
             int? Id = HttpContext.Session.GetInt32("Id");
            //  if its in session log them in
            if(Id !=null)
            {
                return RedirectToAction("Dashboard");
            }
            if(ModelState.IsValid){
                if(!_context.Users.Any(u => u.email == model.email)){
                    ModelState.AddModelError("password", "credentials are wrong.");
                    return View("Login");
            } 
                var user= _context.Users.SingleOrDefault(u => u.email ==model.email);
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.password,model.Password))
                {
                    HttpContext.Session.SetInt32("Id", user.id);
                    return RedirectToAction("Dashboard");
                }
                ModelState.AddModelError("email", "credentials are wrong.");
                return View("Index");
            }
            return View("login");
             }
             [Route("Dashboard")]
             public IActionResult Dashboard(){
                 int? Id = HttpContext.Session.GetInt32("Id");
                if(Id ==null)
                {
                    return RedirectToAction("index");
                }
                     ViewBag.weddings = _context.Wedding.Include(u => u.creator).Include(u => u.attendees);
                     ViewBag.user = _context.Users.SingleOrDefault(u => u.id == HttpContext.Session.GetInt32("Id"));
                     return View("Dashboard");
                }

            [Route("AddWedding")]
            public IActionResult AddWedding(){
                int? Id = HttpContext.Session.GetInt32("Id");
                if(Id == null)
                {
                    return RedirectToAction("Index");
                }
                return View("AddWedding");
            }

            [HttpPost]
            [Route("AddWedding")]
            public IActionResult SaveWedding(WeddingViewModel model){
                int? Id = HttpContext.Session.GetInt32("Id");
                 if(Id == null)
                {
                    return RedirectToAction("Index");
                }
                if(model.date < DateTime.Now){
                    return View("AddWedding");
                }
                if(ModelState.IsValid){
                    Wedding newwedding = new Wedding{
                        wedderone = model.wedderone,
                        weddertwo = model.weddertwo,
                        date = model.date,
                        address = model.address,
                        userid = Id
                    };

                    _context.Wedding.Add(newwedding);
                    _context.SaveChanges();

                    return RedirectToAction("Dashboard");
                }
                return View("AddWedding");
                }


        [Route("logout")]
        public IActionResult logout(){
            HttpContext.Session.Remove("Id");
            // used to remove the session
            return RedirectToAction("Index");
            
        }
        [Route("RSVP/{id}")]
        public IActionResult RSVP(int id){
            int? Id = HttpContext.Session.GetInt32("Id");
                 if(Id == null)
                {
                    return RedirectToAction("Index");
                }
                // the line above just checks if your logged in and grabs it.
            RSVP rsvp = new RSVP{
                userid = Id,
                // Uppercase id was specifically made for Userid
                weddingid = id
                // lowercase was specifically made for the wedding id


            };
            _context.RSVP.Add(rsvp);
            _context.SaveChanges();            // your saving this into your database
            return RedirectToAction("Dashboard");
        }

        [Route("UNRSVP/{id}")]
        public IActionResult UNRSVP(int id){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id == null)
            {
                return RedirectToAction("Index");
            }
            var rsvp = _context.RSVP.SingleOrDefault(u => u.userid == Id && u.weddingid == id);
            if(rsvp != null){
                _context.RSVP.Remove(rsvp);
                _context.SaveChanges();
            }
            return RedirectToAction("Dashboard");
            }
            [Route("delete/{id}")]
            public IActionResult Delete(int id){
                int? Id = HttpContext.Session.GetInt32("Id");
                if(Id == null)
                {
                    return RedirectToAction("Index");
                }
                var wedding = _context.Wedding.Include(u => u.creator).Include(u => u.attendees).SingleOrDefault(u => u.id == id);
                if(wedding != null && wedding.creator.id == Id){
                    _context.Wedding.Remove(wedding);
                    _context.SaveChanges();
                }
                    return RedirectToAction("Dashboard");
                }
            [Route("show/{id}")]
            public IActionResult show(int id){
                int? Id = HttpContext.Session.GetInt32("Id");
                if(Id == null)
                {
                    return RedirectToAction("Index");
                }
                var wedding = _context.Wedding.Include(u => u.creator).Include(u => u.attendees).ThenInclude(u => u.user).SingleOrDefault(u => u.id ==id);
                ViewBag.wedding = wedding;
                return View("Wedding");
            }
            
        



            // the lamda => taking the _conext and saves it for one time into the into the u which will go through the userid 
            // and the weddingid in order to unrsvp


    }
}
