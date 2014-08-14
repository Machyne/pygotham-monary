Our Monary talk for PyGotham
============================

[PyGotham link](http://pygotham.org/talks/50)

Description
-----------
NumPy arrays combine the speed of C with the convenience of Python. It is the
fundamental package for scientific and statistical computing in Python.
MongoDB's scale, speed, and flexibility make it ideal for storing large amounts
of data. However, the official MongoDB driver is not optimized for loading
MongoDB documents into NumPy arrays. Enter "Monary", which allows you to easily
examine and manipulate data using NumPy arrays. We will explore how Monary can
accelerate your scientific analysis while providing you with the scale and
flexibility of MongoDB and the ease of Python.

Abstract
--------
For scientists, mathematicians, and programmers concerned with data, using
MongoDB provides scale and flexibility, but can pose a problem: MongoDB stores
data as documents, so Python programmers often retrieve the data as
dictionaries. This format is prohibitive for data scientists who want to
perform MapReduce or other column-oriented operations. Of course, the data in
the dictionaries could then be copied over into a list or array, but this
doubles the amount of work and scales poorly. How can we use MongoDB and Python
with larger data sets?

The answer is Monary, a library with a simple solution: take the MongoDB
documents and copy data directly into NumPy arrays. This talk will walk through
a tutorial on using Monary, and we will offer under-the-hood explanations of
how it all works. We will also give practical demonstrations of Monary's speed
benefits and uses.
