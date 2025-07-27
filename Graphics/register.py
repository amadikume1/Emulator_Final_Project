from cmu_graphics import *
import math
#Register Block



def SetUpCubeMemory(app):
    
        app.Cubemem = []
            
        
        app.CubeBlockx = 400
        app.CubeBlocky = 560
        app.CubeBlockPosX = 0
        app.CubeBlockSizex = 60
        app.CubeBlockSizey = 50
        
        app.CubeTagx = app.RegistersBlockx + 100
        app.CubeTagy = app.RegistersBlocky - 25
    
        
        app.MiniViewCubeSizex = 100
        app.MiniViewCubeSizey = 50
        app.MiniFadeRateCube = 1.45
        
        app.isDragCube = False
        app.MouseInBlockCubeData = ((0, 0), 0)
        app.inBlockCube = False
        app.BlockChordsCube = []
        
        app.MiniBlockOpacityCube = 0
        

def SetUpRegister(app):
    
        app.Regs = []
            
        
        app.RegistersBlockx = 684
        app.RegistersBlocky = 475
        app.RegistersBlockPosX = 0
        app.RegistersBlockSizex = 60
        app.RegistersBlockSizey = 50
        
        app.RegistersTagx = app.RegistersBlockx + 100
        app.RegistersTagy = app.RegistersBlocky - 25
    
        
        app.MiniViewRegistersSizex = 100
        app.MiniViewRegistersSizey = 50
        app.MiniFadeRateRegisters = 1.45
        
        app.isDragRegisters = False
        app.MouseInBlockRegistersData = ((0, 0), 0)
        app.inBlockRegisters = False
        app.BlockChordsRegisters = []
        
        app.MiniBlockOpacityRegisters = 0

#---------------------------------------------------------------------------------------------------------------------

#TextMode button

class Button:
    
    def __init__(self, x, y, width, height, modes):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.OnButtonPos = False
        self.ColorButton = 'steelBlue'
        self.ColorLoad = 'salmon'
        self.loadwidth = 0
        self.NonCompleteLoadWidth = 0
        self.Base = 0
        self.ModeLabels = modes
        self.ColorsPerMode = ['white', 'black']
        self.ModeSelected = 0
        self.ColorForAMode = 0
        self.ColorForBMode = 0
        

    def Draw(self):
        
        drawRect(self.x, self.y, self.width, self.height, fill = self.ColorButton)
        
    def OnButton(self, mousex, mousey):
        
        if mousex > self.x and mousex < (self.x + self.width)  and mousey > self.y and mousey < (self.y + self.height)  and self.loadwidth < self.width:
            
            self.OnButtonPos = True
          
            
        else:
            
            self.OnButtonPos = False
        
        
    def WhenButtonHold(self, time):
        
            if time == 0:
                
                self.Base = self.NonCompleteLoadWidth 
                
           
            self.loadwidth = int((time * 2) + self.Base + 1)
            
            
            
                
            
            
            if time != 0:
                
                self.NonCompleteLoadWidth = self.loadwidth
            
            if math.ceil(self.loadwidth) >= self.width  and self.OnButtonPos:
                
                 
                    colorload = self.ColorLoad
                    
                    
                    self.ColorLoad = self.ColorButton
                    
                    self.ColorButton = colorload
                    
                    
                    self.OnButtonPos = False
                    
                    self.loadwidth = self.width
                    
                    
                    
                    self.NonCompleteLoadWidth = 0
                    
                    if self.ModeSelected == 0:
                        self.ModeSelected = 1
                        self.ColorForAMode = 1
                        self.ColorForBMode = 0
                        
                        
                    else:
                        
                        self.ModeSelected = 0
                        self.ColorForAMode = 0
                        self.ColorForBMode = 1
                    
        
            if self.OnButtonPos:
                
                
                drawRect(self.x, self.y, self.loadwidth, self.height, fill = self.ColorLoad)
        
        
    def EaseRelease(self):
        
        if self.NonCompleteLoadWidth >= self.width:
            
            self.NonCompleteLoadWidth = 0
        
        if self.NonCompleteLoadWidth != 0 and not(self.OnButtonPos):
            
   
           
            drawRect(self.x, self.y, self.NonCompleteLoadWidth, self.height, fill = self.ColorLoad)
            
            self.NonCompleteLoadWidth -= 1
            
    def DrawLabels(self):
        
        pos = 15
        
        
        for letter in range(len(self.ModeLabels[self.ModeSelected])):
            
            letters = self.ModeLabels[self.ModeSelected][letter]
            
            if pos > self.NonCompleteLoadWidth:
                
            
                
                if self.ModeSelected  == 1:
                    
                    letters = self.ModeLabels[0][letter]
                   
                else:
                    letters = self.ModeLabels[1][letter]
                    
                color = self.ColorsPerMode[self.ColorForBMode]
                
            else:
                color = self.ColorsPerMode[self.ColorForAMode]
            
            
            drawLabel(letters, self.x + pos, self.y + (self.height/2), size = 25, font = 'monospace', fill = color)
            
            pos += 15

