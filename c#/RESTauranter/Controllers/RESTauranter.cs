using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using RESTauranter.Models;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace RESTauranter.Controllers{

    public class RESTauranterController:Controller{
        private ReviewsContext _context;
        public RESTauranterController(ReviewsContext context)
        {
            _context = context;
        }
        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            return View("Index");
        }
        [HttpPost]
        [Route("review")]
        public IActionResult reviews(Reviews newReview){
        if(ModelState.IsValid){
            _context.Add(newReview);
            _context.SaveChanges();
        
            return RedirectToAction("review");
            // RedirectToAction to this specifc route route 
        }
            return View("Index");
        }
        [HttpGet]
        [Route("review")]
        public IActionResult review(){
             ViewBag.reviews = _context.reviews.OrderBy(date => date.created_at).ToList();
            return View();
        }


    }
}
