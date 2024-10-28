"""
to sprawdza czy jest dobry wynik z sha1.py
"""

import hashlib

doc1 = "abcabc123"
doc2 = "KTzkOvvzVj"
print(hashlib.sha1(doc1.encode()).hexdigest())
print(hashlib.sha1(doc2.encode()).hexdigest())
