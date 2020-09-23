#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 3) {
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log(data);
});
