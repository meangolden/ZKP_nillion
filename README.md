
# Zero Knoweldge Proof (ZKP) Protocol

This repository contains the outline of a zero-knowledge proof protocol for authentication.
The protocol is a modified code of the Chaum-Pederson
(https://www.cs.umd.edu/~waa/414-F11/IntroToCrypto.pdf page 377,subsection "3.2.
whereby the prover demonstrates knowledge of the private key corresponding to
the claimed identity through a series of computations mod p.

## Files

- `exp_auth.py`: This file runs the zero knowledge protocol. 
- `domain_parameters.py`: This file contains functions to generate domain parameters with cryptographic properties. These parameters are needed for `auth.py`. Additionally, it has been used to create a spreadsheet with a list of appropriate domain parameters. 
- `large_primes.txt`: This file contains a case of very large domain parameters (primes of size 625 base 10). 

## Usage

To use the protocol, simply run the `exp_auth.py` file.


