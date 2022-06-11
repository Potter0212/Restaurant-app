# 식당 대기 프로그램 [ 큐 구현 ]
# 1. enQueue
def enQueue(data):
    global SIZE, front, rear
    if isQueueFull():
        print("현재 대기 인원이 모두 찼습니다.")
        return
    rear += 1           # 입구 인덱스 증가
    queue[rear] = data  # 입구에 대이터 증가

# 2. deQueue
def deQueue():
    global SIZE, front, rear
    if isQueueEmpty():
        print("대기 인원이 없습니다.")
        return None
    front += 1             # 출그 인덱스 증가
    data = queue[front]
    queue[front] = None    # 출구에 대이터 추출
    # 데이터 추출시 한칸씩 당기기
    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    # 출구는 항상 -1 이어야 한다.
    front = -1
    # 입구는 한칸 앞으로 당긴다.
    rear -= 1
    return data

# 3. peek
def peek():
    global SIZE, front, rear
    if isQueueEmpty():
        print("대기 인원이 없습니다.")
        return None
    print("곧 입장할 고객 : ", queue[front+1])
    return None

# 4. isQueueFull
def isQueueFull():
    global SIZE, front, rear
    if rear == SIZE-1: # 만약에 입구번호가 최대 길이보다 크면
        return True
    else:
        return False

# 5. isQueueEmpty
def isQueueEmpty():
    global SIZE, front, rear
    if front == rear: # 입구와 출구가 -1이면 큐 안에 데이터 존재 X
        return True
    else:
        return False

# 0. 전역변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# 프로그램 실행
while True:
    select = int(input("1. 대기등록 2. 입장 3.종료 선택 : "))
    if select == 1:
        print("대기등록")
        phone = input("전화번호 : ")
        count = input("인원 수 : ")
        enQueue((phone, count))
        print("현재 대기 상태 : ", queue)
        print("고객님의 대기 번호는 ", rear+1, "번 입니다.")
    elif select == 2:
        print("입장")
        deQueue()
        print("현재 대기 상태 : ", queue)
        peek()
    elif select == 3:
        print("종료")
        break
    else:
        print("알 수 없는 번호입니다.")