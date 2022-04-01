/* 
 - HashMap is a datastructure which maps keys to values 
 - build internally using arrays 
 example 
const obj = {
   "firstName": "Abubakar"
   "lastName" : "Ali"
}

console.log(obj['firstName']) will give you "Abubakar"

- Array is also a datastructure that maps keys to values 
- Main difference between Arrays and HashMap is that;in Arrays data is referenced using a numerical index; 
- since hashmap internally uses an array we have to our keys (strings) to numerical integers
- hashing relies on utf-8 referencing to get strings equivalent numerical representation 
*/

//!!IMPORTANT : HASHMAPS USE PRIME NUMBERS TO INCREASE UNIQUENESS OF HASHES THAT MAP TO KEYS 

class HashMap {
    constructor(arraySize = 3){
        this.keyMap = new Array(arraySize)
    }
    _hash = (str) => {
         if(typeof str !== 'string') {
           return str
         }
        let total 
       // weird prime ensures the items in the keymap array are spaced out , increasing randomness of key
        let WEIRD_PRIME = 13; 
       // if string is larger , no need to iterate over all chars
        for(let i = 0 ; i < Math.min(str.length, 100) ; i ++){
            total = (WEIRD_PRIME * (str[i].charCodeAt(0) - 96)) % this.keyMap.length
        }
        return total
    }

   // resize called when loadFactor is 80 % ; 
   // rehashes everything 
   // doubles table size 

    resize =( ) => {
     let newTable = new Array(this.keyMap.length * 2)
     this.keyMap.forEach((items) => {
       items.forEach(([key,value])=> {
          const itemKey = this._hash(key)

        
        if(!this.keyMap[itemKey]){
           
          return this.keyMap[itemKey] = [[key,value]]
        }else {
         //check if similar key exists 
         const values = this.keyMap[itemKey];
         
         for(let i=0; i < values.length; i++){
           if(values[i][0] === key){
            //overide existing  
             return values[i][1] = value 
           }
         }
         // collisions occurs when two keys share the same hash (array is small , 'rat', 'tar')
         // handles collisions using separate chaining 
           
           this.keyMap[itemKey].push([key,value])
           
         
        }
         
       })
     })
      this.keyMap = newTable

    }

 //inserts an item
    numsItem = 0
    set = (key,value) => {
        this.numsItem++
        const loadFactor = this.numsItem / this.keyMap.length
         if(loadFactor > 0.8){
          this.resize()
         }
        const itemKey = this._hash(key)

        
        if(!this.keyMap[itemKey]){
           
          return this.keyMap[itemKey] = [[key,value]]
        }else {
         //check if similar key exists 
         const values = this.keyMap[itemKey];
         
         for(let i=0; i < values.length; i++){
           if(values[i][0] === key){
            //overide existing  
             return values[i][1] = value 
           }
         }
         // collisions occurs when two keys share the same hash (array is small , 'rat', 'tar')
         // handles collisions using separate chaining 
           
           this.keyMap[itemKey].push([key,value])
           
         
        }

    }

 //gets an individual item
    get = (key) => {
     const idx = this._hash(key)
       if(!this.keyMap[idx]){
        return undefined
       }
     return this.keyMap[idx].find(x => key === x[0])[1]
    }

 // returns all keys 
   _getAllKeys = ( ) => {
    let keyArray = []
    for(let i = 0; i<this.keyMap.length; i++){
      if(this.keyMap[i]){
       for(let j=0; j < this.keyMap[i].length; j++){
          if(!keyArray.includes(this.keyMap[i][j][0])){
            keyArray.push(this.keyMap[i][j][0])
          }
       }
      }
   
    }
      return keyArray
   }


 //returns all values
  _getAllValues = () => {
   const valueArr = []
   for(let i =0 ; i< this.keyMap.length; i++){
     if(this.keyMap[i]){
      for(let j=0; j < this.keyMap[i].length; j++){
        if(!valueArr.includes(this.keyMap[i][j][1])){
         valueArr.push(this.keyMap[i][j][1])
        }
      }
     }
   }
   return valueArr
  }


}

const ht = new HashMap()
ht.set('firstName','Abubakar');
ht.set('fName','Abubakar');
ht.set('tName','Abubakar');
ht.set('zirstName','Abubakar');
ht.set('yfName','Abubakar');
ht.set('trwName','Abubakar');
ht.set('firrstName','Abubakar');
ht.set('fhsfName','Abubakar');
ht.set('wtName','Abubakar');

console.log(ht.keyMap)

