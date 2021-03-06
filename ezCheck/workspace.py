# -*- coding: utf-8 -*-

' ezCheck workspace module '

__author__ = 'Yicas-3111'

import time

class EzCheck(object):
    def __init__(self, open=True, show_step=False, show_timer=False, show_type=False):
        self.step = 1
        self.show_step = show_step

        self.target_list = ()

        self.check_stat = open
        self.show_type = show_type

        self.timer = show_timer
        self.time_now = 0

    def get_name(self, obj):
        namespace = globals()
        return [name for name in namespace if namespace[name] is obj]

    def time_main(self):
        if not self.timer:
            return
        if self.time_now == 0:
            print("timer: <0.01", end="  ||  ")
            self.time_now = time.time()
            return
        time_temp = time.time() - self.time_now
        print("timer:", "%.3f" % time_temp, end="  ||  ")
        self.time_now = time.time()
        return

    def check(self, *target_list):
        if not self.check_stat:
            return
        if self.show_step:
            print(self.step, end="  -->  ")
            self.step += 1
        self.time_main()
        self.target_list = target_list
        for i in self.target_list:
            target_name = self.get_name(i)
            target_content = i
            print(target_name[0], ":", target_content, end=" ")
            if self.show_type:
                print(",", type(i), end="")
            print(end="  ||  ")
        print(" ")


if __name__ == "__main__":
    a = 1
    b = 2
    list = [1, 23, 4]
    sys = EzCheck(False, show_step=False, show_timer=True, show_type=True)
    for i in range(10):
        for j in range(1231123):
            k = i*j // 989
        list.append(a)
        a += 10
        b += 20
        sys.check(a, b, list, sys)