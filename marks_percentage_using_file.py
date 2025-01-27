name=input("Enter the name:")
mark1=int(input("Enter the mark for PHYSICS:"))
mark2=int(input("Enter the mark for CHEMISTRY:"))
mark3=int(input("Enter the mark for MATHEMATICS:"))

def percentage_of_marks(name,mark1,mark2,mark3):
    return ((mark1+mark2+mark3)/3)
          
percentage=percentage_of_marks(name,mark1,mark2,mark3)
print("NAME\tPHYSICS\t  CHEMISTRY\tMATHEMATICS\n")
print(f"{name}\t {mark1}\t  {mark2}\t\t{mark3}\n")
print(f"PERCENTAGE:{percentage:.2f}\n")

report_card_content=(f"REPORT CARD \n-------------------\nNAME:{name}\nPHYSICS:{mark1}\nCHEMISTRY:{mark2}\nMATHEMATICS:{mark3}\nPERCENTAGE:{percentage:.2f} \n --------------------")
    
with open(f"{name}_report_card.txt","w") as file:
    file.write(report_card_content)
