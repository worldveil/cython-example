# build the cython extension
python setup.py build_ext --inplace

# for more complex math functions like pow, this can make a difference
# https://python.g-node.org/python-summerschool-2011/_media/materials/cython/cython-slides.pdf
#OPT="-O3 -ffast-math" python setup.py build_ext --inplace