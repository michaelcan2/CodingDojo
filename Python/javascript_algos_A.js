function reverseString(str){
    var word = "";
    for(var i = str.length-1; i>=0; i--){
      word += str[i]  
      
    }
    // your fucntion equas this, its done
     return word
  }
  console.log(reverseString("today"))

 

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
        if(open < close){
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

//   -----javascript singly linked lists------
// starts off with a consturctor function for a linked lists

function LinkedList(){
    // the linked list only has one property known to it and thats the head node.
    // its null first because the list is empty.
    this.head = null;
}



    // !!!BELOW IS ONE WAY WE CAN ADD A METHOD TO THE CONSTRUCTOR FXN.
    // sayHi is the name of the method and can be called by --"w/elistnameis".sayHi();--
    // this.sayHi=function(){
    //     console.log('Hi');

    // };

    // !!!!THIS IS THE OTHER WAY: ADD IT TO THE PROTOTYPE OF THE FXN.
    // using Prototype is the normal convention. This is b/c if we wanted to make more 
    // then one list.    var list2 = new LinkedList();      var list3 = new LinkedList();
    // if we just left sayHi on line 67 in the constructor everytime we make a new linked list
    //  it would be constructing its own say hi function. so var list,var list2, var list3,
    // wld have there own say hi function in memory. it's insufficeint to keep creating a fxn.
    // over and over everytime you create a linked list.
    // THIS IS WHY PROTOTYPE ARE HELPFUL.

    LinkedList.prototype.sayHi = function(){
        console.log('Hi');
        // WHEN you add a function to a prototype, this prototype is just ONE object,
        // and it's shared by every instance of the linked list. SO no matter how many
        // list we create this is just going to be one object, the prototype is just
        // going to be one object  that has a fuction attached to it. 
        // it will be the same thing so will still be able to access them in each of the list 
        // and it will be much more efficent. 

        // WARNNING!! when you use the prototype you lose the ability to create
        // private variables. So were sacrificing that for efficently.     
    };

    LinkedList.prototype.isEmpty = function(){
        // three equal signs has to be the same data time
        if (this.head === null){
          return true;
        }else{
            return false;
        }

        };


    LinkedList.prototype.size = function(){
        // this current is the runner and is starting at this.head
        var current = this.head;
        
        // have a variable count start at zero. and start at this.head and keep
        // traversing through the list to the end and everytime we go to the next node
        // we will increment the account.
        var count = 0;

        while(current !== null){
            count++;
            current = current.next;
        }
        return count;
    };
    // prepend will need to take a value, w/e value you want to add at the beginning
    // of the list.
    LinkedList.prototype.prepend = function(val){
        // this function will add a node to the beginning of a list.
        // creating an object is very easy in javascript
        var newNode = {
            // a node has two properties inside it and it has a pointer to the
            // next node
            data: val,
            // and our next node remember that we want this new node to be pointing
            // to the previous self.head 
            next: this.head 

        };
        // now we just need to update this.head to point to this new_node
        this.head = newNode;
    };



// var list = new LinkedList();
// list.sayHi()

var list2 =  new LinkedList();
list2.prepend(5);
list2.prepend(9);

console.log(list2)