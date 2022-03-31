/*
 a linked list is a data structure which is defined by a node that stores the value and a pointer to the next node 
example 
Head            Tail
12 -> 2 -> 3 -> 1

*/


//node that defines the value and next pointer
class Node {
    constructor(val){
        this.val = val 
        this.next = null
    }
}

class SinglyLinkedList {
    constructor(val){
        this.head = null
        this.tail = null
        this.length = 0 ; 
    }
    //add from the bottom 
    push(val){
        let  newNode = new Node(val)
        if(!this.head){
            this.head = newNode
            this.tail = this.head
        } else {
            this.tail.next = newNode
            this.tail = newNode
        }
        
        
        this.length++
        return this

    }

     //remove from the bottom 
    pop(){
        if(!this.head) return undefined; 
        let current = this.head; 
        let newNode = current 

        while(current.next){
            newNode = current; 
            current = current.next;
        }
        this.tail = newNode; 
        this.tail.next = null 
        this.length--
        if(this.length === 0){
            this.head = null; 
            this.tail = null
        }
        return newNode

    }

    //add from the top 
    shift(){
        if(!this.head) return undefined; 
        let currentHead = this.head ; 
        this.head = currentHead.next; 
        this.length--; 
        if(this.length === 0){ 
            this.tail = null
        }
        return currentHead
    }

     // remove first element
    unshift(val){
        let newNode = new Node(val)
        if(!this.head){
            this.head = newNode; 
            this.tail = this.head
        }else {
            newNode.next = this.head; 
            this.head = newNode
        }
        this.length++
        return newNode
    }


    //get an element using an index
    get(index){
        if(index < 0 || index > this.length) return null
        let counter = 0 ; 
        let current = this.head
        while(counter !== index){
            current = current.next; 
            counter++
        }
        return current
    }

    //update an element using and index and a value 
    set(index,val){
      let foundNode = this.get(index)
      if(foundNode) {
          foundNode.val = val;
          return true
      }

      return false

 
    }

    //insert anywhere in the list

    insert(index, val){
        //check if index is valid
        if(index < 0 || index > this.length){
            return undefined
        } else if(index === this.length ) {
            this.push()
            return true
        } else if(index === 0 ){
            this.shift(val)
            return true
        } else {
        //create new node; 
        let newNode = new Node(val)
        let nextNode = this.get(index)
        let prevNode = this.get(index - 1)
        newNode.next = nextNode
        prevNode.next = newNode

        this.length++
        return true
        
        }
            
    }

    //remove from anywhere in the list
  remove(index){
      //check if index is valid
      if(index < 0 || index > this.length) return undefined
      if(index === 0) return !!this.unshift()
      if(index === this.length) return !!this.pop()

      // 
      let prevNode = this.get(index - 1)
      let nextNode = this.get(index)

      prevNode.next = nextNode
      this.length--;
      return true
  }
   reverse(){
       let node = this.head;
       this.head = this.tail; 
       this.tail = node; 

       let prev = null; 
       let next; 
    

       for(let i = 0 ; i< this.length; i++){
           //changes the pointer
           next = node.next; 
           node.next = prev

           //iterates
           prev = node; 
           node = next
       }

       return this
   }

    print(){
        let arr = []
        let current = this.head
        while(current){
            arr.push(current.val)
            current = current.next
        }

        return arr
    }
}

const list = new SinglyLinkedList()
list.push("Hello")
list.push('world')
list.push('254')


