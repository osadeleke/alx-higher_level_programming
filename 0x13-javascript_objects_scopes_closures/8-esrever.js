#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [list[list.length - 1]];
  let i;
  for (i = list.length - 2; i > -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};
