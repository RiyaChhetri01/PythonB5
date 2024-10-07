#write a function to evaluate expression res = i*10 for all values betweeen 0 to n
import time
n = 100000
 #nlist=[1000 ,1234,12345,34556]

# start_time = time.time()
def wrapper_fn(func,*args,**kwargs ):
    def wrapped(*args,**kwargs):
         start_time = time.time() * 1000 #for milisecond
         #testfn(n)
         func(*args,**kwargs)
         end_time=time.time() * 1000
         diff=end_time - start_time
         print(f"execution time for n ={n} is \n {diff}")
    return (wrapped)
@wrapper_fn #the function after this will be wrapped  decorator_function
def testfn(n):
    for i in range(0,n):
        res=i * 10
@wrapper_fn
def testfn2(n):
    for i in range(0,n):
        res=i * i
    print(res)
#newWrapperFn=wrapper(testfn,n)
#newWrapperFn(n)
#execute function
#wrapper(testfn,n)
testfn2(n)
# advantage: 