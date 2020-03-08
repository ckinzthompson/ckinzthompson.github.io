---
layout: posts
author: Colin Kinz-Thompson
title: Speed Up Python Code Using .C
date: 2016-02-13
---

Vectorized Python code using Numpy can be very fast, however it is not always possible to avoid using slow for-loops in your program. However, if you can write a few lines in .C, there is an easy way to integrate perform the for-loops using C code, and still use Python for the rest of your program.

You can do this by writing a wrapper for the C program in Python using Ctypes. The C program can then be called directly from your Python program.

Here I'll show you how to do this with a silly for loop based calculation. Let's say that you wanted the cumulative product of a vector, x. Numpy already has a cumulative sum function, and you could use that to perform a fast vectorized calculation all in Python instead of a slow for-loop based calculation

{% highlight python %}
import numpy as np

def cprod_slow(x):
	y = np.zeros_like(x)
	y[0] = x[0]
	for i in range(np.size(x)-1):
		y[i+1] = y[i]*x[i+1]
	return y

def cprod_fast(x):
	y = np.cumsum(np.log(x))
	return np.exp(y)
{% endhighlight %}

But what if your particular calculation didn't vectorize easily? How could we take our vector x in Python and use for-loops for a fast calculation? Well in .C we could have pointers to an input and output vector, and do

{% highlight C %}
// Function prototype
void cprod(int npoints, double *input_vector, double *output_vector);

// Actual function
void cprod(int npoints, double *input_vector, double *output_vector){
	output_vector[0] = input_vector[0];

	for (int i=0; i < npoints - 1; i++){
		output_vector[i+1] = output_vector[i]*input_vector[i+1];
	}
}
{% endhighlight %}

Then this file, cprod.c, could be compiled using GCC in a terminal with

{% highlight console %}
gcc -shared -o cprod.so -fPIC -O3 cprod.c
{% endhighlight %}

to create a library called cprod.so. Python's C-Types can be used to load this library and call it from inside a Python program. Here's an example of how to create a wrapper function to do that for either a Mac or Linux computer

{% highlight python %}
import numpy as np
from os import path as _path
from sys import platform as _platform
import ctypes as _ctypes

### Try to load compiled .C library
# Assuming the .so is in the same folder as this .py file
try:
	_libpath = _path.dirname(_path.abspath(__file__))
	if _platform == 'darwin':
		_sopath = _libpath+'/cprod'
	elif _platform == 'linux' or _platform == 'linux2':
		_sopath = _libpath + '/cprod'
	_lib = np.ctypeslib.load_library(_sopath, '.')

	#Setup the .C cumulative product function calls/returns
	_c_cprod = _lib.cprod
	_c_cprod.restype = _ctypes.c_void_p
	_c_prod.argtypes = [
		_ctypes.c_int,
		np.ctypeslib.ndpointer(dtype = np.double),
		np.ctypeslib.ndpointer(dtype = np.double)]

	def _cprod(x):
		# x is a numpy array
		x = x.astype('double')
		y = np.zeros_like(x,dtype='double')
		n = np.size(n)
		_c_cprod(n,x,y)
		return y

	cprod = _cprod

	_clibflag = True
	print "Loaded integrand written in C"
	print _sopath

### Failure: Use the Python version
except:
	def cprod_slow(x):
		y = np.zeros_like(x)
		y[0] = x[0]
		for i in range(np.size(x)-1):
			y[i+1] = y[i]*x[i+1]
		return y

	cprod = _cprod_slow
	_clibflag = False
	print "Couldn't find the compiled library"
	print "Using cprod written in Python \n    This will be much slower!"
{% endhighlight %}

Now you can call cprod(x) in Python, and if it was able to find the compiled .C library, cprod should be much faster even with the for-loops.
