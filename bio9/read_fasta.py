def read_fasta(filename):
    """Returns a dictionary associating labels with DNA."""
    result = {}
    with open(filename, 'rt') as f:
        dna = ''
        label = ''
        for line in f:
            if line.startswith('>'):
                if label != '':
                    result[label] = dna
                label = line[1:-1]
                dna = ''
            else:
                dna += line[:-1]
        result[label] = dna
        return result
        
def pairs(dictionary):
    for key1 in dictionary:
        for key2 in dictionary:
            if key1 != key2:
                value1 = dictionary[key1]
                value2 = dictionary[key2]
                if value1[-3:] == value2[:3]:
                    print (key1, key2)
                    
pairs(read_fasta('rosalind_grph.txt'))
