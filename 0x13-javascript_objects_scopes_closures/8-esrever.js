#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length === 0) {
    return [];
  }
  const newList = [list[list.length - 1]];
  let i;
  for (i = list.length - 2; i > -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};
