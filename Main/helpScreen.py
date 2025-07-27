
from Main.Initial import *
#Help screen

def HelpStart(app): 
    
    app.HelpScreenUp = False
    app.HelpLabelX = app.width / 2
    app.HelpLabelY = app.height / 2
    
    
def BaseHelpScreen(app):
    
    
    
    
    drawRect(0, 0, app.width, app.height, fill = 'salmon')
    
    
          
    drawLabel("Welcome all to the AKU32", app.CalLabelX, app.CalLabelY, size = 40, font= 'monospace')
    
    drawLabel("System 32", app.CalLabelX, app.CalLabelY+70, size = 30, font= 'monospace')
    

    drawLabel("Hit the mouse button for information of each feature", app.CalLabelX, app.CalLabelY+120, size = 20, font= 'monospace')
    
    
def LastHelpScreen(app):
    
    drawRect(0, 0, app.width, app.height, fill = 'salmon')
    
    
    drawLabel("Now if your ready press delete and go on to the program", app.CalLabelX, app.CalLabelY, size = 25, font= 'monospace')
    

def AssemblyHelpScreen(app): #Written by ChatGPT
    

    drawRect(0, 0, app.width, app.height, fill = 'lightblue')
    
    baseX = app.width/2  
    startY = 40  
    lineHeight = 25  
    smallLineHeight = 20  
    
    drawLabel('The Assembly Language Reference', baseX, startY, size=32, bold=True, font='monospace')
    
    currentY = startY + 50
    
    drawLabel('Basic Instruction Format:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Operation, Operand1- Operand2', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 5
    
    drawLabel('Register Format:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('R1 through R31 (e.g., R1, R2, R30)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Special Registers:', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('R30: Stack Pointer', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('R31: Base Pointer', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 5
    
    drawLabel('Jump Commands:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('JMP, IMM            (Jump to immediate address)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('JMP, Rs             (Jump to register value)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('JMP, Rs- IMM        (Jump register plus immediate)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('JMP, Rs GRAT Rt- IMM (Jump if Rs > Rt to IMM)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('JMP, Rs LESS Rt- IMM (Jump if Rs < Rt to IMM)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('JMP, Rs EQL Rt- IMM  (Jump if Rs = Rt to IMM)', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 5
    
    drawLabel('ALU Operations:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('ALU, Rd- Rs1 [OP] Rs2    (Register-Register)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('ALU_RI, Rd- Rs1 [OP] IMM  (Register-Immediate)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('ALU_I, Rd- IMM1 [OP] IMM2 (Immediate-Immediate)', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 5
    
    drawLabel('Memory Operations:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('LOD, Rd- IMM     (Load immediate)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('LOD, Rd- Rs      (Load from register)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('LOD, Rd- *IMM    (Load from memory)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('STORE, *IMM- Rs  (Store to memory)', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 5

    colSpacing = 200
    leftX = baseX - colSpacing
    rightX = baseX + colSpacing

    drawLabel('Available Operations:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight

    drawLabel('ADD: Addition', leftX, currentY, size=20, font='monospace')
    drawLabel('POW: Power', rightX, currentY, size=20, font='monospace')
    currentY += smallLineHeight

    drawLabel('SUB: Subtraction', leftX, currentY, size=20, font='monospace')
    drawLabel('EQL: Equal comparison', rightX, currentY, size=20, font='monospace')
    currentY += smallLineHeight

    drawLabel('MUL: Multiplication', leftX, currentY, size=20, font='monospace')
    drawLabel('AND: Bitwise AND', rightX, currentY, size=20, font='monospace')
    currentY += smallLineHeight

    drawLabel('DIV: Division', leftX, currentY, size=20, font='monospace')
    drawLabel('OR: Bitwise OR', rightX, currentY, size=20, font='monospace')
    currentY += smallLineHeight

    drawLabel('MOD: Modulo', leftX, currentY, size=20, font='monospace')
    drawLabel('FLR: Floor division', rightX, currentY, size=20, font='monospace')
    currentY += lineHeight + 5
    
    drawLabel('Memory Map:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('RAM: Addresses 0-49', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Video Memory: Addresses 50-99', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Cube Control: Addresses 100-102', baseX, currentY, size=20, font='monospace')
    
    
    

def LanguageHelpScreen(app): #Written by ChatGPT
    
    drawRect(0, 0, app.width, app.height, fill = 'lightgreen')
    
    baseX = app.width/2  
    startY = 60  
    lineHeight = 30  
    smallLineHeight = 25  
    
    drawLabel('Simple Programming Language Reference', baseX, startY, size=32, bold=True, font='monospace')
    
    currentY = startY + 60
    
    drawLabel('Basic Syntax:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('variable = value', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Variable Rules:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('- Variables are created automatically when used', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- Variables store integers only', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- Variable names can be any length', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Operations:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight

    colSpacing = 200
    leftX = baseX - colSpacing
    rightX = baseX + colSpacing

    drawLabel('+ : Addition', leftX, currentY, size=20, font='monospace')
    drawLabel('* : Multiplication', rightX, currentY, size=20, font='monospace')
    currentY += smallLineHeight

    drawLabel('- : Subtraction', leftX, currentY, size=20, font='monospace')
    drawLabel('/ : Division', rightX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Examples:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('x = 42', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('y = x + 10', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Memory Storage:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Variables are stored sequentially starting at R31', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('First variable at R31 + 0', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Second variable at R31 + 1', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Limitations:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('- No control flow (if, while, etc.)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- No functions or procedures', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- No string or floating point support', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- No Variables within Variables(please dont)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- Maximum of 32 variables', baseX, currentY, size=20, font='monospace')
    
    currentY += smallLineHeight
    currentY += smallLineHeight
    
    drawLabel('Not the greatest but its here, unfinished and boring', baseX, currentY, size=30, font='monospace')
    currentY += smallLineHeight
    drawLabel('like an unwanted child', baseX, currentY, size=30, font='monospace')
    currentY += smallLineHeight
    
    




def TurtleHelpScreen(app): #Written by ChatGPT
    
    drawRect(0, 0, app.width, app.height, fill = 'beige')
    
    baseX = app.width/2  
    startY = 60  
    lineHeight = 40  
    smallLineHeight = 30 
    
    drawLabel('Turtle Program Reference', baseX, startY, size=32, bold=True, font='monospace')
    
    currentY = startY + 60
    
    drawLabel('Controls:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('w - Move Up', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('s - Move Down', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('a - Move Left', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('d - Move Right', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('1 - Toggle Drawing', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 30
    
    drawLabel('How to Use:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('1. Press END to start Turtle mode', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('2. Type movement commands (w,a,s,d)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('3. Press SPACE to execute path', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('4. Press DELETE to clear/reset', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 30
    
    drawLabel('Memory Usage:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('R1: Current position', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('R2: Drawing color', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Video Memory (50-99): Display grid', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Example Path:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('w/w/d/+/s/-/s/a  -> (Up,Up,Right,Draw,Down,Erase,Down, Left)', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight
    



def CalibrationHelpScreen(app): #Written by ChatGPT
    
    drawRect(0, 0, app.width, app.height, fill = 'plum')
    
    baseX = app.width/2  
    startY = 60  
    lineHeight = 50 
    smallLineHeight = 35
    
    drawLabel('Text Calibration Reference', baseX, startY, size=32, bold=True, font='monospace')
    
    currentY = startY + 60
    
    drawLabel('Purpose:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Adjust key repeat timing for comfortable typing', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('How to Use:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('1. Press INSERT to enter calibration mode', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('2. Type normally at your preferred speed', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('3. Press SPACE or click mouse to finish', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('4. Press DELETE to cancel calibration', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Tips:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('- Type a few sentences to get accurate timing', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- Try different speeds to find what works best', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('- Calibration affects key repeat rate', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Settings:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Current key repeat delay:', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel(f'{app.timeforkeyPress:.2f} ms', baseX, currentY, size=20, font='monospa')
    
    currentY += smallLineHeight + 35
    
    drawLabel("", baseX, currentY, size=20, font='monospa')
    currentY += lineHeight + 10
    drawLabel("", baseX, currentY, size=20, font='monospa')
    currentY += lineHeight + 10
    drawLabel("", baseX, currentY, size=20, font='monospa')
    currentY += lineHeight + 10


def StackHelpScreen(app): #Written by ChatGPT
    
    drawRect(0, 0, app.width, app.height, fill = 'papayaWhip')
    
    baseX = app.width/2  
    startY = 60  
    lineHeight = 30  
    smallLineHeight = 25  
    
    drawLabel('Stack Operations Reference', baseX, startY, size=32, bold=True, font='monospace')
    
    currentY = startY + 60
    
    drawLabel('Stack Pointer:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('R30 is reserved as Stack Pointer (SP)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Stack grows upward in memory', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Push Operation:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Push, value', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Examples:', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Push, 42      (Push immediate)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Push, R1      (Push register)', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Push Implementation:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('ALU_RI, R30- R30 ADD 1', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('STORE, *R30- value', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Pop Operation:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Pop, destination', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Examples:', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Pop, R1       (Pop to register)', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Pop, DP       (Pop and discard)', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Pop Implementation:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('LOD, dest- *R30', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('STORE, *R30- 0', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('ALU_RI, R30- R30 SUB 1', baseX, currentY, size=20, font='monospace')
    currentY += lineHeight + 10
    
    drawLabel('Common Stack Operations:', baseX, currentY, size=24, bold=True, font='monospace')
    currentY += lineHeight
    
    drawLabel('Add numbers:', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Pop, R1', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Pop, R2', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('ALU, R3- R1 ADD R2', baseX, currentY, size=20, font='monospace')
    currentY += smallLineHeight
    
    drawLabel('Push, R3', baseX, currentY, size=20, font='monospace')
    
    currentY += smallLineHeight
    
    drawLabel('(there is also add, and if-true-goto, which take the first two positions in the stack, and operate on them:', baseX, currentY, size=15, font='monospace')
    
    currentY += smallLineHeight