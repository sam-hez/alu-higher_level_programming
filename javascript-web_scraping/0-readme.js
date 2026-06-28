#!/usr/bin/node
'use strict';

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  process.exit(0);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  process.stdout.write(data);
  if (data && data[data.length - 1] !== '\n') {
    process.stdout.write('\n');
  }
});
