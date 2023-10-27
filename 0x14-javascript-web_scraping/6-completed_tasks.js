#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let userId = 1;
let count = 1;
let doneTask = 0;
const dictCompleted = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const element of data) {
    if (element.completed === true) {
      doneTask++;
    }
    if (count % 20 === 0) {
      if (doneTask > 0) {
        dictCompleted[`${userId}`] = doneTask;
      }
      userId++;
      doneTask = 0;
    }
    count++;
  }
  console.log(dictCompleted);
});
