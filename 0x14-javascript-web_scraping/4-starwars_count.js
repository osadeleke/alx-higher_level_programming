#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  let count = 0;
  for (const elements of data.results) {
    for (const newElements of elements.characters) {
      if (newElements === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count = count + 1;
      }
    }
  }
  console.log(count);
  if (error) {
    console.error(error);
  }
});
