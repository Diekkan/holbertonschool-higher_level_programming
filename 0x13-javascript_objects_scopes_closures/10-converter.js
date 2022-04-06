#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (n) {
    return n.toString(base);
  };
};
