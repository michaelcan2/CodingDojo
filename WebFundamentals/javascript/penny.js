function timePassed(day){
    var penny=.01;
    for(var i=1;i<=day;i++){
    if(i===1){
      console.log(i + "day" + "="  + penny)
      penny+=penny
     }else {
       console.log(i + "day"+ "=" + penny)
       penny+=penny
     }
    }
    return penny
  }
  timePassed(30)