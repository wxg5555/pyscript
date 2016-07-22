import androidhelper

class Group:
  def __init__(self,boxes):
    self.droid=androidhelper.Android()
    self.boxes=boxes
    for box in boxes:
      box.group=self
  
  def open(self,index):
    print 'open door: %d'% index

class Box:
  def __init__(self,index,no):
    self.index=index
    self.no=no
  def setGroup(self,group):
    self.group=group

  def __str__(self):
    return 'box %d'%self.index
 
  def __getattr__(self,name):
    print 'exec groups %s'% name
    return lambda **arg: self.proxy(name,arg)
    
  def proxy(self,name,arg):
    m=getattr(self.group,name)
    print 'args is %s'% arg
    if arg:
      m(self.index,arg)
    else:
      m(self.index)

  def getfile(self):
    pass

class Department:
  def __init__(self,name):
    self.name=name

class Person:
  def __init__(self,name,address):
    self.name=name
    self.address=address

class Role:
  def __init__(self,person,dept,carno,boxno,files=[]):
    self.person=person
    self.dep=dept
    self.carno=carno
    self.boxno=boxno
    self.files=files
		
  def addfile(self,file):
    files.append(file)

def generatRoles():
  jtc=Department('jtc')
  wsc=Department('wsc')
  p1=Person('wxg','ny')
  p2=Person('sbg','mjp')
  p3=Person('lj','llc')
  p4=Person('dh','ljt')
  r1=Role(p1,jtc,'001',1)
  r2=Role(p2,wsc,'002',2)
  r3=Role(p3,jtc,'003',3)
  r4=Role(p4,wsc,'004',4)
  roles=[r1,r2,r3,r4]
  return roles
  
if __name__=='__main__':
  roles=generatRoles()
  groups=[]
  for i in range(5):
    box=Box(i,i)
    print box
    groups.append(box)
  group=Group(groups)
  for r in roles:
    if r.carno=='003':
      for box in group.boxes:
        if box.no==r.boxno:
          box.open()
  
  