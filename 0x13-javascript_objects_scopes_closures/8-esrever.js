#!/usr/bin/node

exports.esrever = function (list) {
  let len = 0;
  const rev = [];
  for (let j = 0; list[j]; j++) {
    len++;
  }
  for (let i = 0; len > 0; i++) {
    rev[i] = list[len - 1];
    len--;
  }
  return (rev);
};
