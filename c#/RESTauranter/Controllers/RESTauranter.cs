using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using RESTauranter.Models;
using System.Linq;

namespace RESTauranter.Controllers{
	[Route("/RESTauranter")]
    public class RESTauranterController:Controller{
        private RESTauranterContext _context;
        // changed yourContext to RESTauranterContext
        public RESTauranterController(RESTauranterContext context)
        {
            _context = context;
        }
 
        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            // List<Person> AllUsers = _context.Users.ToList();
            // return View("Index");
        }
    }
}
