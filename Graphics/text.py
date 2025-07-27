
import math
import copy
from cmu_graphics import *
#Text Functions

def SetUpText(app):
    
    
    app.pagetop = [60, 60]
    app.pagedim = [300, 500]
    app.textsize = 11
    app.rowspace = app.textsize + 15
    app.rowletterfit = math.floor((app.pagedim[0] / app.textsize))
    app.colletterfit = math.floor((app.pagedim[1] / app.rowspace))
    app.EnableTyping = False
    app.posperrow = [0]
    app.string = []
    app.curserPos = 0
    app.delspeed = 1
    app.currrow = 0
    app.opac = 100
    app.time = 0
    app.cursercolor = 'black'
    
    for _ in range(200):
    
        app.string.append('')
    
    app.line = [app.string]
    app.linepos = 0
    

def ClearText(app):
    
    SetUpText(app)


def CondenseLine(app):
    
    lines = []
    
    for string in app.line:
        
        lines.append(''.join(string))
        
    return lines
    
    
        
        
        
def drawCurser(app):
    
    xcord = app.curserPos


def CurserOnMousePress(app, mousex, mousey):
    
    if app.EnableTyping:
        
        
        
        
        y = pythonRound((mousey - app.pagetop[1]) / (math.floor((500/ app.rowspace))))
        
        x = pythonRound((mousex - app.pagetop[0]) / (math.floor((100/ app.textsize))))
        
        
        
        if (y-1) >= 0 and y <= len(app.line):
            
            
            app.line[app.linepos] = copy.deepcopy(app.string)
            
            app.currrow = y - 1
            app.linepos = y - 1
            
            
           
                
               
        
                
                
            app.curserPos = app.posperrow[app.linepos]
                        
            for i in range(200):
                    
                app.string[i] = ''
                            
                        
            app.string = app.line[app.currrow]
                
                
            if (x-1) < 0:
            
                app.curserPos = 0
                
            elif (x-1) < app.curserPos:
                app.curserPos = x-1
                
    if app.HelpScreenUp:
        
        if app.CurrentHelpScreen == 6:
            
            app.CurrentHelpScreen   = 0
            
        else:
            
            app.CurrentHelpScreen  += 1
            
                
        
        
    
def KeyCommand(app, key):
    
    app.opac = 100
    app.time = 0
    
    
    
    
    if key == 'backspace' and app.curserPos >= 0 and app.EnableTyping:
        
        
        
        if app.linepos == 0 and app.curserPos == 1:
            
            app.posperrow[app.currrow] -= 1
            app.curserPos -= 1
            app.line[app.currrow][app.curserPos] = ''
            
            for i in range(app.curserPos, len(app.string)-1):
                
                #print(app.curserPos)
                app.string[i] = app.string[i+1]
            

            
        elif app.curserPos != 0:
            
            
            
            app.posperrow[app.currrow] -= 1
            app.curserPos -= 1
            app.line[app.currrow][app.curserPos] = ''
            
            for i in range(app.curserPos, len(app.string)-1):
                
                #print(app.curserPos)
                app.string[i] = app.string[i+1]
                
                
                
        elif app.curserPos == 0 and app.currrow != 0:
            
            
            carryup = []
            
            for i in app.line[app.currrow]:
                
                
                if i != '':
                    
                    carryup.append(i)
                    
                if i == '':
                    
                    break
                
                
            blank  = True
        
            
            for i in app.line[app.currrow]:
                
                
                if i != '':
                    
                    blank = False
                    
                    break
                    
                
            
                
            
            
            if app.linepos != 0:   
                
               
                app.line = app.line[:app.currrow] + app.line[app.currrow + 1:]
                app.string = app.line[app.currrow-1]
                app.posperrow = app.posperrow[:app.currrow] + app.posperrow[1+app.currrow:] 
                app.linepos -= 1
                app.currrow -= 1
                app.curserPos = app.posperrow[app.currrow]
                
           
            
            elif blank and len(app.line) == 1:
                
                app.posperrow = [0]
            
         
            
            for i in range(app.curserPos, app.curserPos + len(carryup)):
                
                
                #print(app.curserPos)
                app.string[i] = carryup[i - app.curserPos]
               
          
            app.posperrow[app.linepos] += len(carryup)
            
       
    elif key == 'up':
        
        
        if not(app.currrow == 0):
            app.line[app.linepos] = copy.deepcopy(app.string)
            
            app.currrow -= 1
            app.linepos -= 1
            
            
     
            
            
            
            
            if (app.linepos + 1) == len(app.line) - 1  and (len(app.posperrow) < len(app.line)):
                
            
                app.posperrow.append(app.curserPos+1)
            
            
            
            if  app.posperrow[app.linepos] < app.curserPos:
                
                
                    app.curserPos = app.posperrow[app.linepos]
            
            
            for i in range(200):
        
                app.string[i] = ''
                
            
            app.string = app.line[app.currrow]
        
        print(f"chnaged to row:{app.currrow} value should now be {app.posperrow[app.linepos]} and is {app.curserPos}", app.posperrow)
        
    elif key == 'down':
        
        
        
       
        
            
            
            if not((app.currrow + 1 >= len(app.line))):
                
                app.line[app.linepos] = copy.deepcopy(app.string)
                app.currrow += 1
                app.linepos += 1
            
            
                #print(app.posperrow)
                #print(app.curserPos, app.posperrow[app.currrow])
                
               
                if  app.posperrow[app.linepos] < app.curserPos:
                
                
                    app.curserPos = app.posperrow[app.linepos]
                    
                for i in range(200):
                
                    app.string[i] = ''
                        
                    
                app.string = app.line[app.currrow]
            
             
        
        
       
        
        
            #print(f"chnaged to row:{app.currrow} value should now be {app.posperrow[app.linepos]} and is {app.curserPos}", app.posperrow)
       
    elif key == 'left':
        
        #print(app.curserPos)
        #print(app.line)
        if not(app.curserPos == 0):
            app.curserPos -= 1
        
    elif key == 'right':
        
        if (app.curserPos < app.posperrow[app.linepos]):
            app.curserPos += 1    
    
        
        
    elif key != 'backspace' and app.EnableTyping and key != 'enter':
     
       
        
        app.wordsaftercurser = app.string[app.curserPos:]
        
        
        if key == 'space':
            
            key = ' '
            
      
        app.line[app.linepos][app.curserPos] = key
        
        app.curserPos += 1
        
        app.posperrow[app.linepos] += 1
        
        if len(app.line) > app.colletterfit:
            
            app.pagedim[1] += 25
            app.colletterfit = math.floor((app.pagedim[1] / app.rowspace))
         
         
            
        
        #print('current: ', app.curserPos, app.posperrow) 
        
        
        for i in range(app.curserPos, 200):
            
            app.line[app.linepos][i] = ''
            
            
            
            
        #print(app.wordsaftercurser[:10], 55655)    
        
        
        for i in range(app.curserPos, len(app.wordsaftercurser)):
             
             
             app.line[app.linepos][i] = app.wordsaftercurser[i - app.curserPos]
            
        
        #print(app.curserPos, 88) 
       
            
            
        #print(app.wordsaftercurser, 78)
        
        #print(app.linepos)
        #print(app.posperrow)
        
        
        
            
    if key == 'enter':
        
       
        app.currrow += 1
        app.line[app.linepos] = ((app.string[:app.curserPos]))
        
        
        
        for i in range(len(app.line[app.linepos]), 200):
            
            app.line[app.linepos].append('')
            
        app.carryover = app.string[app.curserPos:]
        
        
        finalvalid = 0
        for i in range(len(app.carryover)):
            
            if app.carryover[i] == '':
                
                break
                
        #print(i)
        
        
        app.carryover = app.string[app.curserPos:app.curserPos + i]
        
    
        app.posperrow[app.linepos] -= len(app.carryover)    
            
    
            
        for i in range(200):
            
            
            if i < len(app.carryover):
                
                app.string[i] = app.carryover[i]
                
            else:
                
                app.string[i] = ''
            
        app.curserPos = 0
        app.linepos += 1
        
        #print(app.currrow, app.curserPos)    
        app.posperrow.insert(app.linepos, app.curserPos +  len(app.carryover))
      
        #print(app.posperrow)
        app.line.insert(app.currrow, app.string)
        
        
        
        
        app.carryover = []
  

    
        
def drawLetter(app):
    
    col = 0
    row = 0
    
   
    
    drawRect(app.pagetop[0], app.pagetop[1], app.pagedim[0], app.pagedim[1], fill = 'paleTurquoise', border = 'darkgrey', borderWidth = 5)
    
    
    for linePos in range(len(app.line)):
        
        
        if linePos > app.colletterfit:
            
           
            continue
        
        line = app.line[linePos]
        linelen = len(line)
        col = 0
        
        for letterpos in range(len(line)):
            offset = 0
            
            
            letterText = line[letterpos]
            
            if line[letterpos] == "space":
                
                letterText = ' '
                
                
            elif letterpos == (linelen-1):
                
                
                
                drawLabel('\n', 110 + col, 120 + row, fill="black", size=18, align='center')
                
                col = 0
                row += 20
                continue
            
            elif (letterpos > app.rowletterfit and letterpos !=0):
                
               
                continue
            
            elif letterText in ('d', 'i', 'f', 'l', 'k', 't', 'h', 'b') or letterText.isupper() or letterText.isdigit():
                offset = -1.4
            
            elif letterText == ',':
                
                offset = 5

            
            
            drawLabel(letterText, app.pagetop[0] + (10 + col), (app.pagetop[1] + 20) + row + offset, fill="black", size=20, font='monospace', align = 'center')
            col += 10
            offset = 0
            
     
    #curser
    
    
    if app.EnableTyping == True and (55 + (app.curserPos * 10) < app.pagedim[0]  and (30 + (app.currrow * 20)) < app.pagedim[1]):
        
        drawRect(app.pagetop[0] + 5 + (app.curserPos * 10), app.pagetop[1] + 10 + (app.currrow * 20), 2, 15 , fill = app.cursercolor, opacity=app.opac)

def EnableDraw(app, mouseX, mouseY):
    
    InX = mouseX > app.pagetop[0] and mouseX < (app.pagetop[0] + app.pagedim[0])
    InY = mouseY > app.pagetop[1] and mouseY < (app.pagetop[1] + app.pagedim[1])
    
    if InX and InY:
        app.EnableTyping = True
        
    else:
        app.EnableTyping = False
        
        
        
def Resize(app, mouseX, mouseY):
   
        
    if app.EnableTyping and (app.pagedim[0] > 9 or app.pagedim[1] < 10):
        
      
        app.pagedim[0] = mouseX
        app.pagedim[1] = mouseY
        
    if app.pagedim[0] <= 10:
        
        app.pagedim[0] = 10
      
    if app.pagedim[1] <= 10:
        
        app.pagedim[1] = 9
    
    app.rowletterfit = math.floor((app.pagedim[0] / app.textsize))
    
    app.colletterfit = math.floor((app.pagedim[1] / app.rowspace))
        
    