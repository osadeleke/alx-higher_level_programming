#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error writing to the file: ${err})`);
      }
    });
  } else {
    console.error(`Error: ${error}`);
  }
});
