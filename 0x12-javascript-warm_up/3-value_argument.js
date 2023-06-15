#!/usr/bin/node
const first_argument = process.argv.slice(2).every(arg => arg.startsWith('_')); 
if (!first_argument){
	console.log('No argument');
}	else{
	console.log('first_argument');
}
