#!/usr/local/bin/python

class Worker:
    age = 0
    name = ''
    __weight = 0
    __status = 10

    def Out(self):
        print "Name: ", self.name
        print "Age:", self.age

    def In(self):
        print 'Type info:'
        self.name = raw_input("\tName: ")
        self.age = int(raw_input("\tAge: "))

    def get_weight(self):
        return self.__weight

    def eat(self, kg):
        print "Weight before eat: ", self.__weight
        if kg > 10 :
            self.age += 1
            self.__weight += kg/2
            print "Age after eat: ", self.age
        else :
            self.__weight += kg
        print "Weight after eat: ", self.__weight

    def UpdateStt(self, stt, time):
        print ("Status before " + stt + ": "), self.__status
        if stt == "walk" :
            self.__status += time
        elif stt == "dance" :
            self.__status += time * 2
        elif stt == "work" :
            if time > (self.__status/2) :
                self.__status = 0;
                print 'I died from overwork!'
            else :
                self.__status -= time * 2
        print ("Status after " + stt + ": ") , self.__status


wrk = Worker()
wrk.name = "Boo"
wrk.age = 3
wrk.Out()
wrk.__weight = 10
print "Changeweight: ", wrk.__weight 
print "Get__weight: ", wrk.get_weight()
wrk.eat(2)
wrk.eat(3)
wrk.eat(15)
wrk.UpdateStt("walk", 2)
wrk.UpdateStt("dance", 2)
wrk.UpdateStt("work", 10)
wrk.In()

