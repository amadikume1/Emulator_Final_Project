#Emulator

Emodes = {'111': "ALU", '100':"ALU_RI", '001':"ALU_I", '010': "Load", '110': "Store", '011': "Branch", "101": "RStore"}

EALU_OP = {'1000': 'ADD', '1100':'SUB', '1110': "MUL", '1111':"DIV", "0001":"MOD", "0011":"POW", "0111": "EQL", "1001": "AND", "1011": "OR", "0010": "FLR"}  

EBranchOP = {'10000': "JPI", '11000':'JPR', '11100': 'JPRI', '11110': 'JPII', '11111': 'JPIR', '00001': 'JPRR', '01001': "JMPCIR", '01101': "JMPCRI"}

ECBOP = {"001":"GRAT", "011":"LESS", "111": "EQL", "101": "AND", "110": "OR"}

EStoreOP = {'1': 'R-to-M', '0': 'I-to-M'}

ELoadOP = {'11': 'LODI', '10': "LODR", '01': "LODM", '00': 'LODMR'}

#test binary instruction


Videocolors = [
    'lightSalmon', 'darkSalmon', 'lightCoral', 'salmon', 'crimson', 'red', 
    'fireBrick', 'darkRed', 'coral', 'tomato', 'orange', 'darkOrange', 
    'orangeRed', 'lightYellow', 'lemonChiffon', 'lightGoldenrodYellow', 
    'papayaWhip', 'moccasin', 'peachPuff', 'paleGoldenrod', 'khaki', 
    'yellow', 'darkKhaki', 'gold', 'paleGreen', 'lightGreen', 
    'mediumAquamarine', 'greenYellow', 'darkSeaGreen', 'yellowGreen', 
    'mediumSpringGreen', 'chartreuse', 'springGreen', 'lightSeaGreen', 
    'lawnGreen', 'mediumSeaGreen', 'limeGreen', 'oliveDrab', 'darkCyan', 
    'seaGreen', 'olive', 'teal', 'lime', 'darkOliveGreen', 'forestGreen', 
    'green', 'darkGreen', 'lightCyan', 'paleTurquoise', 'powderBlue', 
    'lightBlue', 'aquamarine', 'lightSteelBlue', 'lightSkyBlue', 'skyBlue', 
    'aqua', 'cyan', 'turquoise', 'cornflowerBlue', 'mediumTurquoise', 
    'mediumSlateBlue', 'deepSkyBlue', 'dodgerBlue', 'darkTurquoise', 
    'cadetBlue', 'royalBlue', 'steelBlue', 'blue', 'mediumBlue', 
    'midnightBlue', 'darkBlue', 'navy', 'lavender', 'thistle', 'violet', 
    'plum', 'orchid', 'fuchsia', 'magenta', 'mediumOrchid', 'mediumPurple', 
    'mediumSlateBlue', 'blueViolet', 'darkOrchid', 'slateBlue', 'darkViolet', 
    'darkMagenta', 'darkSlateBlue', 'purple', 'indigo', 'pink', 'lightPink', 
    'hotPink', 'paleVioletRed', 'deepPink', 'mediumVioletRed', 'cornSilk', 
    'blanchedAlmond', 'bisque', 'navajoWhite', 'wheat', 'burlyWood', 'tan', 
    'sandyBrown', 'rosyBrown', 'goldenrod', 'peru', 'chocolate', 
    'darkGoldenrod', 'sienna', 'brown', 'saddleBrown', 'maroon', 'white', 
    'snow', 'ghostWhite', 'azure', 'ivory', 'mintCream', 'floralWhite', 
    'aliceBlue', 'lavenderBlush', 'seashell', 'honeydew', 'whiteSmoke', 
    'oldLace', 'linen', 'beige', 'mistyRose', 'antiqueWhite', 'gainsboro', 
    'lightGray', 'silver', 'darkGray', 'lightSlateGray', 'gray', 
    'slateGray', 'dimGray', 'darkSlateGray', 'black'
]



#convert binary string to integer
def BinaryToDec(binary):
    
    num = 0
    
    binary = binary[::-1]
    
    for i in range(len(binary)):
        
        num += int(binary[i]) * (2**i)
        
    
    
    if num > (2**len(binary))/2:
        
        
        
        num = num - (2**len(binary)) 
        
        
    
        
    return num
    
#inizilize RAM to a collection of 0 values
def InizilizeRAM(RAM):
    
    for _ in range(1000):
        
        RAM.append(0)
  
  
        
#inizilize Registers to a collection of 0 values      
def InizilizeRegister(Registers):
    
    for _ in range(32):
        
        Registers.append(0)
        
    
        
#split and interpret binary for ALU operation       
def GetAluInfo(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(EALU_OP[binary[3:7]])
    
    alu_list.append(BinaryToDec(binary[7:12]))
    
    
    alu_list.append(BinaryToDec(binary[12:17]))
    alu_list.append(BinaryToDec(binary[17:22]))
    
    return alu_list
    
    
#split and interpret binary for ALU Register-Immediate operation   

def GetAluRIInfo(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(EALU_OP[binary[3:7]])
    alu_list.append(BinaryToDec(binary[7:12]))
    alu_list.append(BinaryToDec(binary[12:17]))
    alu_list.append(BinaryToDec(binary[17:32]))
    
    return alu_list
    
#split and interpret binary for ALU Immediate operation    
def get_aluI_info(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(EALU_OP[binary[3:7]])
    alu_list.append(BinaryToDec(binary[7:12]))
    alu_list.append(BinaryToDec(binary[12:22]))
    alu_list.append(BinaryToDec(binary[22:32]))
    
    return alu_list
  
  
 
def GetLoadRInfo(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(ELoadOP[binary[3:5]])
    alu_list.append(BinaryToDec(binary[5:10]))
    alu_list.append(BinaryToDec(binary[10:15]))
    
    return alu_list
    
    
def GetLoadIInfo(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(ELoadOP[binary[3:5]])
    alu_list.append(BinaryToDec(binary[5:10]))
    alu_list.append(BinaryToDec(binary[10:32]))
    
    return alu_list


def GetLoadMInfo(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(ELoadOP[binary[3:5]])
    alu_list.append(BinaryToDec(binary[5:10]))
    alu_list.append(BinaryToDec(binary[10:32]))
    
    return alu_list
    
    
def GetLoadMRInfo(binary):
    
    alu_list = []
    
    alu_list.append(Emodes[binary[0:3]])
    alu_list.append(ELoadOP[binary[3:5]])
    alu_list.append(BinaryToDec(binary[5:10]))
    alu_list.append(BinaryToDec(binary[10:15]))
    
    return alu_list
    


    
    
#split and interpret binary for Store operation   
def GetStoreInfo(binary):
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EStoreOP[binary[3]])
    aluList.append(BinaryToDec(binary[4:17]))
    
    if binary[3] == '1':
    
        aluList.append(BinaryToDec(binary[17:22]))
        
    else:
        
        aluList.append(BinaryToDec(binary[17:32]))
    
    
    
    return aluList

def GetRStoreInfo(binary):
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EStoreOP[binary[3]])
    aluList.append(BinaryToDec(binary[4:9]))
    
    if binary[3] == '1':
    
        aluList.append(BinaryToDec(binary[9:14]))
        
    else:
        
       
        aluList.append(BinaryToDec(binary[9:32]))
    
    
    return aluList
    



def GetJPIInfo(binary):
    
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    
    aluList.append(BinaryToDec(binary[8:32]))
   
   
    
    return aluList
    
    
def GetJPRInfo(binary):
    
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(BinaryToDec(binary[8:13]))
    
    
    return aluList
    
def GetJPRIInfo(binary):
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(BinaryToDec(binary[8:13]))
    aluList.append(BinaryToDec(binary[13:32]))
    
   
    return aluList
    
def GetJPIIInfo(binary):
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(BinaryToDec(binary[8]))
    aluList.append(BinaryToDec(binary[9:32]))
    
    return aluList

def GetJPIRInfo(binary):
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(BinaryToDec(binary[8]))
    aluList.append(BinaryToDec(binary[9:14]))
    
    return aluList
    
def GetJPRRInfo(binary):
    
    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(BinaryToDec(binary[8:13]))
    aluList.append(BinaryToDec(binary[13:18]))
    
    return aluList
    
def GetJMPCIRInfo(binary):
    

    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(ECBOP[binary[8:11]])
    aluList.append(BinaryToDec(binary[11:16]))
    aluList.append(BinaryToDec(binary[16:21]))
    aluList.append(BinaryToDec(binary[21:32]))
    
    
    return aluList

def GetJMPCRIInfo(binary):
    

    aluList = []
    
    aluList.append(Emodes[binary[0:3]])
    aluList.append(EBranchOP[binary[3:8]])
    aluList.append(ECBOP[binary[8:11]])
    aluList.append(BinaryToDec(binary[11:16]))
    aluList.append(BinaryToDec(binary[16:21]))
    aluList.append(BinaryToDec(binary[21:26]))
    
    
    return aluList

   
#this is the decode stage of the processor  
def decoder(binary):
    
    #this list will be used to store all the importent information about the current instruction
    importentInfo = []
    
    # find our adressing mode by finding first two bits in the mode dictionary
    curr_mode = Emodes[binary[:3]]
    
    
    #use adressing mode to determine how binary should be interpreted
    
    if curr_mode == "ALU":
        
        importentInfo = GetAluInfo(binary)
        
    elif curr_mode == "ALU_I":
        
        importentInfo = get_aluI_info(binary)
   
        
    elif curr_mode == "ALU_RI":
        
        importentInfo = GetAluRIInfo(binary)
    
    elif curr_mode == "Store":
        
        importentInfo = GetStoreInfo(binary)
        
        
    elif curr_mode == "RStore":
        
        importentInfo = GetRStoreInfo(binary)
    
    
    elif curr_mode == "Load":
        
        
        
        curr_mode = ELoadOP[binary[3:5]]
        
        if curr_mode == "LODI":
                
                importentInfo = GetLoadIInfo(binary)
                
        elif curr_mode == "LODM":
                
                importentInfo = GetLoadMInfo(binary)
                
            
        elif curr_mode == "LODR":
                
                importentInfo = GetLoadRInfo(binary)
                
        elif curr_mode == "LODMR":
            
                importentInfo = GetLoadMRInfo(binary)
                
        
        
        
        
    
    elif curr_mode == "Branch":    
        
  
        
        
        curr_mode = EBranchOP[binary[3:8]]
     
        
        if curr_mode == "JPI":
            
            importentInfo = GetJPIInfo(binary)
            
        elif curr_mode == "JPR":
            
            importentInfo = GetJPRInfo(binary)
            
        elif curr_mode == "RStore":
            
            importentInfo = GetRStoreInfo(binary)
            
        elif curr_mode == "JPRI":
            
            
            importentInfo = GetJPRIInfo(binary)
            
            
        elif curr_mode == "JPIR":
            
            importentInfo = GetJPIRInfo(binary)
        
            
        elif curr_mode == "JPRR":
            
            importentInfo = GetJPRRInfo(binary)
            
            
        elif curr_mode == "JMPCIR":
            
            importentInfo = GetJMPCIRInfo(binary)
        
        elif curr_mode == "JMPCRI":
            
            importentInfo = GetJMPCRIInfo(binary)
            
 
    return importentInfo


   
#this function acts as the ALU of the system, doing the core logic and arthmatic operations
#takes in two pieces of data, and the desired operation
def alu(data1, data2, op):
    
    #use switch case
    match op:
        case 'ADD':
            
            return data1 + data2
            
            
        case 'SUB':
            
            return data1 - data2
            
        case 'MUL':
            
            return data1 * data2
        
        case 'DIV':
            
            return int(data1 / data2)
            
            
        case 'OR':
            
            return data1 | data2
            
        case 'AND':
            
            
            return data1 & data2
        case "POW":
            
            return data1 ** data2
            
        case "EQL":
            
            return data1 == data2
            
        case "GRAT":
            
         
            
            return data1 > data2
            
        case "LESS":
            
            return data1 < data2
            
        case "MOD":
            
            return data1 % data2
            
        case "FLR":
            
            
            return data1 // data2
            
        case "Pass":
            
            return data1
 
 
 
#this is the execute stage of the processor
def execute(information, Registers):
    
    execute_info = []
    
    
    #if our instruction is a base ALU instruction
    if information[0] == "ALU":
        
    
        #provides adressing mode, and the instruction we want to excute in that adressing mode
        execute_info.extend([information[0], information[2]])
        
        #uses ALU fucntion to execute the described instruction on the data provided
        #in this case the data is taken from our register list
        execute_info.append(alu(Registers[information[3]], Registers[information[4]], information[1]))
       
    
    #if our instruction is a base ALU_RI instruction
    elif information[0] == "ALU_RI":
        
        execute_info.extend([information[0], information[2]])
        
        #in this case the data is both an immediate value, and is taken from our register list
        
        
        execute_info.append(alu(Registers[information[3]], information[4], information[1]))
        
        
    elif information[0] == "ALU_I":
        
        execute_info.extend([information[0], information[2]])
        
       
        execute_info.append(alu(information[3], information[4], information[1]))
        
    elif information[1] == "JPR":
        
        
     
        
        execute_info = information[:-1] + [Registers[information[-1]]]
        
        
    elif information[1] == "JPRI":
        
        
 
        execute_info = information[:-2] + [Registers[information[-2]]] + [information[-1]]
        
    
    elif information[1] == "JMPRR":
        
        execute_info = information[:-2] + [Registers[information[-2]]] + [Registers[information[-1]]]
    
    elif information[1] == "JMPCIR":
        
       
       
        execute_info = information[:-3] + [alu(Registers[information[-3]], Registers[information[-2]], information[2])] + [information[-1]]
        
        
    elif information[1] == "JMPCRI":
        
        
        execute_info = information[:-3] + [alu(Registers[information[-3]], Registers[information[-2]], information[2])] + [Registers[information[-1]]]
        
        
    else:
        
        #store instructions do not use alu operations
        execute_info = information
        
  
        
    return execute_info





#this is the store stage of the processor
def store(information, Registers, Memory, app):
    
    


    
    #if the Store instruction is for immediate to memory, then the data is directly indexed into the RAM list
    if information[0] == 'Store' and information[1] == 'I-to-M':
        
        if information[2] >= 100 and information[2] < 103:
            
            
            app.CubeMemory.mem[information[2] - 100] = information[3]
            
        
        elif information[2] >= 50 and  information[3] < 140:
            
            app.VideoRAM.mem[information[2] - 50] = Videocolors[information[3]]
            
        
        elif information[2] < 100 and information[2] > 0:
            
            Memory[information[2]] = information[3]
        
    #if the Store instruction is for Register to memory, then the data is taken from Regsietr list, and indexed into the RAM list 
    elif information[0] == 'Store' and information[1] == 'R-to-M':
        
        
        if information[2] >= 100 and  information[2] < 103:
            
            app.CubeMemory.mem[information[2] - 100] = Registers[information[3]]
            
            
        
        elif information[2] >= 50 and  information[2] < 100 and  information[3] < 100:
            
            app.VideoRAM.mem[information[2] - 50] = Videocolors[Registers[information[3]]]
            
        
        
        elif information[2] < 100 and information[2] >= 0:
        
            Memory[information[2]] = Registers[information[3]]
            
            
        
    elif information[0] == "RStore" and information[1] == 'I-to-M':
        
        
        if Registers[information[2]] >= 100 and  Registers[information[2]] < 103:
            
                app.CubeMemory.mem[Registers[information[2]] - 100] = information[3]
            
        
        
        elif Registers[information[2]] >= 50 and  Registers[information[2]] < 100:
            
            app.VideoRAM.mem[Registers[information[2]]- 50] = Videocolors[information[3]]
            
            
            
        elif Registers[information[2]] < 100  and Registers[information[2]] >= 0:
        
            Memory[Registers[information[2]]] = information[3]
            
            
        
        
    elif information[0] == "RStore" and information[1] == 'R-to-M':
        
        
        
            
        if Registers[information[2]] >= 100 and  Registers[information[2]] < 103:
            
            
            
            app.CubeMemory.mem[Registers[information[2]] - 100] = Registers[information[3]]
            
        
        
        elif Registers[information[2]] >= 50 and  Registers[information[2]] < 100:
            
            
            
            app.VideoRAM.mem[Registers[information[2]] - 50] = Videocolors[Registers[information[3]]]
            
        
        elif Registers[information[2]] < 100  and Registers[information[2]] >= 0:
        
          
            
            Memory[Registers[information[2]]] = Registers[information[3]]
            
        
        
    else:
        
        
        return information

    
#this is the load stage of the processor
def load(Register, information, RAM, app): 
  
    if information == None:
        
        return None
        
    
    if type(information) == list and information[0] in ('ALU_RI', 'ALU', 'ALU_I'):
        
   
        
        Register[information[1]] = information[-1]
        
        
    elif information[1] == 'LODI':
        
        Register[information[2]] = information[-1]
        
    elif information[1] == 'LODR':
        
        Register[information[2]] = Register[information[-1]]

        
    elif information[1] == 'LODM':
        
        if information[-1] >= 100 and  information[-1]  < 103:
        
              
            Register[information[2]] = app.CubeMemory.mem[information[-1] - 100]
            
            
        elif information[-1] >= 50 and  information[-1]  < 100:
            
        
             Register[information[2]] = information[-1] - 50
             
        elif information[-1]  < 100  and information[-1] >= 0:
            
             Register[information[2]] = RAM[information[-1]]
             
             
        
    elif information[1] == 'LODMR':
        
        if Register[information[-1]] >= 100 and  Register[information[-1]] < 103:
            
            Register[information[2]] = app.CubeMemory.mem[Register[information[-1]] - 100]
            
        
        
        elif Register[information[-1]] >= 50 and  Register[information[-1]]< 100:
            
            
            
             Register[information[2]] = Register[information[-1]] - 50
             
             
        elif Register[information[-1]] < 100  and Register[information[-1]] >= 0:
            
             Register[information[2]] = RAM[Register[information[-1]]]