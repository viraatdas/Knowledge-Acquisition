main resource [[Introduction_to_Modern_Cryptography.pdf]]


## Chapter 1: Introduction and classical ciphers

### Setting of Private-key encryption
- setting in which communicating parties share some secret information in advance is [[private-key]] (or symmetric-key) setting

**The syntax of encryption**
Private-key encryption scheme
- *key-generation algorithm*: `Gen` is a probabilistic algorithm that outputs a key `k` chosen according to some distribution 
- *encryption algorithm*: `Enc` take as a input a key `k` and a plantext `m` and outputs a ciphertext `c`  -> $Enc_k(m)$
- *decryption algorithm*: `Dec` takes input a key `k` and ciphertext `c` and outputs a plaintext `m` -> $Dec_k(c)$

