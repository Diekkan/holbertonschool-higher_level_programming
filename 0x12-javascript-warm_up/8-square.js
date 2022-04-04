#!/usr/bin/node

if (process.argv[2]) {
  if (parseInt(process.argv[2]) > 0) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      console.log('X'.repeat(parseInt(process.argv[2])));
    }
  } else if (parseInt(process.argv[2]) < 0) {
    // do nothing
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
