# NodeJS

NodeJs is free to use




# Installing NodeJs

```
curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -;sudo yum install -y nodejs
```

## Checking nodejs version

```
thor@host01 ~$ node --version
v14.21.3
```


### Example of NodeJs code

```
thor@host01 /home$ cat add.js 
// Returns addition of two numbers
let add = function (a, b) {
  return a+b;
};

const a = 10, b = 5;
console.log("Addition : "+ add(a,b));
```


### Running a NodeJs code

```
thor@host01 /home$ node add.js 
Addition : 15
```



## NPM

NPM is Node Package managment system

```
thor@host01 ~$ npm help

Usage: npm <command>

where <command> is one of:
    access, adduser, audit, bin, bugs, c, cache, ci, cit,
    clean-install, clean-install-test, completion, config,
    create, ddp, dedupe, deprecate, dist-tag, docs, doctor,
    edit, explore, fund, get, help, help-search, hook, i, init,
    install, install-ci-test, install-test, it, link, list, ln,
    login, logout, ls, org, outdated, owner, pack, ping, prefix,
    profile, prune, publish, rb, rebuild, repo, restart, root,
    run, run-script, s, se, search, set, shrinkwrap, star,
    stars, start, stop, t, team, test, token, tst, un,
    uninstall, unpublish, unstar, up, update, v, version, view,
    whoami

npm <command> -h  quick help on <command>
npm -l            display full usage info
npm help <term>   search for help on <term>
npm help npm      involved overview

Specify configs in the ini-formatted file:
    /home/thor/.npmrc
or on the command line via: npm <command> --key value
Config info can be viewed via: npm help config

npm@6.14.4 /usr/lib/node_modules/npm
```

### NPM version

```
thor@host01 ~$ npm -v
6.14.4
```

### NPM search package

```
thor@host01 ~$ npm search file
NAME                      | DESCRIPTION          | AUTHOR          | DATE       | VERSION  | KEYWORDS
file                      | Higher level path…   | =aconbere       | 2014-02-21 | 0.2.2    |         
File                      | HTML5 FileAPI…       | =coolaj86 =narf | 2014-10-24 | 0.10.2   | html5 jsdom file-api file
fs-extra                  | fs-extra contains…   | =jprichardson…  | 2023-03-20 | 11.1.1   | fs file file system copy directory extra mkdirp mkdir m
dotenv                    | Loads environment…   | =~jcblw…        | 2023-06-17 | 16.3.1   | dotenv env .env environment variables config settings
resolve                   | resolve like…        | =ljharb         | 2023-04-05 | 1.22.2   | resolve require node module
chokidar                  | Minimal and…         | =es128…         | 2022-01-18 | 3.5.3    | fs watch watchFile watcher watching file fsevents
memfs                     | In-memory…           | =streamich      | 2023-06-26 | 4.2.0    | fs filesystem fs.js memory-fs memfs file file system mo
jsonfile                  | Easily read/write…   | =jprichardson…  | 2020-10-31 | 6.1.0    | read write file json fs fs-extra
replace-in-file           | A simple utility to… | =adamreisnz     | 2023-05-28 | 7.0.1    | replace text contents file
open                      | Open stuff like…     | =sindresorhus   | 2023-03-26 | 9.1.0    | app open opener opens launch start xdg-open xdg default
papaparse                 | Fast and powerful…   | =mholt =pokoli  | 2023-03-23 | 5.4.1    | csv parser parse parsing delimited text data auto-detec
form-data                 | A library to create… | =mikeal…        | 2021-02-15 | 4.0.0    | 
file-loader               | A file loader…       | =evilebottnawi… | 2020-10-27 | 6.2.0    | webpack
execa                     | Process execution…   | =sindresorhus…  | 2023-07-27 | 7.2.0    | exec child process execute fork execfile spawn file she
find-up                   | Find a file or…      | =sindresorhus   | 2022-02-08 | 6.3.0    | find up find-up findup look-up look file search match p
file-entry-cache          | Super simple cache…  | =royriojas      | 2021-02-20 | 6.0.1    | file cache task cache files file cache key par key valu
write-file-atomic         | Write files in an…   | =npm-cli-ops…   | 2023-04-26 | 5.0.1    | writeFile atomic
tmp                       | Temporary file and…  | =raszi          | 2020-04-29 | 0.2.1    | temporary tmp temp tempdir tempfile tmpdir tmpfile
micromatch                | Glob matching for…   | =es128…         | 2022-03-24 | 4.0.5    | bash bracket character-class expand expansion expressio
formidable                | A node.js module…    | =felixge…       | 2023-06-28 | 3.5.0    | multipart form data querystring www json ulpoad file
```


## Installing file package with npm

```
thor@host01 ~$ npm install file
npm WARN saveError ENOENT: no such file or directory, open '/home/thor/package.json'
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN enoent ENOENT: no such file or directory, open '/home/thor/package.json'
npm WARN thor No description
npm WARN thor No repository field.
npm WARN thor No README data
npm WARN thor No license field.

+ file@0.2.2
added 1 package from 1 contributor and audited 1 package in 0.512s
found 0 vulnerabilities
```


```
thor@host01 ~$ npm info file

file@0.2.2 | MIT | deps: none | versions: 4
Higher level path and file manipulation functions.
https://github.com/aconbere/node-file-utils

dist
.tarball: https://registry.npmjs.org/file/-/file-0.2.2.tgz
.shasum: c3dfd8f8cf3535ae455c2b423c2e52635d76b4d3
.integrity: sha512-gwabMtChzdnpDJdPEpz8Vr/PX0pU85KailuPV71Zw/un5yJVKvzukhB3qf6O3lnTwIe5CxlMYLh3jOK3w5xrLA==

maintainers:
- aconbere <aconbere@gmail.com>

dist-tags:
latest: 0.2.2  

published over a year ago by aconbere <aconbere@gmail.com>
```


### Inspecting the file package.json file

```
thor@host01 ~/node_modules/file$ pwd
/home/thor/node_modules/file


thor@host01 ~/node_modules/file$ cat package.json 
{
  "_from": "file",
  "_id": "file@0.2.2",
  "_inBundle": false,
  "_integrity": "sha512-gwabMtChzdnpDJdPEpz8Vr/PX0pU85KailuPV71Zw/un5yJVKvzukhB3qf6O3lnTwIe5CxlMYLh3jOK3w5xrLA==",
  "_location": "/file",
  "_phantomChildren": {},
  "_requested": {
    "type": "tag",
    "registry": true,
    "raw": "file",
    "name": "file",
    "escapedName": "file",
    "rawSpec": "",
    "saveSpec": null,
    "fetchSpec": "latest"
  },
  "_requiredBy": [
    "#USER",
    "/"
  ],
  "_resolved": "https://registry.npmjs.org/file/-/file-0.2.2.tgz",
  "_shasum": "c3dfd8f8cf3535ae455c2b423c2e52635d76b4d3",
  "_spec": "file",
  "_where": "/home/thor",
  "author": {
    "name": "Anders Conbere",
    "email": "aconbere@gmail.com"
  },
  "bugs": {
    "url": "http://github.com/aconbere/node-file-utils"
  },
  "bundleDependencies": false,
  "deprecated": false,
  "description": "Higher level path and file manipulation functions.",
  "devDependencies": {
    "mocha": "1.9.x"
  },
  "directories": {
    "lib": "lib"
  },
  "homepage": "https://github.com/aconbere/node-file-utils#readme",
  "license": "MIT",
  "main": "./lib/file",
  "name": "file",
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/aconbere/node-file-utils.git"
  },
  "tags": [
    "file",
    "path",
    "fs",
    "walk"
  ],
  "version": "0.2.2"
}
```


## Installing file package module globally with npm 

```
thor@host01 ~/node_modules/file$ sudo npm install file -g
+ file@0.2.2
added 1 package from 1 contributor in 0.322s
```

### Packages npm default dir

```
thor@host01 /usr/lib/node_modules/npm/node_modules$ pwd
/usr/lib/node_modules/npm/node_modules
```



## Downloading example-app.nodejs app

```
thor@host01 /usr/lib/node_modules/npm/node_modules$ cd /home/thor/; git clone https://github.com/contentful/the-example-app.nodejs
Cloning into 'the-example-app.nodejs'...
remote: Enumerating objects: 2935, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 2935 (delta 12), reused 2 (delta 0), pack-reused 2914
Receiving objects: 100% (2935/2935), 6.81 MiB | 0 bytes/s, done.
Resolving deltas: 100% (1770/1770), done.
```


### Inspecting the app downloaded

```
thor@host01 ~/the-example-app.nodejs$ pwd
/home/thor/the-example-app.nodejs
thor@host01 ~/the-example-app.nodejs$ cat package.json 
{
  "name": "example-contentful-theExampleApp-js",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start:watch": "nodemon ./bin/www --ignore public/",
    "start:dev": "node ./bin/www",
    "debug": "node debug ./bin/www",
    "start": "NODE_ENV=production node ./bin/www",
    "start:production": "NODE_ENV=production node ./bin/www",
    "lint": "eslint ./app.js routes",
    "format": "eslint --fix . bin --ignore public node_modules",
    "pretest": "npm run lint",
    "test": "npm run test:unit && npm run test:integration && npm run test:e2e",
    "test:e2e": "node test/run-e2e-test.js",
    "test:e2e:dev": "node test/run-e2e-test.js --dev",
    "test:integration": "jest test/integration",
    "test:integration:watch": "jest test/integration --watch",
    "test:unit": "jest test/unit",
    "test:unit:watch": "jest test/unit --watch"
  },
  "engines": {
    "node": ">=8.9.3"
  },
  "dependencies": {
    "body-parser": "^1.18.2",
    "contentful": "^6.0.0",
    "cookie-parser": "~1.4.3",
    "dotenv": "^5.0.0",
    "execa": "^0.9.0",
    "express": "^4.16.2",
    "helmet": "^3.11.0",
    "lodash": "^4.17.5",
    "marked": "^0.3.16",
    "morgan": "^1.9.1",
    "pug": "~2.0.0-beta6"
  },
  "devDependencies": {
    "cheerio": "^1.0.0-rc.2",
    "cookie": "^0.3.1",
    "eslint": "^4.18.1",
    "eslint-config-standard": "^11.0.0",
    "eslint-plugin-import": "^2.8.0",
    "eslint-plugin-node": "^6.0.0",
    "eslint-plugin-promise": "^3.6.0",
    "eslint-plugin-standard": "^3.0.1",
    "jest": "^22.4.0",
    "nodemon": "^1.18.9",
    "supertest": "^3.0.0",
    "yargs": "^11.0.0"
  }
}
```


Notice we have dependencies session. For example, helmet depends on 3.11.0


