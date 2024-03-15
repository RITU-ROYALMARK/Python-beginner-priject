import time
import threading

def square_num(number):
    print("THE SQUARE OF THE NUMBER")
    for n in number:
        time.sleep(0.2)
        print(n*n)

def cube_num(number):
    print("THE CUBE OF THE NUMBER")
    for n in number:
        time.sleep(0.2)
        print(n*n*n)


arr = [2,3,4,5,6,7,8,9,10,1]
t = time.time()
# square_num(arr)
# cube_num(arr)
t1 = threading.Thread(target=square_num,args=(arr,))
t2 = threading.Thread(target=cube_num,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"THE TIME TAKEN {time.time()-t}")












































































































































