# Zero Knowledge Proof (ZKP) Protocol

This repository presents a zero-knowledge proof protocol for authentication. The protocol is based on the Chaum-Pederson algorithm, as described in the [original paper](https://www.cs.umd.edu/~waa/414-F11/IntroToCrypto.pdf) (page 377, subsection "3.2"). It allows the prover to demonstrate knowledge of the private key associated with the claimed identity by performing computations modulo p.

## Files

- `exp_auth.py`: This file executes the zero-knowledge protocol.
- `domain_parameters.py`: This file provides functions to generate domain parameters with cryptographic properties. These parameters are necessary for `auth.py`. Additionally, it has been utilised to create a spreadsheet containing a selection of suitable domain parameters.
- `large_primes.txt`: This file includes an example of domain parameters with very large primes (size 625 in base 10).

## Usage

To utilise the protocol, simply run the `exp_auth.py` file.
