import time
class timer:
        start=0
        end=0
        counter=0
        def timer_f(self,para):
                if para==0:
                        timer.start=time.time() 
                        timer.end=0
                if para==1:
                        timer.end=time.time()
                        timer.counter+=timer.end-timer.start
                        timer.start=0

        def print_time(self):
                print timer.counter


