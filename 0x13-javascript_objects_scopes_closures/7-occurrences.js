#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, pos) => pos === searchElement ? count + 1 : count, 0);
};
