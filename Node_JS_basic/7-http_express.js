const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

// Route pour la racine
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route pour /students
app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  let responseText = 'This is the list of our students\n';
  
  // Récupérer le chemin du fichier database depuis les arguments
  const database = process.argv[2];
  
  if (!database) {
    return res.send(responseText + 'Cannot load the database');
  }
  
  // Utiliser countStudents pour récupérer les données
  countStudents(database)
    .then((studentsData) => {
      responseText += studentsData;
      res.send(responseText);
    })
    .catch((error) => {
      responseText += 'Cannot load the database';
      res.send(responseText);
    });
});

// Démarrer le serveur sur le port 1245
app.listen(1245);

// Exporter l'application
module.exports = app;
