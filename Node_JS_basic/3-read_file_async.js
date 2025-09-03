function countStudents(path) {
return new Promise((resolve, reject) => { // return a new promise with the csv file
    const fs = require('fs'); // module here for the promise

    fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
        reject(new Error('Cannot load the database'));
        return;
    }

    const lines = data.split('\n');
    const cleanLines = lines.filter(line => line.trim() !== '');
    const rows = cleanLines.slice(1);
    const students = rows.map(line => line.split(','));

    const totalStudents = students.length;
    console.log(`Number of students: ${totalStudents}`);

    const fields = {}; // same step of exo 2
    for (const student of students) {
        const firstname = student[0];
        const field = student[3];
        if (!fields[field]) {
        fields[field] = [];
        }
        fields[field].push(firstname);
    }

    for (const fieldName of Object.keys(fields)) {
        const names = fields[fieldName].join(', ');
        console.log(`Number of students in ${fieldName}: ${fields[fieldName].length}. List: ${names}`);
    }
    resolve(); // iùportant for the end of the promise
    });
});
}

module.exports = countStudents;
