using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using BankAccount.Models;
using Microsoft.AspNetCore.Identity;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

namespace BankAccount.Controllers{
    
    public class BankAccountController:Controller{
        private BankAccountContext _context;
 
        public BankAccountController(BankAccountContext context)
        {
            _context = context;
        }
        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            int? Id = HttpContext.Session.GetInt32("Id");
            if(Id !=null)
            {
                return RedirectToAction("Account");
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
                return RedirectToAction("Account");
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
                    password = model.Password,
                    balance = 0
                };
                _context.Users.Add(user);
                _context.SaveChanges();
                HttpContext.Session.SetInt32("Id", user.id);

                return RedirectToAction("Account");
            }
            return View("Index");
        }
         [HttpGet]
        [Route("login")]
        public IActionResult login1()
        {
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
                return RedirectToAction("Account");
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
                    return RedirectToAction("Account");
                }
                ModelState.AddModelError("email", "credentials are wrong.");
                return View("Index");
            }
            return View("login");
        }
        [Route ("Account")]
        public IActionResult Account(){
            //  if its in session log them in
            if(HttpContext.Session.GetInt32("Id")==null)
            {
                return RedirectToAction("Index");
            }
            // now we are getting the user ands aving them into the viewbag 

            var user = _context.Users.Include( u => u.transactions ).SingleOrDefault(u => u.id == HttpContext.Session.GetInt32("Id"));
            user.transactions = user.transactions.OrderByDescending(t => t.created_at).ToList();
            ViewBag.user = user;
            // include was made to include the transactions into the user.
            return View("Account");
        }
        [HttpPost]
        [Route("Transaction")]
        public IActionResult transaction(BalanceViewModel transaction){
            if(HttpContext.Session.GetInt32("Id") == null)
            {
                return RedirectToAction("Index");
            }
            var user = _context.Users.Include( u => u.transactions ).SingleOrDefault(u => u.id == HttpContext.Session.GetInt32("Id"));
            if(ModelState.IsValid){
                if(transaction.balance < 0){
                    if(user.balance + transaction.balance < 0){
                        ModelState.AddModelError("balance", "You don't have enough to withdraw" + transaction.balance + ".");
                        user = _context.Users.Include(u => u.transactions).SingleOrDefault(u => u.id == HttpContext.Session.GetInt32("Id"));
                        ViewBag.user = user;
                        return View("Account");
                    }
                }
                Transaction newtransaction = new Transaction{
                    amount = transaction.balance,
                    userid = user.id,
                    user=user
                };
                _context.Transactions.Add(newtransaction);
                user.balance += transaction.balance;
                _context.SaveChanges();
                return RedirectToAction("Account");
            }
            user.transactions = user.transactions.OrderByDescending(t => t.created_at).ToList();
            ViewBag.user = user;
            return View("Account");
        }
        [Route("logout")]
        public IActionResult logout(){
            HttpContext.Session.Remove("Id");
            // used to remove the session
            return RedirectToAction("Index");
        }

    }
}
