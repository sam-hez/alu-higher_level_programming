#!/usr/bin/node
'use strict';

const request = require('request');

const url = process.argv[2];
const wedgeId = '18';

function isWedgeCharacter (character) {
  if (!character) {
    return false;
  }

  if (typeof character === 'object') {
    if (typeof character.url === 'string') {
      character = character.url;
    } else if (typeof character.id === 'number' || typeof character.id === 'string') {
      return String(character.id) === wedgeId;
    } else if (typeof character.name === 'string') {
      return character.name === 'Wedge Antilles';
    }
  }

  const value = String(character);
  if (value === wedgeId || value === `people/${wedgeId}` || value === `/people/${wedgeId}` || value === `/people/${wedgeId}/`) {
    return true;
  }

  const match = value.match(/\/people\/(\d+)\/?$/);
  return match && match[1] === wedgeId;
}

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const count = data.results.filter((film) => film.characters.some(isWedgeCharacter)).length;
  console.log(count);
});
