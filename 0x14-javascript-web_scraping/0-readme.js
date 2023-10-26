#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
const filePath = args[0];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
