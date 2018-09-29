function reverseString(str){
    var word = "";
    for(var i = str.length-1; i>=0; i--){
      word += str[i]  
      
    }
    // your fucntion equas this, its done
     return word
  }
  console.log(reverseString("today"))

 
// --orints anything with an evenlength
function evenLength(arr){
    var result = [];
//   remove Even-Length string
for(var i = 0;i < arr.length; i++){
    // what were iterating through then []the index,
    // saying if the length! of the first string is evemn,
    // we want to remove it.
    if (arr[i].length % 2 != 0){
      // talk to josh about how the runs of algos would go weather to write just the method or to write the entire algos
      result.push(arr[i]);

    }
  }
  return result;
}

console.log(evenLength(['hello', 'so', 'do', 'i', 'yay!']))


function parensValid(str){
    var open = 0;
    var close = 0;
    // dont need to check for even or odds b/c whenever we do find a pair we just go back to zero
    for (var i = 0; i<str.length; i++){
      if(str[i] == '('){ 
       open++;
      }
      // if you want everything single conditional statement to be checked 
      if(str[i] == ')'){
        if(open <= close){
          // b/c in this instruction were return true or false 
          return false;
        }
        // open = -1;
        close ++;
      }   
      // if(str[i] == '(' before the elif then it wont work)
    }
    if(close != open){
      return false;
    }
    else {
      return true;
    }
  }
  
  console.log(parensValid('(whatup))world()'))


// ----pg.82 arrays pt 2

function flatten(arr){
    // the thing about array in place
    // maniulate it inside the same arr,
    // but without the inplace you can make a new array, and put your 
    // stuff in the new place.

    var result = [];
    // first we need to iterate through the array
    for(var i = 0; i <arr.length; i ++){
      
        console.log('looping');
    // checks if its an int or an array
        if(Array.isArray(arr[i]) == true){
       
            console.log(Array.isArray(arr[i]));
            if(arr[i] == undefined){
              for (var j = 0; j < arr.length; j++){
                  console.log(arr[i][j])
                  result.push(arr[i][j])
                }
                console.log(arr[i])
            }
        }
        else{
            result.push(arr[i]);
        }
    }
    return result;
}
console.log(flatten([1,2,3,[4,5],[],8]));

// 1.decide what your getting back and what you need to check for inorder to get that thing back.
// 2. check for what your comparing
// 3. make sure your order of stuff makes sense from 1.
// 4.when your confused console.log everything to give your clarify on that its printing what your expecting.


// ----------- array: Remove Duplicates

function remove(arr){
    for(var i = 0; i < arr.length; i++){
      for(var w=i+1; w < arr.length; w++){
        if(arr[i] == arr[w]){
          arr.splice(w,1);
          console.log( arr[i]);
          
          
        }
  
      }
      
    }
    return arr
  
  }
  
  remove([1,2,3,3,4])
  
  // 1.decide what your getting back and what you need to check for inorder to get that thing back.
  // 2. check for what your comparing
  // 3. make sure your order of stuff makes sense from 1.
  // 4.when your confused console.log everything to give your clarify on that its printing what your expecting.
  
  // check for extra integers