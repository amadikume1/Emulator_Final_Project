# Custum_Emulator_Project


<img width="1260" height="1017" alt="image" src="https://github.com/user-attachments/assets/d2c8b8b7-4e8c-476f-ac3e-37f33de0a3da" />



AKU32 System 32

A comprehensive 32-bit CPU emulator with assembly language support, visual memory management, and interactive programming environment built with Python and CMU Graphics.
Features

CPU Emulation

  32-bit architecture with 32 general-purpose registers (R1-R31)
  Complete instruction pipeline: Fetch → Decode → Execute → Store → Load
  Memory-mapped I/O with video memory and special memory regions
  Real-time execution with visual feedback

Programming Languages

  AKU32 Assembly Language: Full-featured assembly with multiple addressing modes
  Simple High-Level Language: C-like syntax that compiles to assembly
  Stack-based operations with built-in push/pop functionality

Interactive Features

  3D Cube Visualization: Control a rotating cube through memory-mapped registers
  Turtle Graphics: Logo-style drawing system with movement commands
  Visual Memory Browser: Interactive RAM, Register, and Video memory viewers
  Text Editor: Built-in editor with syntax highlighting and error reporting



Project Structure
-----------------

Folder | Description
-------------- | -----------
Main/ | Entry point and application controller
Emulator/ | Virtual machine core (CPU, memory, registers)
Assembler/ | Translates user-friendly code into VM instructions
Graphics/ | Handles drawing, UI, and graphics rendering
VM/ | High-level instruction execution engine
Language/ | Parses user-level syntax and tokens
Turtle/ | Implements turtle-graphics-like behavio



CMU Graphics Modifications
--------------------

  Missing Keys
 -------------------
    This project uses the cmu_graphics library, which uses pygame to handle key input events.
    Custom Emulator Project
    
    However, the version originally downloaded did not correctly register the following keys:
    - Insert
    - Delete
    - End
    - Home
    - Page Up
      
    To fix this, the getKey function in the cmu_graphics.py source was modified by updating the
    keyNameMap dictionary:
    
     pygame.K_INSERT: 'insert',
     pygame.K_DELETE: 'delete',
     pygame.K_END: 'end',
     pygame.K_PAGEUP: 'pageup',
     pygame.K_PAGEDOWN: 'pagedown',
     pygame.K_HOME: 'home',
     
    If you're using this project with your own cmu_graphics installation, apply this patch to ensure
    full key input compatibility.
  

  Key State Tracking Bug
  -------------------------
  
    Issue: When holding Shift + another key and Pressiing quickly, the library would sometimes miss key release events, causing keys to appear "stuck" in a pressed state.
    
    Root Cause: The self._allKeysDown set could become desynchronized with actual key states, leading to phantom held keys.
    
    Solution: Added key state verification  variable using pygame's direct key checking:

                elif event.type == pygame.KEYDOWN:
                                      self.handleKeyPress(event.key, event.mod)
          
                                      if (event.key != pygame.K_LSHIFT) and (event.key != pygame.K_RSHIFT):
                                                  
                                                  true_count += 1
                                          
          
          
                                       
                elif event.type == pygame.KEYUP:
                                      self.handleKeyRelease(event.key, event.mod)
          
                                      if (event.key != pygame.K_LSHIFT) and (event.key != pygame.K_RSHIFT):
                                          true_count -= 1

      Now when an Miss-Fire occurs, it will be detetcetd, and the self.allKeysDown variable will be set to an empty set, so be refiled with accurate info

                if len(self._allKeysDown) > 0 and true_count == len(self._allKeysDown):
      
                                  
      
                                  print("KeyHoldCalled", len(self._allKeysDown), self._allKeysDown, true_count)
                                  
      
                                  self.callUserFn(
                                      'onKeyHold',
                                      (list(self._allKeysDown), list(self._modifiers)),
                                  )
      
                 else: 
      
                                  self._allKeysDown = set()

                                          
          
                                          

    
  
Program Flow
-------------------

    1. Launch the application
    2. Press TAB for help screens
    3. Type your first assembly program
    4. Press HOME to assemble and run
    5. Press DELETE to reset text area




Assembly Language Reference
-----------------------------

  Instruction Format
  
    - Operation, Destination- Source1 [OP] Source2



Core Instructions
-----------------------------
  ALU Operations
    
      ALU, Rd- Rs1 [OP] Rs2 - Register-Register operations
      ALU_RI, Rd- Rs [OP] IMM - Register-Immediate operations
      ALU_I, Rd- IMM1 [OP] IMM2 - Immediate-Immediate operations


  Available Operations: ADD, SUB, MUL, DIV, MOD, POW, EQL, AND, OR, FLR

  
  Memory Operations
      
      LOD, Rd- IMM - Load immediate value
      LOD, Rd- Rs - Load from register
      LOD, Rd- *IMM - Load from memory address
      LOD, Rd- *Rs - Load from memory address in register
      STORE, *IMM- Rs - Store register to memory
      STORE, *Rs- Rd - Store using register as address
  
  Control Flow
      
      JMP, IMM - Jump to immediate address
      JMP, Rs - Jump to register value
      JMP, Rs- IMM - Jump to register + immediate
      JMP, Rs [COND] Rt- IMM - Conditional jump

  
  Conditions: GRAT (>), LESS (<), EQL (==)


  Stack Operations
  
      Push, value - Push value or register to stack
      Pop, destination - Pop from stack to register



  Memory Map
  --------------------
  
      RAM: Addresses 0-49 (General purpose memory)
      Video Memory: Addresses 50-99 (Display buffer)
      Cube Control: Addresses 100-102 (3D cube rotation)

  
  High-Level Language Variable Assignment
  _________________________________________

        Syntax: Var_Name = Integer



Interactive Features
_______________________

  3D Cube Control
  -----------------
    Control a rotating 3D cube by writing to memory addresses 100-102:


  Turtle Graphics
  -------------------
    Create drawings using turtle-style commands:
    
    w - Move up
    s - Move down
    a - Move left
    d - Move right
    + - drop current color on block
    - - remove color from block

  Video Display
  -------------------
    Create pixel art by writing color values to video memory (addresses 50-99):


Controls & Shortcuts
_________________________

Navigation
    
    TAB - Show help screens
    HOME - Assemble and run program
    ESC - Stop program execution
    DELETE - Clear text editor

Special Modes

    INSERT - Enter typing calibration mode
    END - Enter turtle graphics mode
    PAGE UP - Toggle 3D cube display
    PAGE DOWN - Reset cube rotation

Text Editor

    Standard text editing with cursor support
    Multi-line editing 
    error highlighting
    Drag and resize text area

Architecture Details

  Register File
  -----------------
    
    R1-R29: General purpose registers
    R30: Stack pointer (SP)
    R31: Base pointer/Frame pointer
  
  Instruction Encoding
  ---------------------

    32-bit instructions with variable field lengths
    3-bit operation mode identifier
    Multiple addressing modes for flexibility
    Immediate values up to 24 bits

  Stages
  -----------------

    Fetch: Retrieve instruction from ROM
    Decode: Parse instruction format and extract operands
    Execute: Perform ALU operations and address calculations
    Store: Write results to memory
    Load: Update register file

Error Handling
  
    error detection during assembly
    Visual error highlighting in source code
    error messages
    Interactive error pop-up boxes



Contributing
______________

This project demonstrates concepts in:

    Computer architecture and CPU design
    Assembly language implementation
    Compiler design and parsing
    Interactive graphics programming
    Educational software development


Acknowledgments
__________________

    Built using CMU Graphics library
    3D graphics theory from educational resources
    Assembly language design inspired by classic architectures

