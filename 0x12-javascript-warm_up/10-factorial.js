#!/usr/bin/node

const number = parseInt(process.argv[2]);
let result = 1;

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}

function factorial (a) {
  if (a < 1) {
    return result;
  } else {
    result = a * factorial(a - 1);
    return result;
  }
}
