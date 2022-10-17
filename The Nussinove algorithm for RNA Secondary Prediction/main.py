from builtins import range, print

f={156 : 'R',
114 : 'N',
115 : 'D',
103 : 'C',
129 : 'E',
128 : 'Q',
57 : 'G',
137 : 'H',
113 : 'I',
113 : 'L',
128 : 'K',
131 : 'M',
147 : 'F',
97 : 'P',
87 : 'S',
101 : 'T',
186 : 'W',
163 : 'Y',
99 : 'V',
71 : 'A'
}

file = open("weight.txt")
amino_weight_dict={}
# read weights file and save data in dictionary
for f in file:
    line= f.rstrip()
    dict_values=line.split(" ")
    amino = dict_values[0]
    weight_value = int(dict_values[1])
    amino_weight_dict[amino]=weight_value

weight_amino_dict={}
file2 = open("reverse weight.txt")
# read weights file and save data in dictionary
for f in file2:
    line= f.rstrip()
    dict_values=line.split(" ")
    weight_value = int(dict_values[0])
    amino = str(dict_values[1])
    weight_amino_dict[weight_value] = amino

#function that return the theortical spectrum
sorted_weights =[]
def lin_spectrum(full_peptide):
    peptide_divisions=[]
    for i in range(len(full_peptide)):
        for j in range(len(full_peptide)):
            if (i+j)< len(full_peptide):
                 peptide_divisions.append(full_peptide[j:j+i+1])
            #else:
             # sublist.append(peptide[j:len(peptide)]+peptide[0:(i+j)-len(peptide)])

    total_weight = [0]
    #loop calculate weights for each element in the list
    for i in peptide_divisions:
            total_weight.append(weight_calc(i))
    #the totals list must be sorted
    sorted_weights=sorted(total_weight)
    return sorted_weights

#function take each element in the sublist to calculate the weight
def weight_calc(pep_seq):
    sum=0
    for s in pep_seq:
        sum+=amino_weight_dict[s]
    return sum


def cons(pep_seq):
    StrFrame1 = []
    out1=[]
    i = 0
    weightList = []
    for i in range(len(lin_spectrum(pep_seq))):
        weightList.append(lin_spectrum(pep_seq)[i])
        #print(weightList[i])
    for i in range(len(pep_seq)):
        StrFrame1.append(pep_seq[i])

        #print(StrFrame1[i])
    for i in range(len(StrFrame1)):
            for j in range(len(weightList)):
                    if(amino_weight_dict[StrFrame1[i]] == weightList[j]):
                        print("Output = ",i , " " , StrFrame1[i] , " : ", j ,' ', amino_weight_dict[StrFrame1[i]])
                        out1.append(amino_weight_dict[StrFrame1[i]])

                        break
    inital_list(out1)

def inital_list(sort_weight):
    #for i in range (len(f)):
    stringList2=[]
    p = []
    SeqFram1ListStr = []
        #for j in range(len(weight_amino_dict)):
         # if (weight_amino_dict[sort_weight[i]] == sort_weight[i]):
    print("ff = ", sort_weight)
    for i in range (len(sort_weight)):
            if(i != len(sort_weight)):
                print("Output22 = ", weight_amino_dict[sort_weight[i]])
                p.append(weight_amino_dict[sort_weight[i]])

    for i in range(len(p)):
        stringList2.append(p[i:i + 2])

    for i in range(len(stringList2)):
        SeqFram1ListStr = [''.join([str(elem) for elem in sublist]) for sublist in stringList2]


    for i in range(len(SeqFram1ListStr)):
        print("gg = ",SeqFram1ListStr[i])

    string3 = ''
    i = 0
    for i in p:
        string3 = string3 + i + " "


    w=[]

    Q =list(SeqFram1ListStr)
    for i in range(len(SeqFram1ListStr)):
        for j in range(len(p)):
            w.insert(0, string3[j]+SeqFram1ListStr)

       # print("ff = ", stringList2[i])


#Main
peptide = input("Enter the Peptide: ")

p =  cons(peptide)
print(p)
#print(lin_spectrum(peptide))