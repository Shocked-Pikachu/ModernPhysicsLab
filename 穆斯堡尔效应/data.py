def cal(filename):
    doseSum = 0
    m = 0
    with open(filename, 'r') as file:
        next(file)
        next(file)
        next(file)
        for line in file:
            numbers = line.split()
            if len(numbers) != 4:
                continue
            if numbers[0] == 'Organ ID|':
                continue
            organMass = float(numbers[1])
            dose = float(numbers[2])
            doseSum += dose * organMass
            m += organMass
            print(organMass, dose)
    return doseSum/m

print(cal('fig/Co57.out'))