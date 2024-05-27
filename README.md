# RSA Attack

This project is a Python implementation of an RSA attack using the factoring method. It includes the implementation of the Montgomery Ladder algorithm, the Miller-Rabin primality test, and the quadratic sieve for factorization.

## Getting Started
### Dependencies
- Python 3.x
- gmpy2
- sympy


### Installing
Clone the repository using the following command:

```bash
git clone https://github.com/01-00-11-00/shiffy-128.git
```

Install the required packages using the following command:

```bash
pip install gmpy2 sympy
```

### Usage

To use this project, run the main.py script. The script performs a series of tests and then encrypts a test message with a given key. The encrypted message is stored in a binary file. The binary file is then read, and the message is decrypted using the same key. The script outputs the decrypted message.
Run the main.py file with the following command:

```bash
python main.py
```

The program will prompt you to enter the public key 'e', the public key 'n', and the encrypted message. It will then perform a factoring attack on the RSA encrypted message and print the decrypted message.

## Authors
01-00-11-00

ex. [@01-00-11-00](https://github.com/01-00-11-00)

## Version History
- 0.1
    - Initial Release