# Cryptography-Project-1
Project 1 for Cryptography course.

Creation of custom encryption and decryption algorithm that works as follows:
1- An initial key is exchanged based on a mono-alphabetic initial substitution table (configuration) that is shared between the two communicating parties.
2- Encryption is done by substituting the first plain text letters with cipher text letters according to the initial configuration.
3- The second letter is substituted based on the Caesar Cipher shift that depends on the value of the previous letter.
4- The Third letter is again substituted using mono-alphabetic cipher as in step-1.
5- The fourth letter is again done based on the same process explain in step-3 and so on.
