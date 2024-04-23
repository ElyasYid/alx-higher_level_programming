#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, res, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    printChars(chars, 0);
  }
});

function printChars(chars, index) {
  request(chars[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printChars(chars, index + 1);
      }
    }
  });
}
