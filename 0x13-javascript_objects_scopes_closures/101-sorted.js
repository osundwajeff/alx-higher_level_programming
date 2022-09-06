#!/usr/bin/node
const dictionary = require('./101-data.js').dict;
const newDict = {};
for (const key in dictionary) {
  if (newDict[dictionary[key]] === undefined) {
    newDict[dictionary[key]] = [key];
  } else {
    newDict[dictionary[key]].push(key);
  }
}
console.log(newDict);
