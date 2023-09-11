#!/usr/bin/node

let i = 2;
let j;
let listNumbers;
let finalList;

if (process.argv.length < 4) {
  console.log(0);
} else {
  listNumbers = [];
  while (process.argv[i] !== undefined) {
    console.log(process.argv[i]);
    listNumbers.push(parseInt(process.argv[i]));
    i++;
  }
  
  console.log(listNumbers);
  listNumbers.sort((a, b) => b - a);
  
  finalList = [listNumbers[0]];
  j = 1;
  while (listNumbers[j]) {
    if (listNumbers[j - 1] !== listNumbers[j]) {
      finalList.push(parseInt(listNumbers[j]));
    }
    j++;
  }
  console.log(finalList);
  console.log(finalList[1]);
 
}
