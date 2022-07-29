w = "welcome {} to {} wscubetech".format("hello",20)
print(w)
#here automatic hello is print first than 20 print in curly braces

w = "welcome {1} to {0} wscubetech".format("hello",20)
print(w)
#here 20 print first and hello print later because hello is at 0 index and 20 at 1 index

w = "welcome {b} to {a} wscubetech".format(a=50,b=90)
print(w)

w = "welcome {b:^10} to {a} wscubetech".format(a=50,b=90)
print(w)
# {b:10} means w printed within 10 space character
# {b:^10} w printed in center in between 10 space character
# {b:<10} w printed left side within 10 space character
# {b:>10} w printed right side within 10 space character