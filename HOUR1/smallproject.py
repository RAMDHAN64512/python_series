
server=input("Enter Server name ")

cpu = float(input("Enter CPU usage "))
ram = float(input("Enter ram usage "))
disk = float(input("Enter disk usage "))

print("======Python analyzer=======")
print("cpu =",cpu,"%")
print("ram",ram,"%")
print("disk",disk,"%")
print("Average usage ",cpu+ram+disk/3 ,"%")

if cpu>80 or ram >80 or disk>80:
    print("WARNNIG! High alert")
else:
    print("Condition is normal")    
    
print("============================")