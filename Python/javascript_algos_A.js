// function reverseString(str){
//     var word = "";
//     for(var i = str.length-1; i>=0; i--){
//       word += str[i]  
      
//     }
//     // your fucntion equas this, its done
//      return word
//   }
//   console.log(reverseString("today"))

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


// function parensValid(str){
//     var open = 0;
//     var close = 0;
//     // dont need to check for even or odds b/c whenever we do find a pair we just go back to zero
//     for (var i = 0; i<str.length; i++){
//       if(str[i] == '('){ 
//        open++;
//       }
//       // if you want everything single conditional statement to be checked 
//       if(str[i] == ')'){
//         if(open < close){
//           // b/c in this instruction were return true or false 
//           return false;
//         }
//         // open = -1;
//         close ++;
//       }   
//       // if(str[i] == '(' before the elif then it wont work)
//     }
//     if(close != open){
//       return false;
//     }
//     else {
//       return true;
//     }
//   }
  
//   console.log(parensValid('(whatup))world()'))
  