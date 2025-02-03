import csv

def load_regions(region_file):
    regions = []
    with open(region_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                chrom, start, end = parts[0], int(parts[1]), int(parts[2])
                regions.append((chrom, start, end))
    return regions

def filter_pvar(pvar_file, regions):
    matching_lines = []
    with open(pvar_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            if line[0].startswith('#CHROM'):
                matching_lines.append('\t'.join(line))  # Store header
                continue
            
            if len(line) < 2:
                continue  # Skip malformed lines
            
            chrom, pos = line[0], int(line[1])
            
            for region in regions:
                if chrom == region[0] and region[1] <= pos <= region[2]:
                    matching_lines.append('\t'.join(line))  # Store matching line
                    break  # No need to check other regions once matched
    return matching_lines

def extract_positions(pvar_file):
    positions = set()
    with open(pvar_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # Skip header
        for line in reader:
            if len(line) >= 2:
                positions.add(line[1])
    return positions

def find_matching_lines(sstats_file, pos_nlrp3, pos_mefv, output_file):
    with open(sstats_file, 'r') as f, open(output_file, 'w') as out_f:
        for line in f:
            if any(pos in line for pos in pos_nlrp3) and any(pos in line for pos in pos_mefv):
                out_f.write(line)

if __name__ == "__main__":
    pvar_nlrp3 = "../aux/pvar.nlrp3.out"
    pvar_mefv = "../aux/pvar.mefv.out"
    sstats_file ="../aid_exons_arrays/sstats.txt"
    output_file = "../aux/match.mefv.nlrp3.out"
    
    pos_nlrp3 = extract_positions(pvar_nlrp3)
    pos_mefv = extract_positions(pvar_mefv)
    
    find_matching_lines(sstats_file, pos_nlrp3, pos_mefv, output_file)