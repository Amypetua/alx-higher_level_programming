#!/usr/bin/node
if (process.argv.slice(2).every(arg => arg.startsWith('_'))) {
	console.log('No argument');
}
