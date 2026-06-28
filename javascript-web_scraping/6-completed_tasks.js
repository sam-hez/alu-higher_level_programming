#!/usr/bin/node
'use strict';

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const tasks = JSON.parse(body);
  const completedByUser = {};

  tasks.forEach((task) => {
    if (task.completed) {
      completedByUser[task.userId] = (completedByUser[task.userId] || 0) + 1;
    }
  });

  console.log(completedByUser);
});
