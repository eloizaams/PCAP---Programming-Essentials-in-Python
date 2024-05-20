class QueueError(IndexError):  
   pass



class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.insert(0,elem)


    def get(self):
        try:
            val = self.__queue_list[-1]
            del self.__queue_list[-1]
            return val
        except:
            raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    
    
