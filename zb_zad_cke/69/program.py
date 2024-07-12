#jedna linia to genotyp 
#gatunki to g1 g2 g3  łączy ich długość genu(lini)
#
def findGen(line):
  gens = []
  endingPostition = 0 #last end postition
  #go through all characters
  for i in range(0, len(line) - 1):
    #find start pattern
    if line[i] == "A" and line[i+1] == "A":
      # Found AA
      gen = ""
      #Ensure that end was found
      if i >= endingPostition: 
        k = i # select start index
        #go through chars (i -> end - 1)
        for k in range(i, len(line) - 1):
          #find end pattern
          if(line[k] == "B" and line[k+1] == "B"):
            # found ending
            endingPostition = k #define where should start
            gen += "BB"
            break
          else:
            # not found ending. Add next char
            gen += line[k]

      # won't add gen if not have ending
      if gen.find("BB") > 0:
        gens.append(gen)
      
      gen = ""

  return gens

genotypes = []
allGenes = []
with open("C:/Users/Jan/Desktop/KOREPETYCJE/KOREPETYCJE/69/dane_geny.txt") as data: 
    for line in data:
        line = line.strip()
        genotypes.append(line)
        allGenes.append(findGen(line))



def zad1():
    spieces = set()
    maxNumber = 0

  # add unique species
    for i in range(0, len(genotypes)):
        species.add(len(genotypes[i]))

    for spec in species:
    counter = 0
    for genot in genotypes:
        if len(genot) == spec:
            counter += 1

    if counter > maxNumber:
      maxNumber = counter

    print("Liczba gatunkow: " + str(len(species)))
    print("Najwiekszy gatunek: " + str(maxNumber))
zad1()