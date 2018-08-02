using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Http;
using login.Models;

namespace login.Controllers
{
    public class HomeController : Controller
    {
        private logincontext _context;

        public HomeController(logincontext context)
        // homecontroller needs to be same as controller
        {
            _context = context;

        }
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        [Route("Register")]
        public IActionResult Register(UserViewModel user)
        {
            if (ModelState.IsValid)
            {
                PasswordHasher<UserViewModel> Hasher = new PasswordHasher<UserViewModel>();
                user.password = Hasher.HashPassword(user, user.password);
                User newUser = new User()
                {
                    first_name = user.first_name,
                    email = user.email,
                    password = user.password
                };

                _context.Add(newUser);
                _context.SaveChanges();

                return RedirectToAction("Success");
            }
            return View("Index");
        }
        [HttpGet]
        [Route("success")]
        public IActionResult success()
        {
            return View();
        }
        [HttpPost]
        [Route("test")]
        public IActionResult test()
        {
            return View();
        }
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
