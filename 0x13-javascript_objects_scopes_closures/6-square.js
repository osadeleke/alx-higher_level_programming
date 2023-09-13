#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      let j = 0;
      let widthPrint = '';
      while (i < this.size) {
        widthPrint = widthPrint + c;
        i++;
      }
      while (j < this.size) {
        console.log(widthPrint);
        j++;
      }
    }
  }
}

module.exports = Square;
