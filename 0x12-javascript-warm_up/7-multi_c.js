#!/usr/bin/node

const value = parseInt(process.argv[2]);
let i = 0;

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else if (value > 0) {
  while (i < value) {
    console.log('C is fun');
    i++;
  }
}
