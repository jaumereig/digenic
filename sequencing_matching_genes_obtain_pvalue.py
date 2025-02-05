import re

# Function to parse a region file into a dictionary
def parse_region_of_interest(file_path):
    region_of_interest = {}
    with open(file_path, 'r') as f:
        line = f.readline().strip()
        chrom, start, end = line.split('\t')
        region_of_interest['chrom'] = chrom
        region_of_interest['start'] = int(start)
        region_of_interest['end'] = int(end)
    return region_of_interest

# Function to check if a position matches the region of interest
def is_position_in_region(position, region_of_interest):
    match = re.match(r"^chr(\w+):(\d+)$", position)
    if not match:
        return False
    chrom = match.group(1)
    pos = int(match.group(2))
    return chrom == region_of_interest['chrom'] and region_of_interest['start'] <= pos <= region_of_interest['end']

# Function to process sstats_p0.05 file and find matches
def process_sstats_file(region_mefv, region_nlrp3, input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            columns = line.strip().split('\t')
            if len(columns) < 2:
                continue
            pos1 = columns[0]
            pos2 = columns[1]
            
            # Check both positions in both region_of_interest files
            match_mefv1 = is_position_in_region(pos1, region_mefv)
            match_mefv2 = is_position_in_region(pos2, region_mefv)
            match_nlrp31 = is_position_in_region(pos1, region_nlrp3)
            match_nlrp32 = is_position_in_region(pos2, region_nlrp3)
            
            # We need both positions (pos1 and pos2) to match one of the regions
            if (match_mefv1 or match_nlrp31) and (match_mefv2 or match_nlrp32):
                outfile.write(line)

# Main execution flow
def main():
    # Paths to input files
    region_of_interest_mefv_path = 'region_of_interest_mefv.txt'
    region_of_interest_nlrp3_path = 'region_of_interest_nlrp3.txt'
    sstats_file_path = 'sstats_p0.05'
    output_file_path = 'sequencing.match.mefv.nlrp3.out'
    
    # Parse the region of interest files
    region_mefv = parse_region_of_interest(region_of_interest_mefv_path)
    region_nlrp3 = parse_region_of_interest(region_of_interest_nlrp3_path)
    
    # Process sstats file and generate output
    process_sstats_file(region_mefv, region_nlrp3, sstats_file_path, output_file_path)
    print(f"Matching lines have been written to {output_file_path}")

# Run the script
if __name__ == "__main__":
    main()
