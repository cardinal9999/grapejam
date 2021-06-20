# GrapeJam
GrapeJam is a Python package that can serialize Python objects into strings (like Python pickle) and make sure malware code cannot be decoded (like JSON).
Although Python pickle can encode any possible Python object, it can be used to encode malware into a string of bytes.
This is why some programmers used JSON instead. Python's JSON can encode many objects, but cannot encode malware.
JSON still can only encode strings, integers, floats, lists, booleans, and dictionaries. JSON offers security, but it doesn't offer many features.
GrapeJam solves that problem by letting sets and other built-in Python objects be encoded but doesn't allow non-built-in objects.
Here is a list of objects GrapeJam can encode:
1. bytes
2. bytearray
3. boolean
4. integer
5. string
6. list
7. tuple
8. float
9. dict
10. range
11. complex
12. set
13. frozenset
14. datetime 
<a/>
GrapeJam cannot encode Pandas DataFrames. If you want to serialize those, use Python pickle.

How to install GrapeJam: 
1. Open a terminal
2. Navigate to where you want GrapeJam to be installed
3. Type in "git clone https://github.com/cardinal9999/grapejam.git"

In the future, GrapeJam may be able to encode Pandas DataFrames or NumPy arrays.
