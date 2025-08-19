🧭 C’est quoi ce projet ?

Un petit projet d’initiation à ES6 (ECMAScript 2015), la grande mise à jour de JavaScript.
Objectif : écrire du JS moderne (plus clair, plus sûr) et le tester/linter proprement.

Concept clef à connaître : Software Linter (ESLint).

🤔 ES6 en deux mots

ES6 ajoute notamment :

let / const (portée de bloc)

Fonctions fléchées () => {} (+ this lexical)

Paramètres par défaut, rest (...args) et spread (...arr)

Template strings `Hello ${name}`

Itérables + boucle for...of

Objets “modernes” (syntaxe raccourcie, méthodes)

Modules export / import

🎯 Ce que tu vas apprendre

Déclarer correctement variables et constantes

Écrire des fonctions fléchées et utiliser des paramètres par défaut

Manipuler rest/spread

Utiliser les template strings

Parcourir des données avec for...of et les itérateurs

Structurer ton code avec des modules

Tester (Jest) et linter (ESLint) ton code

🧱 Prérequis & règles du projet

Ubuntu 20.04 LTS, Node 20.x.x, npm 9.x.x

Éditeurs autorisés : vi, vim, emacs, VS Code

Tous les fichiers se terminent par une nouvelle ligne

Extension : .js

Tests : Jest

Linter : ESLint (règles spécifiques fournies)

Toutes les fonctions doivent être exportées

Un README.md à la racine est obligatoire

⚡️ Démarrage rapide
1) Installer Node 20 & npm 9
cd ~
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install -y nodejs

node -v
npm -v
# si besoin de npm 9 :
sudo npm i -g npm@9

2) Créer le dossier du projet et init npm
mkdir ES6_basic && cd ES6_basic
npm init -y

3) Installer les outils du projet
# Tests
npm install --save-dev jest
# Transpilation ES6 pour Jest/Node
npm install --save-dev babel-jest @babel/core @babel/preset-env
# Linter
npm install --save-dev eslint

4) Ajouter les fichiers de config

Créer à la racine :

package.json (avec les scripts de test/lint/build)

babel.config.js

.eslintrc.js

Une fois les configs en place :

npm install

5) (Conseillé) .gitignore
node_modules/
dist/
coverage/

🧪 Mini test express (pour valider l’environnement)

src/sum.js

export default function sum(a = 0, b = 0) {
  return a + b;
}


src/sum.test.js

import sum from './sum.js';

test('sum adds numbers', () => {
  expect(sum(2, 3)).toBe(5);
});

test('sum default params', () => {
  expect(sum()).toBe(0);
});


Lancer :

npm test

🗂️ Structure suggérée
ES6_basic/
├─ src/
│  ├─ index.js
│  └─ utils/
├─ __tests__/           # ou fichiers *.test.js à côté des sources
├─ .eslintrc.js
├─ babel.config.js
├─ package.json
├─ README.md
└─ .gitignore

🛠️ Scripts utiles (exemples)
npm test           # lancer Jest
npm run test:watch # relancer les tests en continu
npm run lint       # analyser avec ESLint
npm run lint:fix   # corriger automatiquement si possible
npm run build      # transpiler le code vers ./dist (si configuré)

📚 Ressources à consulter

ECMAScript 6 — ECMAScript 2015

Statements and declarations

Arrow functions

Default parameters

Rest parameter

JavaScript ES6 — Iterables and Iterators

✅ Rappels importants

N’exporte pas le dossier node_modules/ dans Git

Utilise let/const (évite var)

Exporte toutes tes fonctions

Respecte les règles ESLint fournies par le projet