#!/usr/bin/node
let firstArgument = process.argv[2];
if (!firstArgument || isNaN(firstArgument)) {
  console.log('Missing size');
} else {
  firstArgument = parseInt(firstArgument);
  for (let i = 0; i < firstArgument; i++) {
    console.log('X'.repeat(firstArgument));
  }
}
