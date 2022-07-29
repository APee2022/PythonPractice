# polymorphism means same function name (but different signatures) being uses for different types.

class Ws:
    def displayinfo(self):
        print("welcome to wscubetech")
'''
   here we are calling 2 function with same name in such case 
   if we are inherting one in another and try to get both output
   but we get only the output of which object is call
   for getting both output we should use super() method
   '''
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()# if we are not using it than we get only output of IIP class not of Ws class
        print("welcome to IIP")

obj=IIP()
obj.displayinfo()