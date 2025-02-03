import csv

def load_regions(region_file): #! llegir fitxer amb coordenades del gen que volem extreure
    regions = []
    with open(region_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                chrom, start, end = parts[0], int(parts[1]), int(parts[2]) #! separem la línia del fitxer en 3 parts: cromosoma, start i end
                regions.append((chrom, start, end)) #! les 3 coordenades les posem en una llista que es diu regions
    return regions

def filter_pvar(pvar_file, regions): #! llegim el fitcer amb tots els genotips (aid.pvar) i la llista regions que hem creat abans
    with open(pvar_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            if line[0].startswith('#CHROM'):
                print('\t'.join(line))  #! Print header al fitxer output
                continue
            
            if len(line) < 2:
                continue  #! Skip malformed lines
            
            chrom, pos = line[0], int(line[1])
            
            for region in regions:
                if chrom == region[0] and region[1] <= pos <= region[2]:
                    print('\t'.join(line))  #! Print matching line
                    break  #! No need to check other regions once matched

if __name__ == "__main__":
    region_file = "../region_of_interest.txt"
    pvar_file = "../aux/aid.pvar"
    output_file = "../pvar.nlrp3.out"

    regions = load_regions(region_file)
    filter_pvar(pvar_file, regions)