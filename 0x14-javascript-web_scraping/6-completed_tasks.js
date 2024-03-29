#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const dictCompleted = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const element of data) {
    if (!(element.userId in dictCompleted)) {
      if (element.completed === true) {
        dictCompleted[element.userId] = 1;
      }
    } else {
      if (element.completed === true) {
        dictCompleted[element.userId] = dictCompleted[element.userId] + 1;
      }
    }
  }
  console.log(dictCompleted);
});
