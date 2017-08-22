var myNum = 5;
var myString = "Hello Universe";
var myArr = [1,2,3,4];
var myObj = { name:'Bill'};
var anythingVariable = "Hey";
var anythingVariable2 = 25; 
var arrayOne = [true, false, true, true]; 
var arrayTwo = [1, 'abc', true, 2];
var myObj2 = { x: 5, y: 10 };
// object constructor
class MyNode {
    val = 0;
    priv: number
    constructor(value: number) {
        this.val = value
    }

    doSomething() {
        this.priv = 10
    }
    
}

var myNodeInstance = new MyNode(1);
console.log(myNodeInstance.val);
function myFunction() {
    console.log("Hello World");
    return;
}
function sendingErrors() {
	throw new Error('Error message');
}
