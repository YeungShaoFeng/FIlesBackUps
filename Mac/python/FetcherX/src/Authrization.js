const CryptoJS = require('../lib/CryptoJS');

// len: 64
let Auth = () => CryptoJS.AES.encrypt(Date.now() + "\b\xa7", "650219").toString();
let DeAuth = (cipher) => CryptoJS.AES.decrypt(cipher, "650219").toString();
//--T
// console.log(DeAuth("U2FsdGVkX19J+8LXbY5dXxh0m6/8j6PS3c3GKLa5hQUXhDv3SaalVbaZgwq1QUCp"))
// let auth = Auth();
// let plain = DeAuth(auth)

// console.log("*******************************");
// console.log(auth);
// console.log(plain);
// console.log(DeAuth("U2FsdGVkX1+fhwodPQeO4c3tFiOs+1CCoyCrKggkq3sXTIntwz15ce0g0MLQcQrN"));
// console.log("-------------------------------");


// len: 44
// NOW = Date.now();
// console.log(NOW);

// let CreateCipherT = (NOW) => CryptoJS.AES.encrypt(NOW + "\b\xa7", "650219").toString();

// cipherT = CreateCipherT();
// plainT = DeAuth(cipherT) 

// console.log(cipherT);
// console.log(plainT);
// console.log("*******************************");
//--T
