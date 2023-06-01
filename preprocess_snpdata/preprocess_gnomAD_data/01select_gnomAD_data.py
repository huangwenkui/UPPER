import vcf
import sys
import os

pathogenicity_attrs = ['Likely_pathogenic', 'Likely_benign', 'Pathogenic', 'Benign']
ReviewStatus_attrs = [['criteria_provided', '_multiple_submitters', '_no_conflicts'], ['reviewed_by_expert_panel'], ['criteria_provided','_single_submitter']]
vcf_filename = sys.argv[1:][0]

vcf_outfilename = "./gnomAD/ExAC_selected.vcf"
vcf_reader = vcf.Reader(open(vcf_filename, 'r'))
vcf_writer = vcf.Writer(open(vcf_outfilename,'w'),vcf_reader)

#{'AC_FIN': [0], 'AN_FEMALE': '2914', 'K3_RUN': ['GAA:0'], 'BaseQRankSum': 0.727,
# 'GQ_HIST': ['1012|14971|172|100|3161|259|127|30|8|9|5|16|1162|274|59|45|17|2|3|3', '0|0|0|0|0|1|0|0|0|0|0|0|0|1|0|0|0|0|0|0'],
# 'Hom_AMR': [0], 'Hom_EAS': [0], 'K1_RUN': ['G:0'], 'Het_SAS': [0], 'Hom_SAS': [1], 'ESP_AF_POPMAX': ['0'], 'FS': 0.0,
# 'AC_SAS': [2], 'Het_OTH': [0], 'K2_RUN': ['GA:0'], 'Hom_FIN': [0], 'AC_Hom': [1],
# 'DP_HIST': ['14728|2455|2120|518|121|499|534|314|111|21|10|2|2|0|0|0|0|0|0|0', '1|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0'],
# 'DP': 139843, 'AC_AMR': [0], 'AC_AFR': [0], 'AN_POPMAX': ['5052'], 'Hom_OTH': [0], 'AC_OTH': [0], 'AN_EAS': 254, 'AN_OTH': 90,
# 'culprit': 'MQ', 'POPMAX': ['SAS'], 'AN_Adj': 8432, 'AN_AMR': 134, 'Het_AFR': [0], 'AN_CONSANGUINEOUS': '926', 'ReadPosRankSum': 0.727,
# 'AC_Adj': [2], 'ClippingRankSum': 1.15, 'NCC': 60853, 'AN_FIN': 16, 'AC': [3], 'MQRankSum': 0.727, 'AN_SAS': 5052,
# 'Het_FIN': [0], 'AF': [6.998e-05], 'VQSLOD': -1.687, 'AC_POPMAX': ['2'], 'AC_EAS': [0], 'AN': 42870, 'AN_MALE': '5518', 'MQ0': 0,
# 'AGE_HISTOGRAM_HOM': ['0|0|0|0|0|0|1|0|0|0|0|0'], 'GQ_MEAN': 12.48, 'Het_AMR': [0], 'HOM_CONSANGUINEOUS': ['0'],
# 'CSQ': ['C|downstream_gene_variant|MODIFIER|WASH7P|ENSG00000227232|Transcript|ENST00000423562|unprocessed_pseudogene||||||||||rs752859895|1|991|-1||SNV|1|HGNC|38034|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|downstream_gene_variant|MODIFIER|WASH7P|ENSG00000227232|Transcript|ENST00000438504|unprocessed_pseudogene||||||||||rs752859895|1|991|-1||SNV|1|HGNC|38034|YES||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|splice_region_variant&non_coding_transcript_exon_variant&non_coding_transcript_variant|LOW|DDX11L1|ENSG00000223972|Transcript|ENST00000450305|transcribed_unprocessed_pseudogene|5/6||ENST00000450305.2:n.412G>C||412|||||rs752859895|1||1||SNV|1|HGNC|37102|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|non_coding_transcript_exon_variant&non_coding_transcript_variant|MODIFIER|DDX11L1|ENSG00000223972|Transcript|ENST00000456328|processed_transcript|3/3||ENST00000456328.2:n.620G>C||620|||||rs752859895|1||1||SNV|1|HGNC|37102|YES||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|downstream_gene_variant|MODIFIER|WASH7P|ENSG00000227232|Transcript|ENST00000488147|unprocessed_pseudogene||||||||||rs752859895|1|1032|-1||SNV|1|HGNC|38034|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|non_coding_transcript_exon_variant&non_coding_transcript_variant|MODIFIER|DDX11L1|ENSG00000223972|Transcript|ENST00000515242|transcribed_unprocessed_pseudogene|3/3||ENST00000515242.2:n.613G>C||613|||||rs752859895|1||1||SNV|1|HGNC|37102|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|intron_variant&non_coding_transcript_variant|MODIFIER|DDX11L1|ENSG00000223972|Transcript|ENST00000518655|transcribed_unprocessed_pseudogene||2/3|ENST00000518655.2:n.482-31G>C|||||||rs752859895|1||1||SNV|1|HGNC|37102|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|downstream_gene_variant|MODIFIER|WASH7P|ENSG00000227232|Transcript|ENST00000538476|unprocessed_pseudogene||||||||||rs752859895|1|1039|-1||SNV|1|HGNC|38034|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|downstream_gene_variant|MODIFIER|WASH7P|ENSG00000227232|Transcript|ENST00000541675|unprocessed_pseudogene||||||||||rs752859895|1|991|-1||SNV|1|HGNC|38034|||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.', 'C|regulatory_region_variant|MODIFIER|||RegulatoryFeature|ENSR00001576075|CTCF_binding_site||||||||||rs752859895|1||||SNV|1|||||||||||||||||C:0.0003959||||||||C:0|C:6.998e-05|C:0|C:0.0002372|C:0|C:0|C:0|C:0|||||||||||||GGA|.'],
# 'KG_AF_GLOBAL': ['0'], 'AN_NFE': 2116, 'ESP_AF_GLOBAL': ['0'], 'AGE_HISTOGRAM_HET': ['0|0|0|0|0|0|1|0|0|0|0|0'], 'AC_FEMALE': ['0'], 'AN_AFR': 770, 'Het_NFE': [0], 'InbreedingCoeff': -0.0844, 'DOUBLETON_DIST': [None], 'Het_EAS': [0], 'KG_AF_POPMAX': ['0'], 'ESP_AC': ['0'], 'GQ_STDDEV': 15.18, 'AC_CONSANGUINEOUS': ['0'], 'Hom_NFE': [0], 'MQ': 35.72, 'QD': 23.42, 'AC_MALE': ['2'], 'KG_AC': ['0'], 'Hom_AFR': [0], 'AC_Het': [0], 'AC_NFE': [0]}


count = 0
for record in vcf_reader:
     AF = record.INFO['AF']
     if len(AF)==1:
         if AF[0]>=0.01:
             vcf_writer.write_record(record)
             count += 1
print(count)
