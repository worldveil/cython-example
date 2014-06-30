cython-example
====

Quick example of cythonizing a function. Example taken from the official [Cython tutorial](http://docs.cython.org/src/tutorial/cython_tutorial.html).

## Coding

Everything needed is in `primes.pyx`. 

The corresponding pure Python function is located in `primes_py.py`.

## Running

There are two ways to run. 

1. Compiling automatically using `pyximport`
1. Manually building the extension

### Compiling automatically

Simply run:

```
$ python test_quick.py
```

### Compile into an extension

```
$ python test.py
```
