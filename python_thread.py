# # import queue
# # import threading

# # q = queue.Queue()

# # # class Worker(threading.Thread):
# # #     def __init__(self,name):
# # #         super().__init__()
# # #         self.name = name

# # #     def run(self):
# # #         print("sub thread start", threading.currentThread().getName())
# # #         time.sleep(3)
# # #         print("sub thread end ", threading.currentThread().getName())

# # # print("main thread start")
# # # for i in range(5):
# # #     name = f"thread {i}"
# # #     t = Worker(name)
# # #     t.start

# # # print("메인 스레드 끝")


# def worker(num):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print("스레드 {0} : 처리 완료 {1}".format(num+1, item))
#         q.task_done()

# if __name__ == "__main__":
#     num_worker_threads = 5
#     threads=[]
#     for i in range(num_worker_threads):
#         t = threading.Thread(target=worker, args=(i,))
#         t.start()
#         threads.append(t)
    
#     for item in range(20):
#         q.put(item)
    
#     q.join()

#     for i in range(num_worker_threads):
#         q.put(None)
#     for t in threads:
#         t.join()

# import threading
# import time


# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name            # thread 이름 지정

#     def run(self):
#         print("sub thread start ", threading.currentThread().getName())
#         time.sleep(1)
#         print("sub thread end ", threading.currentThread().getName())


# print("main thread start")
# for i in range(5):
#     name = "thread {}".format(i)
#     t = Worker(name)                # sub thread 생성
#     t.daemon = True
#     t.start()                       # sub thread의 run 메서드를 호출

# print("main thread end")

import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())


print("main thread start")
for i in range(5):
    name = "thread {}".format(i)
    t = Worker(name) 
    # t.daemon = True               # sub thread 생성
    t.start()                       # sub thread의 run 메서드를 호출

print("main thread end")

