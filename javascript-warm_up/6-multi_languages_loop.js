#!/usr/bin/node

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let out = '';

for (let i = 0; i < languages.length; i++) {
  out += languages[i] + (i === languages.length - 1 ? '' : '\n');
}

console.log(out);
