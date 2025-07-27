from Main.Initial import *
from Main.helpScreen import *
from Main.redraw import *       
        
        


def NotAllBlank(text):
    
    for line in text:
        
        if line != '':
            
            return True
            
    return False
 

def ManageMemeoryBlockOpacityAndMovement(app):
    
        if app.RAM.inBlock and (app.RAM.MiniBlockOpacity + app.RAM.MiniFadeRate) < 100:
            
            app.RAM.MiniBlockOpacity += app.RAM.MiniFadeRate
            
            
            
        elif not(app.RAM.inBlock):
            
            app.RAM.MiniBlockOpacity = 0
            
        
        
        if app.VideoRAM.inBlock and (app.VideoRAM.MiniBlockOpacity + app.VideoRAM.MiniFadeRate) < 100:
            
            app.VideoRAM.MiniBlockOpacity += app.VideoRAM.MiniFadeRate
            
        
        elif not(app.VideoRAM.inBlock):
            
            
            app.VideoRAM.MiniBlockOpacity = 0
        
        
        if app.Register.inBlock and (app.Register.MiniBlockOpacity + app.Register.MiniFadeRate) < 100:
            
            app.Register.MiniBlockOpacity += app.Register.MiniFadeRate
            
        
        elif not(app.Register.inBlock):
            
            
            app.Register.MiniBlockOpacity = 0
            
            
        
        if app.CubeMemory.inBlock and (app.CubeMemory.MiniBlockOpacity + app.CubeMemory.MiniFadeRate) < 100:
            
            app.CubeMemory.MiniBlockOpacity += app.CubeMemory.MiniFadeRate
            
        
        elif not(app.CubeMemory.inBlock):
            
            
            app.CubeMemory.MiniBlockOpacity = 0
            
            
            
        
        if app.time > 30:
            
            app.opac -= 10
            
            if app.opac < 10:
                
                app.opac = 1
            
            
                
        if app.time > 60:
                 
                 app.opac = 90
                 app.time = 0
                 
                 
        app.RAM.MoveLabel()
        
        app.VideoRAM.MoveLabel()
        
        
        app.Register.MoveLabel()
        
        app.CubeMemory.MoveLabel()
        


    
def onMousePress(app, mouseX, mouseY):
    
    
    
    if app.calibrate and app.timestart:
        
        app.calibrate = False
        app.timestart = False
       
        app.callist =  []
        
        app.calcibratetime = 0
        
        
        
    else:
        
        
        app.TextModeButton.OnButton(mouseX, mouseY)
        
        
        
        CurserOnMousePress(app, mouseX, mouseY)
        
    if not(app.calibrate):
        
        EnableDraw(app, mouseX, mouseY)
        
        
        
    
    
        
        
          
     
def onMouseMove(app, mouseX, mouseY):
    
    if not(app.calibrate):
        app.RAM.MouseInMemoryLoc(mouseX, mouseY)
        
        
    
        app.VideoRAM.MouseInMemoryLoc(mouseX, mouseY)
        
        app.Register.MouseInMemoryLoc(mouseX, mouseY)
        
        app.CubeMemory.MouseInMemoryLoc(mouseX, mouseY)
        
        app.Error.InErrorBlock(mouseX, mouseY)
        

def onMouseDrag(app, mouseX, mouseY):
    
    if not(app.calibrate):
        Resize(app, mouseX, mouseY)
        
        app.RAM.MoveMemoryBlock(mouseX, mouseY, app)
        
        app.RAM.isDrag = True
     
        
        app.VideoRAM.MoveMemoryBlock(mouseX, mouseY, app)
        
        app.VideoRAM.isDrag = True
        
        app.CubeMemory.MoveMemoryBlock(mouseX, mouseY, app)
        
        app.CubeMemory.isDrag = True
        
        
        
        app.Register.MoveMemoryBlock(mouseX, mouseY, app)
        app.Register.isDrag = True
     
        
    
def onMouseRelease(app, mouseX, mouseY):
    
    if not(app.calibrate):
        app.RAM.isDrag = False
        
        app.VideoRAM.isDrag = False
        
        app.Register.isDrag = False
        
        app.CubeMemory.isDrag = False
        
        app.TextModeButton.OnButtonPos = False
        
        app.ButtonHoldTime = 0






    
def KeyPressingValidation(app, keys):
    
    
    
    validkey = (keys[0].isalpha() or keys[0].isdigit() or keys[0] in app.Validkey) and not(keys[0] in  app.Invalidkey)
    
    if not(app.calibrate):
        
       
     
        app.keyhold = True
        
            
            
        if app.EnableTyping and app.holdtime > (app.timeforkeyPress) and validkey and app.Hold:
            
        
          
            KeyCommand(app, keys[0])
            
          
            
        app.Hold = True


def onKeyRelease(app, key):
    
    if not(app.calibrate):
        app.Hold = False

def onKeyRelease(app, key):
    
    
    if not(app.calibrate):
        app.keyhold = False
        app.holdtime = 0
        app.Hold = False


def onKeyHold(app, keys):
    
    KeyPressingValidation(app, keys)
    



def onKeyPress(app, key, modifier):
    
    
    if app.EnableTyping and key == 'delete':
        
        ClearText(app)
        
    
    if key == "tab":
        
        app.HelpScreenUp = True
    
    

    TurtleMode(app, key)
    CalibrationMode(app, key)
    
    if not(app.calibrate) and not(app.HelpScreenUp) and not(app.TurtleRun):

        if key == 'pagedown':
            
        
            
            app.reset = True
            
        if key == 'escape':
            
            app.EmulatorRunning = False
        
       
        
      
        SetUpTurtle = [
        'LOD, R1-55',      # Start position (leftmost)
        'LOD, R2-73',      # Blue color
        'LOD, R3-59',      # End position (rightmost)
        'LOD, R4-0',       # For zero comparisons
        'LOD, R5-99',
        'LOD, R6-25']  
        
        # White color to erase 
        
        rightmove = [
        'ALU_RI, R3-  R1 ADD 1',
        'ALU_RI, R4 - R3 FLR 10',
        'ALU_RI, R4 - R4 MUL 10',
        'ALU_RI, R4 - R4 ADD 9',
        'JMP, R3 EQL R4 - x',
        'STORE, *R1-0',
        'STORE, *R1-R6',  # Clear current position
        'ALU_RI, R1-R1 ADD 1',
        'LOD, R1 - R3',
        'STORE, *R1-R6',   # Color new position
        'STORE, *R1-0',
        'LOD, R6 - 25']
        
        
        leftmove = [
        ' ',
        'ALU_RI, R3-  R1 SUB 1',
        'ALU_RI, R4 - R3 FLR 10',
        'ALU_RI, R4 - R4 MUL 10',
        'JMP, R3 EQL R4 - x',
        'STORE, *R1-0',
        'STORE, *R1-R6',  # Clear current position
        'ALU_RI, R1-R1 SUB 1',
        'LOD, R1 - R3',
        'STORE, *R1-R2',   # Color new position
        'STORE, *R1-0',
        'LOD, R6 - 25'
        ]
        
        movedown = [
        ' ',
        ' ',
        'ALU_RI, R3-  R1 ADD 10',
        'LOD, R4 - 100',
        'JMP, R3 GRAT R4 - x',
        'STORE, *R1-0',
        'STORE, *R1-R6',  # Clear current position
        'ALU_RI, R1-R1 ADD 10',
        'LOD, R1 - R3',
        'STORE, *R1-R2',   # Color new position
        'STORE, *R1-0',
        'LOD, R6 - 25']
            
            
            
        
        
        
        
        moveup = [
            
        ' ',
        ' ',
        'ALU_RI, R3-  R1 SUB 10',
        'LOD, R4 - 50',
        'JMP, R3 LESS R4 - x',
        'STORE, *R1-0',
        'STORE, *R1-R6',  # Clear current position
        'ALU_RI, R1-R1 ADD 10',
        'LOD, R1 - R3',
        'STORE, *R1-R2',   # Color new position
        'STORE, *R1-0',
        'LOD, R6 - 25']
        
        
        dropcolor = [
            
            'LOD, R6-12'
            
            ]
            
        removecolor = [
            
            'LOD, R6-25'
            
            ]
        
        
    
        test = SetUpTurtle
        
        
        
        KeyToTurtle = {'w':moveup, 's':movedown, 'd': rightmove, 'a': leftmove, '+': dropcolor, '-': removecolor}
        
        
        if len(app.Turtlelist) != 0 and app.TurtleRun == False:
            
            for i in  range(len(app.Turtlelist)):
                
                
                thismove = copy.deepcopy(KeyToTurtle[app.Turtlelist[i]])
                
                if app.Turtlelist[i] == '+' or app.Turtlelist[i] == '-':
                    
                    test += thismove
                    
                else:
                    
                    thismove[4] = thismove[4].replace('x', '#Turtle' + str(i))
                    thismove.append('#Turtle' + str(i))
                    test += thismove
                    
            app.Turtlelist = []
                    
                    
            ReplaceCurrentAssemblyTurtle(app, test)
                    
            
            
        lines = CondenseLine(app)
         
         
        
        if (key == 'home' and NotAllBlank(lines)) or (key == 'home' and len(app.Turtlelist) != 0 and app.TurtleRun == False):
            
            
           
            
            app.Error.StopAnimation = False
            app.Error.height  = 0
            app.ErrorOccured = False
            
        
            
            
            if app.TextModeButton.ModeSelected == 0 or len(app.Turtlelist) != 0:
                    
                    
                    
                    assembly = AssembleCode(lines, app.labels, ErrorList, app)
                    
                
                
             
                
            else:
                
        
                
                assembly = LanguageToAssembly(lines)
                        
                        
                        
                assembly = AssembleCode(assembly, app.labels, ErrorList, app)
                        
            
            
            if not(assembly[0] in ErrorList):
                
                app.Turtlelist = []
                
                app.ROM = []
                
                app.ErrorPos = 0
                
                app.PC = 0
                app.labels = {}
                
                for i in range(len(app.Register.mem)):
                    
                    app.Register.mem[i] = 0
                    
                    
                    
                    
                for i in range(len(app.RAM.mem)):
                    
                    app.RAM.mem[i] = 0
                    
                    
                    
                    
                for i in range(len(app.VideoRAM.mem)):
                    
                    app.VideoRAM.mem[i] = 'lightgreen'
                    
                    
                
                for i in range(len(app.CubeMemory.mem)):
                    
                    app.CubeMemory.mem[i] = '0'
                    
                    
                app.ROM = assembly
                
                
                
                
                app.EmulatorRunning = True
            
                
            else:
       
                
                app.ErrorOccured = True
                
                app.Turtlelist = []
                
                
                ErrorMessage = ErrorList[assembly[0]].replace('x',assembly[1])
                
                app.ErrorPos = lines.index(assembly[-1])
                
                app.ErrorLine = assembly[-1]
                
                app.Error.messege = ErrorMessage + f' -> line: {app.ErrorPos}'
                
                
            
           
        if not(app.holdtime > (app.timeforkeyPress)) and (key.isalpha() or key.isdigit() or key in app.Validkey) and not(key in app.Invalidkey) and not(app.Hold):
                
              
                    KeyCommand(app, key)
    