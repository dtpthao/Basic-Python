
class Triangle:
    side = 5
    agles = [30, 60]
    
    def changeangle(self, index, percent):
        if index >= 0 and index < 2:
            tmp = self.agles[index] * percent/100 + self.agles[index]
            if (tmp + self.agles[index ^ 1]) < 180 :
                print 'angle before change: ', self.agles[index]
                self.agles[index] = tmp
                print 'angle after change: ', self.agles[index]
            else :
                print 'Invalid sum of angles'
        else :
            print 'Invalid index'
    
    def high(self):
        import math
        pi1 = self.agles[0] * math.pi/180
        ctg1 = math.cos(pi1) / math.sin(pi1)
        pi2 = self.agles[1] * math.pi/180
        ctg2 = math.cos(pi2) / math.sin(pi2)
        return float(self.side/(ctg1 + ctg2))

    def otherside(self):
        import math
        high = self.high()
        print 'Side1: ', high/math.sin(self.agles[0]*math.pi/180)
        print 'Side2: ', high/math.sin(self.agles[1]*math.pi/180)

side1 = Triangle()
print 'high: ', side1.high()
side1.otherside()
side1.changeangle(1, 20)
