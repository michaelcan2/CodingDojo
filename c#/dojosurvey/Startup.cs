﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;

namespace dojosurvey
{
    public class Startup
    {
        // This method gets called by the runtime. Use this method to add services to the container.
        // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
     public void ConfigureServices(IServiceCollection services)
{
    services.AddMvc();
}
// This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
    //Debug code...
    app.UseMvc( routes =>
    {
        routes.MapRoute(
            name: "Default", // The route's name is only for our own reference
            template: "", // The pattern that the route matches
            defaults: new {controller = "Hello", action = "Index"} // The controller and method to execute
        );
    });
}


    }
}
