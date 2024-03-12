#!/usr/bin/node
exports.esrever = function (list) {
  let aang = list.length - 1;
  let kora = 0;
  while ((aang - kora) > 0) {
    const temp = list[aang];
    list[aang] = list[kora];
    list[kora] = temp;
    kora++;
    aang--;
  }
  return list;
};
