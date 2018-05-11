using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System.Data;
using MySql.Data.MySqlClient;
using FinalTest.Factory;
using FinalTest.Models;
// when connecting to Factory say using *namespaceinFactory* exactly 
// session can go up
// Controller

namespace FinalTest.Controllers{
    public class FinalTestController:Controller{
        TrailFactory trailfactory;
        public FinalTestController()
        {
            trailfactory=new TrailFactory();
        }
        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            ViewBag.Trails = trailfactory.FindAll();
            // brings mysql to html
            return View("index");
        }
        [HttpGet]
        [Route("AddTrail")]
        public  IActionResult newtrailget(){
           System.Console.WriteLine("here");
            return View("AddTrail");
        }     
        [HttpPost]
        [Route("AddTrail")]
        public  IActionResult newtrailpost(woodsTrails trail){
            if(ModelState.IsValid)
            {
                trailfactory.Add(trail);
                return RedirectToAction("Index");
            }
            return View("AddTrail");
            // this is return view of addtrail
        }     
        [Route("trail/{id}")]
        public IActionResult trail(int id){
            ViewBag.Trail=trailfactory.FindByID(id);
        // method wrote in factoy now being used to route for the trail.html
        // iactionresult is what you are going to return
        return View();
        }
    }
}
