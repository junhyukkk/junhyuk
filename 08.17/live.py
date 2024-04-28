# 큐 (Queue)
"""
큐는 선입선출 구조
>> stack , top 과 비교했을 때
  front, rear 가 각각 비슷한 역할
  but front 는 rear 가 쌓여도 -1로 변하지않음
    pop 할때 front 가 마지막 삭제위치가 됨
    front 와 rear가 같아지는 순간 : 처음과 deq enq 의 마지막
"""
# ex)
'''
def enq(data):
    global rear
    if rear == Qsize-1:
        print('Q is full') # 가득차면
    else:
        rear += 1
        Q[rear] = data

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
enq(1)
enq(2)
enq(3)
enq(4)
'''
"""
# ex) dequeue
def deq():
    global front
    if front == rear:      # 비어있으면
        print('큐가 비어있음')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

print(deq())
"""

# 원형 Q
# ex)

def enq(data):
    global rear
    global front
    if (rear + 1) % cQsize == front:
        print('cQ is full')
    else:
        rear = (rear+1) % cQsize
        cQ[rear] = data

def deq():
    global front
    front = (front + 1) % cQsize 
    return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
print(cQ)
enq(4)




