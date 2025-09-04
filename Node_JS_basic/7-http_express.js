const express = require('express');
const fs = require('fs');

const app = express();

// Route pour la racine
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route pour /students - logique directe sans import
app.get('/students', (req, res) => {
  let responseText = 'This is the list of our students\n';
  
  const database = process.argv[2];
  
  if (!database) {
    return res.send(responseText + 'Cannot load the database');
  }
  
  // Logique directe inspirée de 3-read_file_async.js
  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      return res.send(responseText + 'Cannot load the database');
    }

    const lines = data.split(/\r?\n/);
    const students = lines.slice(1).filter((line) => line.trim() !== '');
    
    responseText += `Number of students: ${students.length}\n`;

    const groups = {};
    for (const line of students) {
      const cols = line.split(',');
      const firstname = cols[0].trim();
      const field = cols[cols.length - 1].trim();
      if (!groups[field]) groups[field] = [];
      groups[field].push(firstname);
    }
    
    for (const [field, list] of Object.entries(groups)) {
      responseText += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
    }
    
    res.send(responseText.trim());
  });
});

// Démarrer le serveur sur le port 1245
app.listen(1245);

// Exporter l'application
module.exports = app;
