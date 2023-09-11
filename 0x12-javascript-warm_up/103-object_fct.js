#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/*
function myObject.incr () {
  myObject.value++;
}
*/
function incrObj (a) {
  a++;
}
myObject.incr = incrObj(myObject.value);
console.log(myObject);
/*
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
*/
