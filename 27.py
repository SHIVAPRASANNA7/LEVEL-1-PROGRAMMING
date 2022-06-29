import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("CSK", "MI", "RCB", "SRH", "DC", "RR")
Tuple3 = ((1, "VILLUPURAM"), ( 2, "PONDY"), (3, "NEYVELI"), (4, "CHENNAI"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")
