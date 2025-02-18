


region_of_interest_mefv_path = '/home/vant/Escritorio/digenic/regions_of_interest/hg38/region_of_interest_mefv.txt'
region_of_interest_nlrp3_path = '/home/vant/Escritorio/digenic/regions_of_interest/hg38/region_of_interest_nlrp3.txt'
sstats_file_path = '../aid_genes_10Kb_wgs/sstats_p0.05'

output_file_path = '/home/vant/Escritorio/digenic/sequencing_out/mefv_nlrp3/sequencing.match.mefv.nlrp3.out'


region_one = []
region_two = []
sstats_lines = []


with open(region_of_interest_mefv_path, 'r') as file:
        for line in file:
            region_one = line.split()
            region_one_chr, region_one_start, region_one_end = [int(region_one[0]), int(region_one[1]), int(region_one[2])]
            #print(region_one_chr, region_one_start, region_one_end)




with open(region_of_interest_nlrp3_path, 'r') as file:
        for line in file:
            region_two = line.split()
            region_two_chr, region_two_start, region_two_end = [int(region_two[0]), int(region_two[1]), int(region_two[2])]


# with open(output_file_path, 'w') as output_file_path:
#     with open(sstats_file_path, 'r') as file:
#             for line in file:
#                 sstats_lines = line.split()
#                 chr_sstats_1, pos_sstats_1 = sstats_lines[0].split(':')
#                 chr_sstats_2, pos_sstats_2 = sstats_lines[1].split(':')
#                 if int(chr_sstats_1) == region_one_chr or int(chr_sstats_1) == region_two_chr:
#                         if int(chr_sstats_2) == region_one_chr or int(chr_sstats_2) == region_two_chr:
#                             if region_one_start >= int(pos_sstats_1) <= region_one_end or region_two_start >= int(pos_sstats_1) <= region_two_end:
#                                   if region_one_start >= int(pos_sstats_2) <= region_one_end or region_two_start >= int(pos_sstats_2) <= region_two_end:
#                                     output_file_path.write(line)

                          

# version 2  
with open(output_file_path, 'w') as output_file_path:
    with open(sstats_file_path, 'r') as file:
            for line in file:
                sstats_lines = line.split()
                chr_sstats_1, pos_sstats_1 = sstats_lines[0].split(':')
                chr_sstats_2, pos_sstats_2 = sstats_lines[1].split(':')
                if int(chr_sstats_1) == region_one_chr or int(chr_sstats_1) == region_two_chr:
                        if int(chr_sstats_2) == region_one_chr or int(chr_sstats_2) == region_two_chr:
                            if (region_one_start <= int(pos_sstats_1) <= region_one_end and region_two_start <= int(pos_sstats_2) <= region_two_end):
                                output_file_path.write(line)
                            elif (region_one_start <= int(pos_sstats_2) <= region_one_end and region_two_start <= int(pos_sstats_1) <= region_two_end):
                                 output_file_path.write(line)
                            else:
                                 pass
                        else:
                              pass
                else:
                      pass
                
