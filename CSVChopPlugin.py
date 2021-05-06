import PyPluMA

class CSVChopPlugin:
   def input(self, filename):
      #self.myfile = filename
      txtfile = open(filename, 'r')
      parameters = dict()
      for line in txtfile:
         contents = line.split('\t')
         parameters[contents[0]] = contents[1].strip()
      filestuff = open(PyPluMA.prefix()+"/"+parameters['csvfile'], 'r')
      self.lines = []
      for line in filestuff:
         self.lines.append(line)
      if ('start' in parameters):
         self.start = int(parameters['start'])
      else:
         self.start = 0
      if ('end' in parameters):
         self.end = int(parameters['end'])
      else:
         self.end = len(self.lines)

   def run(self):
      pass

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(self.start, self.end):
         filestuff2.write(self.lines[i])
         #if (i != len(self.lines)-1):
         #   filestuff2.write('\n')



