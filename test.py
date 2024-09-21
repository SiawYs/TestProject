def example_function  (x,y):
     if x>10:
      print("X is greater than 10")
  else:
          print(   "X is 10 or less")
  for i in range( 0,10):
     if  i% 2==0:print(    f"{i} is even")
     else:
      print(f"{i} is odd") 
      return  x+y
def   another_function( a,  b ):
          if a == b:
       print("a is equal to b") ; print("This is a sample statement");
               return None
 else:
  print(    "a is not equal to b");return a -b

    class SampleClass :
 def  __init__( self, value ) :
           self.value=value
          def display_value(  self  ):
             print(  "The value is",self.value)

def  main( ) :
      ex_result=example_function(10,20)
 print("Result of example_function:", ex_result)
         obj=SampleClass(   42)
    obj.display_value()
another_function(5,10)
main(   )
