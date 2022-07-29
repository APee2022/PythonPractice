'''
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class.
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.
'''
#example

def div(a,b):
    print(a/b)

def smart_div(func):#Decorator for function div

     def inner(a,b):
         if a<b:
             a,b = b,a
         return  func(a,b)
     return inner

div = smart_div(div)#here we call the modified div

div(4,2)#if i swap the value we got 0.5 as answer but we want 2 as answer
        #after swapping, which means always divide greter number than lower number.
        #position doesn't matter.
div(2,4)