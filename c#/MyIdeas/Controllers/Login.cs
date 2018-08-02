using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using Microsoft.AspNetCore.Identity;
using MyIdeas.Models;

namespace MyIdeas.Controllers{
    public class LoginController:Controller{
    	private MyIdeasContext _context;

    	public LoginController(MyIdeasContext context){
    		_context = context;
    	}

        [HttpGet]
        [Route("")]
        public IActionResult Register(){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id != null)
            {
                return RedirectToAction("Index", "MyIdeas");
            }
            return View("Register");
        }
        [HttpPost]
        [Route("")]
        public IActionResult Register(RegisterViewModel model){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id != null)
            {
                return RedirectToAction("Index", "MyIdeas");
            }
            if(ModelState.IsValid){
                if(_context.users.Any(u => u.email == model.email)){
                    ModelState.AddModelError("email", "A user with this email already exists.");
                    return View("Register");
                }
                PasswordHasher<RegisterViewModel> Hasher = new PasswordHasher<RegisterViewModel>();
                model.password = Hasher.HashPassword(model, model.password);
                User user = new User{
                    first_name = model.first_name,
                    last_name = model.last_name,
                    email = model.email,
                    password = model.password
                };
                _context.users.Add(user);
                _context.SaveChanges();
                HttpContext.Session.SetInt32("Id", user.userId);

                return RedirectToAction("Index", "MyIdeas");
            }
            return View("Register");
        }
        [HttpGet]
        [Route("login")]
        public IActionResult Login(){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id != null)
            {
                return RedirectToAction("Index", "MyIdeas");
            }
            return View("Login");
        }
        [HttpPost]
        [Route("login")]
        public IActionResult Login(LoginViewModel model){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id != null)
            {
                return RedirectToAction("Index", "MyIdeas");
            }
            if(ModelState.IsValid){
                if (!_context.users.Any(u => u.email == model.email)){
                    ModelState.AddModelError("email", "Credentials are wrong.");
                    return View("Login");
                }
                var user = _context.users.SingleOrDefault(u => u.email == model.email);
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.password, model.password))
                {
                    //Handle success
                    HttpContext.Session.SetInt32("Id", user.userId);
                    return RedirectToAction("Index", "MyIdeas");
                }
                ModelState.AddModelError("email", "Credentials are wrong.");
                return View("Login");
                
            }
            return View("Login");
        }
        [Route("logout")]
        public IActionResult Logout(){
            HttpContext.Session.Remove("Id");
            return RedirectToAction("Register");
        }
    }
}