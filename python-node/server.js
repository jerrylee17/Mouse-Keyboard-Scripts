const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter email name: ', (answer) => {
    console.log(`Your email is: ${answer}`);
    rl.close();
});