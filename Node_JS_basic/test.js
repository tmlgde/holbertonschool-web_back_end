// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, content) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

      const lines = content.split(/\r?\n/);
      const students = lines.slice(1).filter((line) => line.trim() !== '');
      let result = `Number of students: ${students.length}\n`;

      const groups = {};
      for (const line of students) {
        const cols = line.split(',');
        const firstname = cols[0].trim();
        const field = cols[cols.length - 1].trim();
        if (!groups[field]) groups[field] = [];
        groups[field].push(firstname);
      }

      for (const [field, list] of Object.entries(groups)) {
        result += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }

      resolve(result.trim()); // important: terminer la Promise en succès
    });
  });
}

module.exports = countStudents;
