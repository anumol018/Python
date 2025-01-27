name=input("Enter the name:")
mark1=int(input("Enter the mark for PHYSICS:"))
mark2=int(input("Enter the mark for CHEMISTRY:"))
mark3=int(input("Enter the mark for MATHEMATICS:"))

def percentage_of_marks(name,mark1,mark2,mark3):
    percentage=((mark1+mark2+mark3)/3)
    print("NAME\tPHYSICS\t  CHEMISTRY\tMATHEMATICS\n")
    print(f"{name}\t {mark1}\t  {mark2}\t\t{mark3}\n")
    print(f"PERCENTAGE:{percentage:.2f}\n")
          
percentage_of_marks(name,mark1,mark2,mark3)
    
