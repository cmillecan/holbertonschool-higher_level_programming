#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit(1);
}

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
});
