
from cmu_graphics import *

#Memeory Drawings

class Memory:
    
    def __init__(self, mem, MemoryBlockx, MemoryBlocky, MemBlockPosX, MemBlockSizex, MemBlockSizey, MemoryTagx, MemoryTagy, MiniViewSizex, MiniViewSizey, MiniFadeRate, isDrag, MouseInBlockData, inBlock, BlockChords, MiniBlockOpacity, name, show, length, itemperrow, app):
    
    
        self.mem = mem
        
        self.shownum = show
        
        if self.shownum:
            for i in range(length):
                
                self.mem.append(0)
                
        else:
            
            for i in range(length):
                
                self.mem.append('lightgreen')
            
        
        self.itempercol = int(length / itemperrow)
        self.itemperrow = itemperrow
        self.MemoryBlockx = MemoryBlockx
        self.MemoryBlocky = MemoryBlocky
        self.MemBlockPosX = MemBlockPosX
        self.MemBlockSizex = MemBlockSizex
        self.MemBlockSizey = MemBlockSizey
        
        self.MemoryTagx = MemoryTagx
        self.MemoryTagy = MemoryTagy
        
        
        self.MiniViewSizex = MiniViewSizex
        self.MiniViewSizey = MiniViewSizey
        self.MiniFadeRate = MiniFadeRate
        
        self.isDrag = isDrag
        self.MouseInBlockData = MouseInBlockData
        self.inBlock = inBlock
        self.BlockChords = BlockChords
        
        self.MiniBlockOpacity = MiniBlockOpacity
        
        self.tag = name
        
        
        
    
    

    def GetMemoryChords(self):
        
        
        x = 0
        y = 0
        numpos = 0
        texty = 0
        
        for i in range(len(self.mem)):
            
            if i % self.itemperrow == 0 and i != 0:
                x = 0
                y += self.MemBlockSizey
                numpos = 0
                texty += (self.MemBlockSizey)
    
            self.BlockChords.append((self.MemoryBlockx + x, self.MemoryBlocky + y))
            
            x += self.MemBlockSizex
            
            numpos += 2
        
    
    
    
    def DrawMemoryBlock(self):
        
        x = 0
        y = 0
        numpos = 0
        texty = 0
        index = 0
        for chord in self.BlockChords:
            
            if self.shownum:
                drawRect(chord[0], chord[1], self.MemBlockSizex, self.MemBlockSizey, fill = 'lightgrey', border = 'grey', borderWidth = 2)
                
            else:
                
                drawRect(chord[0], chord[1], self.MemBlockSizex, self.MemBlockSizey, fill = self.mem[index], border = 'black', borderWidth = .5)
            
            if self.shownum:
                drawLabel(str(self.mem[index])[:5], chord[0] + (self.MemBlockSizex) / 2, chord[1] + (self.MemBlockSizey/2), fill = 'black', align = 'center', font = 'orbitron')
            
            index += 1
        
        
        
        
        
    def extendedMemView(self):
        
        text = str(self.mem[self.MouseInBlockData[1]])
        extra = 0
        if len(text) >= 10:
            
            extra = len(text) - 10
            
            
        if self.inBlock and not(self.isDrag):
            
            if self.shownum:
                drawRect(self.MouseInBlockData[0][0] - self.MiniViewSizex, self.MouseInBlockData[0][1] - self.MiniViewSizey, self.MiniViewSizex + extra * 14, self.MiniViewSizey, fill = 'lightgrey', border = 'grey', borderWidth = 5, opacity = self.MiniBlockOpacity)
                
            else:
                
                drawRect(self.MouseInBlockData[0][0] - self.MiniViewSizex, self.MouseInBlockData[0][1] - self.MiniViewSizey, self.MiniViewSizex + extra * 14, self.MiniViewSizey, fill = text, border = 'black', borderWidth = 5, opacity = self.MiniBlockOpacity)
            
            drawLabel(text, self.MouseInBlockData[0][0] - self.MiniViewSizex + extra * 7 + (self.MiniViewSizex) / 2, self.MouseInBlockData[0][1] - self.MiniViewSizey  + (self.MiniViewSizey/2), fill = 'black', align = 'center', opacity = self.MiniBlockOpacity, size = 20)
        
     
    def MouseInMemoryLoc(self, mousex, mousey):
        
        index = 0
        
        for chord in self.BlockChords:
            
            
            if (mousex > chord[0] and  mousex < chord[0] + self.MemBlockSizex) and (mousey > chord[1] and  mousey < chord[1] + self.MemBlockSizey):
                 
                 
                 self.MouseInBlockData =  ((mousex, mousey), index)
                
                 self.inBlock = True
    
                 
                 return None
                
            index += 1
            
        self.inBlock = False  
    
        
    def MoveMemoryBlock(self, mousex, mousey, app):
        
       
        
        if self.inBlock:
            
            self.MemoryBlockx = (mousex - (self.MemBlockSizex * self.itemperrow)/2 )
            
            
            self.MemoryBlocky = (mousey - (self.MemBlockSizey * self.itempercol)/2 )
            
            
            app.DrawOrderList.remove(self)
            app.DrawOrderList.append(self)
            
        self.BlockChords = [] 
        
        self.GetMemoryChords()
        
        self.MiniBlockOpacity = 0





    def DrawRAMLabel(self):
        
        drawLabel(self.tag,  self.MemoryTagx,  self.MemoryTagy, size=40, font = 'monospace')
      
    def MoveLabel(self):
        
        if self.MemoryTagx > (self.MemoryBlockx + 100) - 1:
            
            self.MemoryTagx-= 7
            
        if self.MemoryTagx < (self.MemoryBlockx + 100) - 1:
            
            self.MemoryTagx += 8
            
            
        if self.MemoryTagy > (self.MemoryBlocky - 25) - 1:
            
            self.MemoryTagy -= 8
            
        if self.MemoryTagy < (self.MemoryBlocky - 25) - 1:
            
            self.MemoryTagy += 7




def SetUpMem(app):
    
    
        app.mem = []
            
        
        app.MemoryBlockx = 10
        app.MemoryBlocky = 700
        app.MemBlockPosX = 0
        app.MemBlockSizex = 60
        app.MemBlockSizey = 40
        
        app.MemoryTagx = app.MemoryBlockx + 100
        app.MemoryTagy = app.MemoryBlocky - 25
    
        
        app.MiniViewSizex = 100
        app.MiniViewSizey = 50
        app.MiniFadeRate = 1.45
        
        app.isDrag = False
        app.MouseInBlockData = ((0, 0), 0)
        app.inBlock = False
        app.BlockChords = []
        
        app.MiniBlockOpacity = 0
        
        
def SetUpVideo(app):
    
        app.pixels = []
            
        
        app.VideoBlockx = 400
        app.VideoBlocky = 60
        app.VideoBlockPosX = 0
        app.VideoBlockSizex = 50
        app.VideoBlockSizey = 50
        
        app.VideoTagx = app.VideoBlockx + 100
        app.VideoTagy = app.VideoBlocky - 25
    
        
        app.MiniViewVideoSizex = 100
        app.MiniViewVideoSizey = 50
        app.MiniFadeRateVideo = 1.45
        
        app.isDragV = False
        app.MouseInBlockVideoData = ((0, 0), 0)
        app.inBlockV = False
        app.BlockChordsVideo = []
        
        app.MiniBlockOpacityVideo = 0
        
        

#-------------------------------------------------------------------------------------------------------------------

#Video Screen

def VideoScreen(app):
    
    app.VideoX = 500
    
    app.VideoY = 60
    
    app.pixelsize = 40
    
    app.pixels = []
    
    app.pixelChords = []
    
    for i in range(50):
        
        app.pixels.append(0)
        
        
    
    
def DrawVideoPixels(app):
    
    
    x = 0
    y = 0
    numpos = 0
    texty = 0
    
    for i in range(len(app.pixels)):
        
        if i % 10 == 0 and i != 0:
            
            x = 0
            y += app.pixelsize
           

        drawRect(app.VideoX + x, app.VideoY + y, app.pixelsize, app.pixelsize, fill = 'lightgrey', border = "black", borderWidth=.1)
        
        x += app.pixelsize
        

#--------------------------------------------------------------------------------------------------------------------