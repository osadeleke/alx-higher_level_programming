#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const compStringSlice = url.slice(0, -5);
const compString = compStringSlice.concat('people/18/');

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  let count = 0;
  for (const elements of data.results) {
    for (const newElements of elements.characters) {
      if (newElements === compString) {
        count = count + 1;
      }
    }
  }
  console.log(count);
  if (error) {
    console.error(error);
  }
});
