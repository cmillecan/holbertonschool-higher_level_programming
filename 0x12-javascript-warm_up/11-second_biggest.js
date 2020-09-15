#!/usr/bin/node
const array = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  array.sort();
  console.log(array[array.length - 2]);
}
