#!/usr/bin/env python
# *-*coding: UTF-8 *-*
#######################################
#File Name: multi_smm.py
#Created Time: 2016-05-08 23:06:16
#######################################

from multiprocessing import Process, Manager
import time, random
import Queue


def use(d):
    while True:
        print 'use'
        print d
        print '*' * 20
        time.sleep(1)

def update(d):
    print 'enter'
    for i in range(10):
        d[i] = i + 100
        time.sleep(1)
        #print '*' * 100
        #print d
        #print '*' * 100
    print 'exit update'


def useQ(q):
    while True:
        if not q.empty():
            print q.get()
        time.sleep(1)


def upQ(q):
    while True:
        i = random.randint(1, 10)
        print 'add %d ' % i
        if not q.full():
            q.put(i)
        time.sleep(1)

if __name__ == '__main__':
    manager = Manager()
    #manager = myQueue()


    #d = manager.dict()
    d = manager.Queue()

    jobs = []

    u = Process(target=useQ, args=(d,))
    u.start()

    #up = Process(target=upQ, args=(d,))
    #up.start()


    upQ(d)
    #time.sleep(10)
    #print 'exit main'
    #print d

