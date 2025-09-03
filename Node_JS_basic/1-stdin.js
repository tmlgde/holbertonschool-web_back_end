process.stdin.setEncoding('utf-8'); // for real string
console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (input) => {
    const name = input.trim(); // for delete /n
    console.log(`Your name is: ${name}`);
});

process.stdin.on('end', () => {
    console.log('This important software is now closing'); // end msg when stdin is close
});