#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  let count = 0;
  for (const elements of data.results) {
    for (const newElements of elements.characters) {
      if (newElements.slice(-3) === '18/') {
        count = count + 1;
      }
    }
  }
  console.log(count);
  if (error) {
    console.error(error);
  }
});
