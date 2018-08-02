using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using System.Linq;
using Wptest.Models;



namespace Wptest.Controllers{
	[Route("/Wptest")]
    public class WptestController:Controller{
    	private WptestContext _context;

    	public WptestController(WptestContext context){
    		_context = context;
    	}

        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            return View("Index");
        }
    }
}
