using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System;
 
namespace passcode.Controllers
{
    public class PasscodeController : Controller
    {
       // Inside your Controller class
// Other code
 
 
        [HttpGet]
        [Route("index")]
        public IActionResult index()
        {
            int? count = HttpContext.Session.GetInt32("count");
            if(count == null){
                count = 0;
            }
            count +=1;
            Random rand = new Random();

            string characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            String passcode ="";

            for(int i =0; i<14; i++){
                passcode += characters[rand.Next(0,characters.Length)];
            }
            ViewBag.Count = count;
            ViewBag.Passcode = passcode;
            HttpContext.Session.SetInt32("count",(int)count);
            return View();
        }
}
}