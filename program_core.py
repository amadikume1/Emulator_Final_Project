from Main.Initial import *
from Main.helpScreen import *
from Main.redraw import *
from Main.eventHandler import *
from cmu_graphics import *

def RunEmulator(Registers, RAM, app):

        if app.ROM[app.PC] != '' and app.ROM[app.PC][0] != '#':
            
            dec = decoder(app.ROM[app.PC])
            
           
            ex = execute(dec, Registers)
            
            
            if (len(ex) in (4, 5) and ex[0] == 'Branch' and ex[-2] == 1)  or (ex[0] == 'Branch'and len(ex) == 3):
            
                
                app.PC = ex[-1]
                
                
                
                return None
            
            
                
            
            st = store(ex, Registers, RAM, app)
            lod = load(Registers, st, RAM, app)
            
            
        
        app.PC += 1


def onStep(app):
    
  
        
    if not(app.calibrate):
        app.time += 1
        
        UpdateRotation(app)
        
        
        
        ManageMemeoryBlockOpacityAndMovement(app)
              
     
     
        if app.TextModeButton.OnButtonPos:
            app.ButtonHoldTime += 1
            
            
        
        if app.ErrorOccured and app.Error.height < 50:
            
            app.Error.height += .5
            
            
        
        if app.Error.InBlock and app.Error.errorShow != 18:
            
              
           
            if app.Error.errorShow <= 18:
                      
                app.Error.errorShow += 1
            else:
                      
                app.Error.errorShow -= 1
            
            
        
    if app.calibrate and app.timestart:
        
            app.calcibratetime += .1
            #print(app.calcibratetime)
            
     
    if not(app.EmulatorRunning) and app.reset:
        
        ResetItem(app)   
        UpdateRotation(app)
            
    
    if app.EmulatorRunning:
        
        
      
        if app.PC < len(app.ROM):
            
            
            RunEmulator(app.Register.mem, app.RAM.mem, app)
            
            
            
            if app.cubemode:   
                MoveObject(app)
                
                UpdateRotation(app)
                
            
            
            
            
        else:
        
          
           app.EmulatorRunning = False
           app.PC = 0
           app.ROM = []
           
           
           
          
      


    if app.Hold:
        
        app.holdtime += 1
        
    else:
        
        app.holdtime = 0
        
    
            
    
def main():

    runApp()

main()
    
    