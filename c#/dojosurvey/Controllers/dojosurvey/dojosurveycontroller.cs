using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace dojosurvey.Controllers
{
    public class dojosurveyController : Controller
    {
       // Inside your Controller class
// Other code
 
// A GET method// fail safe
 
[HttpGet]
[Route("index")]
public IActionResult index()
{
    return View();
}

[HttpPost]
[Route("result")]
public IActionResult results(string name, string location, string language, string textarea)
// we need to take the parameters and then define them in Viewbag

// taking from the result cshtml the name,location language
{
    ViewBag.Name = name;
    ViewBag.Location = location;
    ViewBag.Language = language;
    ViewBag.Textarea = textarea;

    // vbag is how were gonna ask them then in our cshtmls files that are in the views
    return View("result");
    // return RediecttoAction("index)   <--- this is how to redirect 
}

}
}