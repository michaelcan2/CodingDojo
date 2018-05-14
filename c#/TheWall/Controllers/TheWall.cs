using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using TheWall.Models;
using System;
using System.Collections.Generic;

namespace TheWall.Controllers{
	[Route("/TheWall")]
    public class TheWallController:Controller{
        [HttpGet]
        [Route("")]
        public IActionResult Index(){
            return View("Index");
        }
        [HttpPost]
        [Route("PostMessage")]
        public JsonResult Post(string message){
            // pulls a message in the html that is a string
            // Json result is what we are pulling from the session. its like the info that we pull from the api.
            List<string> comments = new List<string>();
            var AnonObject = new{
                // we made an anonymous object
                message = comments,
            };
            return Json(AnonObject);
    }
}
