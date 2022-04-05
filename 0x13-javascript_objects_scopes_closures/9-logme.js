#!/usr/bin/node
let calledtimes = 0;

exports.logMe = function (item) {
  console.log(calledtimes + ': ' + item);
  calledtimes++;
};
