import vcf
import sys
import os

pathogenicity_attrs = ['Likely_pathogenic', 'Likely_benign', 'Pathogenic', 'Benign', 'Pathogenic/Likely_pathogenic','Benign/Likely_benign']
ReviewStatus_attrs = [['criteria_provided', '_multiple_submitters', '_no_conflicts'], ['reviewed_by_expert_panel'], ['criteria_provided','_single_submitter']]
vcf_filename = sys.argv[1:][0]
mode = sys.argv[1:][1]
path, basename = os.path.split(vcf_filename)
name, fextension = os.path.splitext(basename)
vcf_outfilename = path + "/" +name + "_selected" + fextension
if mode =="Deletion":
    vcf_outfilename = path + "/" + name + "_deletion" + fextension
vcf_reader = vcf.Reader(open(vcf_filename, 'r'))
vcf_writer = vcf.Writer(open(vcf_outfilename,'w'),vcf_reader)
# Record(CHROM=1, POS=69134, REF=A, ALT=[G])
# Record.INFO{'CLNREVSTAT': ['criteria_provided', '_single_submitter'],
# 'ORIGIN': ['1'], 'MC': ['SO:0001583|missense_variant'],
# 'CLNSIG': ['Likely_benign'], 'GENEINFO': 'OR4F5:79501', 'ALLELEID': 2193183,
# 'CLNVC': 'single_nucleotide_variant', 'CLNHGVS': ['NC_000001.10:g.69134A>G'],
# 'CLNDISDB': ['MeSH:D030342', 'MedGen:C0950123'],
# 'CLNVCSO': 'SO:0001483', 'CLNDN': ['Inborn_genetic_diseases']}
# print record.INFO['CLNSIG']
count = 0
for record in vcf_reader:
    if mode =="missense":
        if record.INFO['CLNVC'] == 'single_nucleotide_variant':
            try:
                if record.INFO['CLNSIG'][0] in pathogenicity_attrs:
                    if record.INFO['CLNREVSTAT'] in ReviewStatus_attrs:
                        vcf_writer.write_record(record)
                        count+=1
            except:
                continue
    elif mode=="Deletion":
        if record.INFO['CLNVC'] == 'Deletion':
            try:
                if record.INFO['CLNSIG'][0] in pathogenicity_attrs:
                    if record.INFO['CLNREVSTAT'] in ReviewStatus_attrs:
                        vcf_writer.write_record(record)
                        count+=1
            except:
                continue
print(count)
