#!/usr/bin/node

let largestValue;
let secondLargest;
let i = 3;

if (process.argv.length < 4) {
  console.log(0);
} else {
  largestValue = process.argv[2];
  while (process.argv[i] !== undefined) {
    if (largestValue < process.argv[i]) {
      largestValue = process.argv[i];
    }
    i++;
  }
  i = 0;
  secondLargest = process.argv[2];
  while (process.argv[i] !== undefined) {
    if (process.argv[i] > secondLargest && process.argv[i] !== largestValue) {
      secondLargest = process.argv[i];
    }
    i++;
  }

  console.log(secondLargest);
}
