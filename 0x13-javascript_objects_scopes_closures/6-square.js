#!/usr/bin/node
const SquareJ = require('./5-square');

class Square extends SquareJ {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let l = 0; l < this.height; l++) {
      let p = '';
      for (let t = 0; t < this.width; t++) {
        p += c;
      }
      console.log(p);
    }
  }
}

module.exports = Square;
