#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

let firstArgument = process.argv[2];
let nextArgument = process.argv[3];

firstArgument = parseInt(firstArgument);
nextArgument = parseInt(nextArgument);

add(firstArgument, nextArgument);
