# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2017
"""
Python APIs for use with IBM Streams
and IBM Bluemix Streaming Analytics service.

Python Application API for IBM Streams
--------------------------------------
Module that allows the definition and execution of streaming
applications implemented in Python. Applications use Python code to process tuples and tuples are Python objects.

Python functions as SPL operators
---------------------------------
A Python function or class can be simply turned into an SPL primitive operator
to allow SPL tuple processing using Python.

Streams Python REST API
-----------------------
Module that allows interaction with an running Streams instance or service through HTTPS REST APIs.

"""

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
