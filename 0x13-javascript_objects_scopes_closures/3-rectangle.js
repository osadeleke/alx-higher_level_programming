#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let widthPrint = '';
    while (i < this.width) {
      widthPrint = widthPrint + 'X';
      i++;
    }
    while (j < this.height) {
      console.log(widthPrint);
      j++;
    }
  }
}

module.exports = Rectangle;
