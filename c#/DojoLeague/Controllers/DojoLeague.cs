using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System.Data;
using DojoLeague.Factory;
// ^^inside dojoLeague file
using DojoLeague.Models;

namespace DojoLeague.Controllers{
    public class DojoLeagueController:Controller{
        public Ninja ninjas;
        // here were assigning a variable called ninjas this at is called making
        // a pointer.
        public Dojo dojos;
        public DojoLeagueFactory dojoleaguefactory;
        public DojoLeagueController()
        {
            ninjas= new Ninja();
            dojos=new Dojo();
            dojoleaguefactory= new DojoLeagueFactory();
        }
        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            return View("Index");
        }
        [Route("Ninjas")]
        public IActionResult Ninjas(){
            return View();
        }
        [HttpPost]
        [Route("Ninjas")]
        public IActionResult Ninjas(Ninja ninja){
            if(ModelState.IsValid)
            {
                dojoleaguefactory.AddNinja(ninja);
                return RedirectToAction("Ninjas");
                    }
                    return View();       
            }
    }
    }
    // public class DojoLeagueController:Controller{
    //     Dojo dojo;
    //     public DojoLeagueController()
    //     {
    //         DojoLeagueFactory= new DojoLeagueFactory();

    //     }
    //     [HttpGet]
    //     [Route("")]
    //     public IActionResult Index(){
    //         return View("Index");
    //     }
    //     [HttpGet]
    //     [Route("")]
    //     public  IActionResult ***PLACEHOLDER(){
          
    //         return View("Dojos");
    //     }    
    // }

