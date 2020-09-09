from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
db=SQLAlchemy()

#  this is the node class for the commented code on Queue.
# class node(object):
#     def __init__(self, name, phone):
#         self.name = None
#         self.phone = None
#         self.next = None


#  The commented code below is to supposed to work with nodes...
# class Queue(object):
#     def __init__(self):
#         self._head = None
#         self._tail = None

#     def enqueue(self, new_node):
#         if self._head = None:
#             self._head = new_node
#             self._tail = new_node
#             return
#         _tail.next = new_node
#         _tail = new_node
#         return
        

#     def dequeue(self):
#         aux = self._head
#         self._head = self._head.next
#         return aux

#     def get_queue(self):
#         return self._queue

#     def size(self):
#         return len(self._queue)

# a test node
# person1 = node("Nelson", "+56977978155")

class Queue:
    def __init__(self):
        self._queue = [
            {
                "name": "Iñaki",
                "phone": "+56977978155"
            },
            {
                "name": "Luis",
                "phone": "+56977978155"
            },
            {
                "name": "Jonathan",
                "phone": "+56977978155"
            }
        ]
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'
        self.account_sid = "ACf8a0cafd3c793f2f06f67ff9c88a463b"
        self.auth_token = "0b9e5d2b3a7d0f54cafc8784c58cbab2"
        self.client = Client(self.account_sid, self.auth_token)

    def enqueue(self, item):
        queue_size = len(self._queue)
        self._queue.append(item)
        message = "You are now in the queue, there are {} people before you".format(queue_size)
        self.sendMessage(item["phone"], message)

    def dequeue(self):
        if len(self._queue) > 0:
            item = None
            if self._mode == 'FIFO':
                item = self._queue.pop(0)
            else:
                item = self._queue.pop()
            message = "Thanks for waiting! It is your turn {}".format(item["name"])
            self.sendMessage(item["phone"], message)
            return True
        else:
            return False

    def get_queue(self):
        return self._queue
        
    def size(self):
        return len(self._queue) 

    def sendMessage(self, phone, body):
        print(phone, body) 
        self.client.messages.create(
        to = phone,
        from_ = "+12569603648",
        body = body
        )

