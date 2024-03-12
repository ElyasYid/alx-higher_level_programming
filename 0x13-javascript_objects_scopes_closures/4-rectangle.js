#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let l = 0; l < this.height; l++) {
      let p = '';
      for (let t = 0; t < this.width; t++) {
        p += 'X';
      }
      console.log(p);
    }
  }

  rotate () {
    const exch = this.width;
    this.width = this.height;
    this.height = exch;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
