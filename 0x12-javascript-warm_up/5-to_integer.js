#!/usr/bin/node
let firstArgument = process.argv[2];
if (!firstArgument || isNaN(firstArgument)) {
  console.log('Not a number');
} else {
  firstArgument = parseInt(firstArgument);
  console.log('My number: ' + firstArgument);
}
