from Main.Initial import *
from Main.helpScreen import *

def redrawAll(app):
 
    
    if not(app.calibrate) and not(app.TurtleRun) and not(app.HelpScreenUp):
        
        drawRect(0, 0, 1000, 1000, fill = 'lightblue')
        drawLetter(app)
        
        drawCurser(app)
        
        
        
        for block in app.DrawOrderList:
            
            block.DrawMemoryBlock()
            block.DrawRAMLabel()
            block.extendedMemView()
        
        
        
        if app.cubemode:  
            DrawObject(app)
            
    
            
        app.TextModeButton.Draw()
        
        app.TextModeButton.WhenButtonHold(app.ButtonHoldTime)
        
        app.TextModeButton.EaseRelease()
        
        app.TextModeButton.DrawLabels()
        
        
        if app.ErrorOccured:
            
            app.Error.ShowMessege()
            
           
            drawRect(65, 70 + app.ErrorPos * 20, 12 * len(app.ErrorLine), 15, fill = 'red', opacity = app.Error.errorShow/1.2)
            
        
        app.Error.ErrorPopUp()
        
        
            
            
    elif app.calibrate and not(app.HelpScreenUp) and not(app.TurtleRun):
        
        CalibrationDraw(app)
        
    elif app.TurtleRun and not(app.HelpScreenUp) and not(app.calibrate):
        
        TurtleDraw(app)
        
        
    elif (app.HelpScreenUp) and not(app.TurtleRun) and not(app.calibrate):
        
        
        if app.CurrentHelpScreen == 0:
            
            BaseHelpScreen(app)
            
        elif app.CurrentHelpScreen == 1:
            
            AssemblyHelpScreen(app)
            
            
        elif app.CurrentHelpScreen == 2:
            
            LanguageHelpScreen(app)
            
            
        elif app.CurrentHelpScreen == 3:
            
            CalibrationHelpScreen(app)
            
            
        elif app.CurrentHelpScreen == 4:
            
            TurtleHelpScreen(app)
            
        elif app.CurrentHelpScreen == 5:
            
            StackHelpScreen(app)
            
        elif app.CurrentHelpScreen == 6:
            
            LastHelpScreen(app)