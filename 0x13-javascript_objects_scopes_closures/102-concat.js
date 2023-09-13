#!/usr/bin/node

const file = require('fs');

filePathA = 'fileA';
filePathB = 'fileB';
filePathC = 'fileC';

file.readFile(filePathA, 'utf8', (err, dataA) => {
	if (err) {
		console.error(err);
		return;
	}

	file.readFile(filePathB, 'utf8', (err, dataB) => {
		if (err) {
			console.error(err);
			return;
		}
		const dataConCat = dataA + dataB;
		file.writeFile(filePathC, dataConCat, (err) => {
			if (err) {
				console.error(err);
				return;
			}
		});
	});
});
