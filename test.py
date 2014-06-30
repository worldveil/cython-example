import timeit
import numpy as np

###
### Prerequisite: to compile the extension, you must first run
### $ sh setup.sh
###

# pure python
python_version = timeit.Timer('primes_py.primes(100)', 
					setup='import primes_py').repeat(10, 1000)
print "Pure Python version average %.4f +/- %.5f seconds" % (
	np.mean(python_version), np.std(python_version))

# cython
cython_version = timeit.Timer('primes.primes(100)', 
					setup='import primes').repeat(10, 1000)
print "Cython version average %.4f +/- %.5f seconds" % (
	np.mean(cython_version), np.std(cython_version))

print "\nCython speed up: %.3f" % (
	np.mean(python_version) / np.mean(cython_version),)
