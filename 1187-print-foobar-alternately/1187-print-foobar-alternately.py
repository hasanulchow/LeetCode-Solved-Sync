from threading import Barrier, Lock #, Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.b = Barrier(2)
        self.l = Lock() # Semaphore(1)
        self.l.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.l.release()
            self.b.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.l:
                printBar()
            self.b.wait()
            self.l.acquire()