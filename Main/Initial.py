
import math
import copy
from cmu_graphics import *
from Emulator.emulator import *
from Graphics.calibration import *
from Graphics.cube import *
from Graphics.ErrorBox import *
from Graphics.register import *
from Graphics.text import *
from Graphics.memory import *
from Assembler.assembly import *
from Language.language import *
from VM.vm import *
from Turtle.turtle import *



def onAppStart(app):
    
    
    app.MaxShapeCount = 10000
    app.CurrentHelpScreen = 0
    app.Invalidkey = ('pageup', 'pagedown', 'home', 'escape', 'delete', 'tab')
    app.Validkey = (',', ':', ';', '%', '/', "/", '+', '-', '-', '_', '.', '>', '<', '?', '*', '#', '=')
    app.height = 800
    app.width = 800
    app.holdtime = 0
    app.keyhold = False
    app.texttime = 0
    app.ButtonHoldTime = 0
    app.reset = False
    app.PC = 0
    app.EmulatorRunning = False
    app.labels = {}
    app.ErrorPos = 0
    app.ErrorLine = ''
    app.setMaxShapeCount(app.MaxShapeCount)
    SetUpMem(app)
    SetUpVideo(app)
    SetUpRegister(app)
    SetUpCubeMemory(app)
    app.HelpScreenUp = True
    
    app.VideoRAM = Memory(app.pixels,
                     app.VideoBlockx, app.VideoBlocky,
                     app.VideoBlockPosX,
                     app.VideoBlockSizex, app.VideoBlockSizey,
                     app.VideoTagx, app.VideoTagy,
                     app.MiniViewVideoSizex, app.MiniViewVideoSizey,
                     app.MiniFadeRateVideo,
                     app.isDragV,
                     app.MouseInBlockVideoData,
                     app.inBlockV,
                     app.BlockChordsVideo,
                     app.MiniBlockOpacityVideo, 'VIDEO', False, 50, 10, app)
                     
    app.Register = Memory(app.Regs,
                      app.RegistersBlockx,
                      app.RegistersBlocky, 
                      app.RegistersBlockPosX,
                      app.RegistersBlockSizex,
                      app.RegistersBlockSizey,
                      app.RegistersTagx,
                      app.RegistersTagy,
                      app.MiniViewRegistersSizex,
                      app.MiniViewRegistersSizey, 
                      app.MiniFadeRateRegisters,
                      app.isDragRegisters,
                      app.MouseInBlockRegistersData,
                      app.inBlockRegisters,
                      app.BlockChordsRegisters,
                      app.MiniBlockOpacityRegisters, "Register File", True, 32, 4, app)                 
                   
    
    app.RAM = Memory(app.mem, 
                 app.MemoryBlockx, app.MemoryBlocky,
                 app.MemBlockPosX,
                 app.MemBlockSizex, app.MemBlockSizey,
                 app.MemoryTagx, app.MemoryTagy,
                 app.MiniViewSizex, app.MiniViewSizey,
                 app.MiniFadeRate,
                 app.isDrag,
                 app.MouseInBlockData,
                 app.inBlock,
                 app.BlockChords,
                 app.MiniBlockOpacity, 'RAM', True, 50, 10, app)
                 
                 
                
                 
    app.CubeMemory = Memory(app.Cubemem, 
                 app.CubeBlockx, app.CubeBlocky,
                 app.CubeBlockPosX,
                 app.CubeBlockSizex, app.MemBlockSizey,
                 app.CubeTagx, app.CubeTagy,
                 app.MiniViewSizex, app.MiniViewSizey,
                 app.MiniFadeRate,
                 app.isDragCube,
                 app.MouseInBlockCubeData,
                 app.inBlockCube,
                 app.BlockChordsCube,
                 app.MiniBlockOpacityCube, 'Cube', True, 3, 3, app)
                 
   
   
    
    app.DrawOrderList = [app.RAM, app.VideoRAM, app.Register, app.CubeMemory]
    
    
    app.RAM.GetMemoryChords()
    
    app.ROM = []
    app.Hold = False
    app.ErrorBoxHeight = 0
    app.ErrorOccured = False
    app.Error = ErrorBox('', 400, 400, 100, 0)
    
    app.VideoRAM.GetMemoryChords()
    app.Register.GetMemoryChords()
    app.CubeMemory.GetMemoryChords()
    
    SetUpText(app)
    ShapeStart(app)
    VideoScreen(app)
    
    CalibrationStart(app)
    TurtleStart(app)
    
    
    app.TextModeButton = Button(60, 10, 150, 40, ["C-       ", "Assembler"])

    app.cubemode = False



#-----------------------------------
