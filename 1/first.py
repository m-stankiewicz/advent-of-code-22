def ReadFileToLines(file):
    equipmentFile = open(file)
    equipmentFileLines = equipmentFile.readlines()
    return equipmentFileLines

def LinesToArr(lines):
    reindeerEquipments = []
    singleEquipment = []
    for line in lines:
        if line == '\n':
            reindeerEquipments.append(singleEquipment)
            singleEquipment = []
        else:
            singleEquipment.append(int(line))
    return reindeerEquipments

def sumArr(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

def FindTotalBiggest(Equipments):
    biggest = 0
    for i in Equipments:
        sum = sumArr(i)
        if sum > biggest:
            biggest = sum
    return biggest 

def FindTotalThreeBiggest(Equipments):
    threeBiggest = []
    for i in Equipments:
        if len(threeBiggest) < 3:
            threeBiggest.append(sumArr(i))
            threeBiggest.sort()
        else:
            sum = sumArr(i)
            if sum > threeBiggest[0]:
                threeBiggest[0] = sum
                threeBiggest.sort()
    return sumArr(threeBiggest) 

filename = "first.txt"
lines = ReadFileToLines(filename)
Equipments = LinesToArr(lines)
print(FindTotalBiggest(Equipments))
print(FindTotalThreeBiggest(Equipments))