#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';
const urlFinal = url.concat(`/${process.argv[2]}/`);

request(urlFinal, (error, response, body) => {
  const data = JSON.parse(body);
  if (error) {
    console.error(error);
  }
  for (const element of data.characters) {
    request(element, (errorC, responseC, bodyC) => {
      const dataC = JSON.parse(bodyC);
      if (errorC) {
        console.error(errorC);
      }
      console.log(dataC.name);
    });
  }
});
