using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace portfolio.Controllers
{
    public class PortfolioController : Controller
    {
       // Inside your Controller class
// Other code
 
// A GET method
[HttpGet]
[Route("index")]
public string index()
{
    return "Hello World!";
}
// fail safe
 
[HttpGet]
[Route("home")]
public IActionResult home()
{
    return View();
}

[HttpGet]
[Route("projects")]
public IActionResult projects()
{
    return View();
}

[HttpGet]
[Route("contact")]
public IActionResult contact()
{
    return View();// Return a view (We'll learn how soon!)
}

[HttpPost]
[Route("contact")]
public IActionResult contact(string name, string email, string textarea)
{
    return View("contact");// Return a view (We'll learn how soon!)
}

}
}