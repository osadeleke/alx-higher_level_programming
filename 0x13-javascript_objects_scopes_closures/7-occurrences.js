#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let ind = 0;
  while (list[ind]) {
    if (list[ind] === searchElement) {
      count++;
    }
    ind++;
  }
  return count;
};
