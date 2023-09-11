#!/usr/bin/node

const value = parseInt(process.argv[2]);
let i;
let j;
let width = 'X';
if (isNaN(value)) {
  console.log('Missing size');
} else if (value > 0) {
  for (i = 1; i < value; i++) {
    width = width + 'X';
  }
  for (j = 0; j < value; j++) {
    console.log(width);
  }
}
