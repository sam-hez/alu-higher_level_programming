#!/usr/bin/node
'use strict';

const request = require('request');

const url = process.argv[2];
const wedgeId = '18';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const count = data.results.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)).length;
  console.log(count);
});
