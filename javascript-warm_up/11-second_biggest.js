#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length <= 1) {
  console.log(0);
} else {
  let max = Number.NEGATIVE_INFINITY;
  let second = Number.NEGATIVE_INFINITY;
  for (let i = 0; i < args.length; i++) {
    const n = args[i];
    if (n > max) {
      second = max;
      max = n;
    } else if (n > second && n < max) {
      second = n;
    }
  }
  console.log(second === Number.NEGATIVE_INFINITY ? 0 : second);
}
