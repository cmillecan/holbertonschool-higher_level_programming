#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  const info = JSON.parse(body);
  console.log(info.title);
});
