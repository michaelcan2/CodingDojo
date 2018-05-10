using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using pokemoninfo.Models;
using System.Net.Http;
using Newtonsoft.Json;

namespace pokemoninfo.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
        
           


            return View();
        }

         public IActionResult pokeinfo()
        {
            ViewData["Message"] = "Your contact page.";
             ViewData["Name"] = "Michael";
            ViewData["Type"] = "YAY!";
            ViewData["Weight"] = "enough";
            ViewData["Height"] = "Average";

            return View();
        }

        [HttpGet]
[Route("pokemon/{pokeid}")]
public IActionResult QueryPoke(int pokeid)
{
    var PokeInfo = new Dictionary<string, object>();
    WebRequest.GetPokemonDataAsync(pokeid, ApiResponse =>
        {
            ViewBag.PokeInfo = ApiResponse;
            // made it a viewbag

        }
    ).Wait();
    // Other code
    return View();
    // added
}



        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
