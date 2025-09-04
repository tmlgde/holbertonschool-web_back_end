// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split(/\r?\n/);
      const students = lines.slice(1).filter((line) => line.trim() !== '');
      
      // Construire le résultat comme une string au lieu de console.log
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
        // Ajouter à result au lieu de console.log
        result += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }
      
      // Retourner le résultat dans resolve
      resolve(result.trim());
    });
  });
}

module.exports = countStudents;
