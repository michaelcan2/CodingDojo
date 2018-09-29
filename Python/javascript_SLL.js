
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
        // DDDDDDDDDD settings variable to object, variable could contain an integer or strings
        // but in this case its an object. 
        var newNode = {
            // ????!!!!! to add a new node you need a dictionary??
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

    LinkedList.prototype.append = function(val){
        // append as a node to the end of the list instead of the front.
        // similar to the size method, where we want to keep trasversing through the list
        // till we get to our last node, and then ADD it to the very end.
        // so once we get to the last node we need to make that last node next value
        // change from null to the last node to the new node.
        // this is just how javascript stores data
        var newNode = {
            data: val,
            // b/c were adding this node to the vary end we want the next to equal null
            next: null

        }
        // were using the isEmpty fuction
        // ??!!! did we need the is empty to be a function i dont
        // have this function in my python one.

        // you need to always check if its empty.

        if(this.isEmpty()){
            this.head = newNode;
            // we return out of the fxn.
            return;
        }
        var current = this.head;
        // we want to stop at the very last node.
        // so we put while current.next doesnt equal null not while just current.
        // that way instead of making current go/actually point to null we're gonna stop
        // at the node that points to null and then we'll make that node point to this new
        // node   
        while(current.next !== null){
            current = current.next;

        }
        current.next = newNode;
    

    };

    LinkedList.prototype.contains = function(val){
        var current = this.head;
        while(current !== null){
            if (current.val === val){
                return true;
            }
            // otherwise will go on to the next node
            current = current.next;

        }
        // so if we go through the entire while loop and still haven't returned true
        // then we'll return false
        return false;
        // ^^^which means its not on the list
    };

    LinkedList.prototype.remove = function(val){
        // first need to make a function to prove that its even in the list.
        // if(this.contains(val) !== val) <---does this mean the same thing
        // trying to say if this does not contain the value
        // if the node to be removed is the 
        // head node. all we do is make this.head = this.head.next if nothing is pointing 
        // to the first head then the first head gets deleted.
        if(!this.contains(val)){
            // we would just return, theres nothing to do.
            return;
            // if its true if it simply goes to the next if statment!!
        }
        // otherwise going to check if this.head is the node that needs to be removed.
        if(this.head.data === val){
            // all we do is move this .head to the next node
            this.head = this.head.next;
            return;
        }
        // the second CASE
        // were going to have two pointers to remove a node in the middle
        // one label previous and the other current.
        // were going to keep moving current and have precious be right behind it.
        // SECRET TO REMOVING IS TO SIMPLY NOT POINT TO IT.
        var prev = null;
        var curr = this.head;

        while(curr.data !== val){
            // will move prev to what current is currently pointing too.
            prev = curr;
            // then make curr = curr.next;
            curr = curr.next;
        }
        // now all we have to do is make the previous.next point to current.next
        // to remove the node completely.
        prev.next = curr.next;




    };

    LinkedList.prototype.print = function(val){
        // starting output with an opening brace
        var output = '[';
        // will have current node start at the beginning
        var current = this.head;

        while (current !== null){
            output += current.data;
            // HERE you are adding a COMMA in the print
            if (current.next !== null){
                output += ',';
            }
            // need to have it move on to the next node otherwise it will never move
            // DONT FORGET WHEN YOU PRINTING!!!
            current = current.next;
        }

        output += ']';
        // return output; if you return you get a werid output WHY?
        console.log(output)
    };





// a print method will make this nicer

// var list = new LinkedList();
// list.sayHi()

var list2 =  new LinkedList();
list2.prepend(5);
list2.prepend(9);
list2.append(8);
list2.print();


// this prints how many in the list
// console.log(list2.size());
// console.log(list2.isEmpty());


// a print method will make this nicer.
// console.log(list2)
// LinkedList { head: { data: 9, next: { data: 5, next: null } } }