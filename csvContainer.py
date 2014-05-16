# -*- coding: utf-8 -*-

class ContainerError(Exception): pass

class csvContainer:
  """ Container to do simple operations with csv files """
  
  f    = None    # The file. Is always open and positioned after the header for reading .
  hea  = None    # The header as a dictionary converting names into column numbers
  fnam = None    # The file name. For creating realted names for audit()
  auto = False   # Automatically convert comma separated files when ^-separated fails

  
  def __init__(self, fnam, auto = False):
    """ Open the file and read the header """
    
    self.fnam = fnam
    self.auto = auto
    self.f    = open(fnam)
    
    li = self.f.readline()
    ky = [i.strip(' ') for i in li.rstrip('\n').split('^')]
    
    self.hea = dict(zip(ky, range(len(ky))))
   
   
  def audit(self):
    """ Scan the entire file counting columns and writing problematic lines to a file """
    
    numcol = len(self.hea)
    stpos  = self.f.tell()
    
    errfile = open(self.fnam + '.audit.csv', 'w')
    
    ln = 1
    li = self.f.readline()
    while li != '':
      row = li.rstrip('\n').split('^')
      
      if self.auto and len(row) == 1: row = li.rstrip('\n').split(',')
      
      if len(row) != numcol: 
#        if len(row) > numcol: raise ContainerError, 'Too many columns %s ' % len(row)
#        if len(row) < 2:      raise ContainerError, 'No separator found or empty row'
        errfile.write(li)
          
        print ln, len(row), row, self.f.tell(), '\n'
      
      li = self.f.readline()
      ln += 1
    
    self.f.seek(stpos)
    errfile.close()


  def aggregate(self, x, groupby, fun):
    """ Apply function fun to variable' x grouping by groupby. x and groupby are variable names and fun is a function possibly 
    a lambda like lambda a, b: a+b. The function is computed incrementally where a is the accumulated value and b is the new value. """

    numcol = len(self.hea)
    stpos  = self.f.tell()
    
    grby  = {}
    idx_x = self.hea[x]
    idx_g = self.hea[groupby]
    
    li = self.f.readline()
    while li != '':
      row = li.rstrip('\n').split('^')
      
      if self.auto and len(row) == 1: row = li.rstrip('\n').split(',')
      
      if len(row) == numcol:
        x = row[idx_x].strip(' ')
        g = row[idx_g].strip(' ')
        
        if g in grby:
          x = fun(grby[g], float(x))
          
        grby[g] = float(x)
      
      li = self.f.readline()
    
    self.f.seek(stpos)

    return(grby)       
      
## end of csvContainer      
    