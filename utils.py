import numpy as np

class BndBox:
	
  def __init__(self,x,y,w,h,c=None,classes=None):
    self.x=x
    self.y=y
    self.w=w
    self.h=h

    self.c=c
    self.classes=classes

    self.label=-1
    self.score=-1

  def get_label(self):
    if self.label==-1:
      self.label=np.argmax(self.classes)
    return self.label

  def get_score(self):
    if self.score==-1:
      self.score=self.classes[self.get_label]
    return self.score

def bbox_iou(box1,box2):
  xmin1=box1.x-box1.w/2
  xmax1=box1.x+box1.w/2
  ymin1=box1.y-box1.h/2
  ymax1=box1.y+box1.h/2

  xmin2=box2.x-box2.w/2
  xmax2=box2.x+box2.w/2
  ymin2=box2.y-box2.h/2
  ymax2=box2.y+box2.h/2

  intersect_w=interval_overlap([xmin1,xmax1],[xmin2,xmax2])
  intersect_h=interval_overlap([ymin1,ymax1],[ymin2,ymax2])

  intersect=intersect_w*intersect_h

  union=box1.w*box1.h+box2.w*box2.h-intersect

  return float(intersect)/union

def interval_overlap(args1,args2):
  min1,max1=args1
  min2,max2=args2
  if max1<min2 or max2<min1:
    return 0
  else:
    return min(max1,max2)-max(min1,min2)

if __name__=="__main__":
  a=BndBox(30,30,40,40)
  b=BndBox(45,45,50,50)
  print(bbox_iou(a,b))