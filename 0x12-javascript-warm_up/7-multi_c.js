#!/usr/bin/node
let firstArgument = process.argv[2];
if (!firstArgument || isNaN(firstArgument)) {
  console.log('Missing number of occurrences');
} else {
  firstArgument = parseInt(firstArgument);
  for (i = 0; i < firstArgument; i++) {
  console.log('C is fun');
  }
}
