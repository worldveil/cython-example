cython-example
====

Quick example of cythonizing a function. Shouldn't be taken as a model implementation - just for my own reference. 

Example taken from the official [Cython tutorial](http://docs.cython.org/src/tutorial/cython_tutorial.html).

## Coding

Everything needed is in `primes.pyx`. 

The corresponding pure Python function is located in `primes_py.py`.

## Running

There are two ways to run. 

1. Compiling automatically using `pyximport`
1. Manually building the extension

### Compiling automatically

Simply run:

```bash
$ python test_quick.py
Pure Python version average 0.9142 +/- 0.04769 seconds
Cython version average 0.0276 +/- 0.00300 seconds

Cython speed up: 33.120
```

### Compile into an extension

```bash
$ sh setup.sh
$ python test.py
Cython version average 1.0102 +/- 0.08426 seconds
Cython version average 0.0271 +/- 0.00164 seconds

Cython speed up: 37.217
```

### Cleaning up

```bash
$ sh reset.sh
```
