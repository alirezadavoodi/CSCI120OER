#-	Define a class and a static method that receives a string (word) and reverses it and returns it.

class ReverseString:
    def stringReverse(word):
        reversed=""
        for i in range(len(word)-1,-1,-1):
            reversed = reversed + word[i]
        return reversed
    


class Histogram:
    def __init__(self, daysSale):
        self._daysSale = daysSale
        
    def getSalesForDay(self, day):
        if day in self._daysSale:
            return self._daysSale[day]
        else:
            print("wrong day entered")
            return
    
    def addDaySale(self, day, sale):
        self._daysSale[day]=sale


class NumberConvertor:
    
    #static method
    def convert(number, base):
        convertedNumber = ""
        
        while number!=0:
            rem = number%base
            number = number//base
            convertedNumber = str(rem)+convertedNumber
        return convertedNumber


class Projector:
        
    #static variable
    collegeName = "Columbia College"
        
    def __init__(self, state, source, model):
        self._state = state
        self._source = source
        self._model = model
        self._volume=0
            
        
    def getState(self):
        return self._state
        
    def setState(self, state):
        self._state = state
        
    def getSource(self):
        return self._source
        
    def setSource(self,source):
        self._source = source
    
    def getModel(self):
        return self._model
        
    def setModel(self, model):
        self._model = model
        
    def volumeUP(self):
        self._volume = self._volume+1
        
        
    def volumeDown(self):
        if self._volume>=1:
            self._volume = self._volume-1
            
    def printProjecctorInfo(self):
        print("Project Model: %s" %(self._model))
        print("Project State: %s" %(self._state))
        print("Project Source: %s" %(self._source))
        print("Project current volum: %d" %(self._volume))
        

def main():
    #test class stringReverse
    print(ReverseString.stringReverse("Vancouver"))
    
    #test histogram
    histogram = Histogram({})
    histogram.addDaySale("Monday", 50)
    histogram.addDaySale("Tuesday", 55)
    histogram.addDaySale("Wednesday", 55)
    histogram.addDaySale("Thursday", 54)
    histogram.addDaySale("Friday", 52)
    histogram.addDaySale("Saturday", 41)
    histogram.addDaySale("Sunday", 37)
    
    print(histogram.getSalesForDay("Monday"))
    print(histogram.getSalesForDay("Friday"))
    print(histogram.getSalesForDay("fake day"))
    
    
    #test base convertor 
    print(NumberConvertor.convert(8,8))
    print(NumberConvertor.convert(13,4))
    print(NumberConvertor.convert(20,2))
    
    
    #test Problem 4
    #state, source, model
    projector = Projector("ON", "HDMI", "NEC")
    projector.setSource("VGH")
    projector.setState("OFF")
    projector.volumeDown()
    projector.volumeUP()
    

    

        
    
main()