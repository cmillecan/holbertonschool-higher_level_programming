#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const filePath = process.argv[2];

request(filePath, 'utf8', (err, response) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log('code: ' + response.statusCode);
});
