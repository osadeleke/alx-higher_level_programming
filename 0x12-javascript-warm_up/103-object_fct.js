#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
//start here
function incr() {
	myObject.value++;
}
myObject.incr = incr;
//end here
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
