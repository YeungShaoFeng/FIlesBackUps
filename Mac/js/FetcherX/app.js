const CryptoJS = require('./CryptoJS');

NOW = Date.now();
console.log(NOW);

let CreateCipherT = (NOW) => CryptoJS.AES.encrypt(NOW + "\b\xa7", "650219").toString();
let DeCipher = cipher=> CryptoJS.AES.decrypt(cipher, "650219").toString();

cipherT = CreateCipherT();
plainT = DeCipher(cipherT) 

console.log(cipherT);
console.log(plainT);

// U2FsdGVkX1+ar/SFsAZNDIEu1x1jGDv6QXjMjIdix1nDexlRbVOP+Zg2KWiB+t+C
// Web:
// U2FsdGVkX1+fhwodPQeO4c3tFiOs+1CCoyCrKggkq3sXTIntwz15ce0g0MLQcQrN

console.log(DeCipher("U2FsdGVkX1+fhwodPQeO4c3tFiOs+1CCoyCrKggkq3sXTIntwz15ce0g0MLQcQrN"));
console.log(DeCipher("U2FsdGVkX1+ar/SFsAZNDIEu1x1jGDv6QXjMjIdix1nDexlRbVOP+Zg2KWiB+t+C"));
