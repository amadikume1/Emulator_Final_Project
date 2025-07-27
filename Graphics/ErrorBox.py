from cmu_graphics import *

class ErrorBox:
    
    
    def __init__(self, messege, x, y, width, height):
        
        self.messege = messege
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.popx = 0
        self.popy = 0
        
        self.opacity = 1
        
        self.errorShow = 1
        self.direc = 1
        
        self.StopAnimation = False
        self.InBlock= False
        
        
    def ShowMessege(self):
        
        if self.height != 0:
            
            drawRect(self.x, self.y, self.width + self.errorShow, self.height + self.errorShow, fill = 'red')
            
            if not(self.InBlock) and not(self.StopAnimation):
                self.errorShow += self.direc
                
                if self.errorShow <= 2:
                    
                    self.direc = 2
                    
                    
                    
                elif self.errorShow >= 100:
                    
                    self.direc = -2
                    self.errorShow = 100
                    
                    
                    
                drawLabel("ERROR", self.x + (self.width + self.errorShow)/2, self.y+ (self.errorShow + self.height)/2, size=18 + self.errorShow/4, fill = 'black', opacity = self.errorShow)
                
                    
            else:
                
            
                      
                      
              
                drawLabel("ERROR", self.x + self.width/2, self.y+self.height/2, size=self.errorShow, fill = 'black', opacity = 100)
                  
             
                 
                
            
            
            
            
            
            
            
            
    
    def InErrorBlock(self, mousex, mousey):
        
            self.popx = mousex
            self.popy = mousey
                
            if mousex > self.x and mousex < (self.x + self.width)  and mousey > self.y and mousey < (self.y + self.height):
                
                self.InBlock = True
                
                self.StopAnimation= True
                
                
            
            else:    
                self.InBlock = False
                self.opacity = 0
                
               
            
            
            
            
    def ErrorPopUp(self):
        
        if self.InBlock:
            
            if self.opacity != 100:
                
                self.opacity += 1
                
                
            drawRect(self.popx, self.popy, len(self.messege) * 15, 50 , fill = 'red', border = 'black', opacity= self.opacity)
            
            drawLabel(self.messege, self.popx + (len(self.messege) * 15)/2, self.popy + 50/2, size = 18)
            
            
        
        
        
        
        
        