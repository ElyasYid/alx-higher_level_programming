#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < x; k++) {
    console.log('C is fun');
  }
}
