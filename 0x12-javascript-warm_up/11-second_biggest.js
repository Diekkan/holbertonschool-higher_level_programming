#!/usr/bin/node

const myList = [];
if (parseInt(process.argv[2])) {
  if (parseInt(process.argv[4])) {
    for (let i = 2, j = 0; process.argv[i]; i++, j++) {
      myList[j] = parseInt(process.argv[i]);
    }
    myList.sort((a, b) => b - a);
    console.log(myList[1]);
  } else {
    console.log('0');
  }
} else {
  console.log('0');
}
