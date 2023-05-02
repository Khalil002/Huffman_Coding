import os
import sys
import filecmp

def main():
    f1 = sys.argv[1]
    f2 = "descomprimido-elmejorprofesor.txt"
    
    if os.path.exists(f1) == False:
        print(f1+" does not exist")
        exit(0)
    elif os.path.exists(f2) == False:
        print(f2+" does not exist")
        exit(0)
        
    if filecmp.cmp(f1, f2):
        print("ok")
    else:
        print("nok")
        
    
if __name__ == "__main__":
    main()