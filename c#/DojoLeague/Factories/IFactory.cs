using DojoLeague.Models;
using System.Collections.Generic;


namespace DojoLeague.Factory{
    public interface IFactory<T> where T:BaseEntity{

    }
    
}
// mandycan will only at first make this factory
// in the terminal you must type in
// mandycan factory **nameOfProject**
// in order to create factories in your dapper framework.