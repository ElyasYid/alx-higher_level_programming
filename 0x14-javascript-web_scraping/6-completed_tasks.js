#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let compd = {};
    todos.forEach((todo) => {
      if (todo.compd && compd[todo.userId] === undefined) {
        compd[todo.userId] = 1;
      } else if (todo.compd) {
        compd[todo.userId] += 1;
      }
    });
    console.log(compd);
  }
});
