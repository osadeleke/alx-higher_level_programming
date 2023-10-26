#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

const idMovie = parseInt(process.argv[2]);

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  for (let i = 1; i < data.results.length + 1; i++) {
    if (i === idMovie) {
      console.log(data.results[i - 1].title);
    }
  }
  if (error) {
    console.error(error);
  }
});
