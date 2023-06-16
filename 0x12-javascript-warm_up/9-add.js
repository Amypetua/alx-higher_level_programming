#!/usr/bin/node
function add (a, b) {
console.log(a + b);
}

let firstArgument = process.argv[2];
let secondArgument = process.argv[3];

firstArgument = parseInt(firstArgument);
secondArgument = parseInt(secondArgument);

add(firstArgument, secondArgument);
