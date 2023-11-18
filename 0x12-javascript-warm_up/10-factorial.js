#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

let firstArgument = process.argv[2];
firstArgument = parseInt(firstArgument);
console.log(factorial(firstArgument));
