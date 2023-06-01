import sys

filename = sys.argv[1:][0]

if filename == "./LOF_GOF/goflof_HGMD2019.csv":
    out_filename = "./LOF_GOF/Classify_GOF_LOF_getdata.csv"

vepout_file = "./LOF_GOF/goflof_HGMD2019_vepout.csv"

out_fp = open(out_filename, "w")
vep_fp = open(vepout_file, "r")
vep_head = next(vep_fp)
vep_head_arr = vep_head.strip().split(",")
vep_head_mapping = {el: i for i, el in enumerate(vep_head_arr)}
head_Flag = True
for vep_line in vep_fp:

    vep_arr = vep_line.strip().split(",")
    id = vep_arr[vep_head_mapping["id"]]

    fp = open(filename, 'r')
    head = next(fp)
    head_arr = head.strip().split(",")
    head_mapping = {el.strip('"'): i for i, el in enumerate(head_arr)}
    for line in fp :
        arr = line.strip('"').split(",")
        HGVSc = arr[head_mapping["HGVSc"]].replace('"', '')
        if id == HGVSc:

            CHROM = vep_arr[vep_head_mapping["CHROM"]]
            Nuc_Pos = vep_arr[vep_head_mapping["Nuc-Pos"]]
            REF_Nuc = vep_arr[vep_head_mapping["REF-Nuc"]]
            ALT_Nuc = vep_arr[vep_head_mapping["ALT-Nuc"]]
            Consequence = vep_arr[vep_head_mapping["Consequence"]]
            IMPACT = vep_arr[vep_head_mapping["IMPACT"]]
            Ensembl_Gene = vep_arr[vep_head_mapping["Ensembl-Gene-ID"]]
            Ensembl_Protein = vep_arr[vep_head_mapping["Ensembl-Protein-ID"]]
            Ensembl_Transcript = vep_arr[vep_head_mapping["Ensembl-Transcript-ID"]]
            Uniprot_Accession = vep_arr[vep_head_mapping["Uniprot-Accession"]]
            ClinVar_preferred_disease_name_in_CLNDISDB = vep_arr[vep_head_mapping["ClinVar_preferred_disease_name_in_CLNDISDB"]]

            LOFGOF = arr[head_mapping["LABEL"]].replace('"','')
            cDNA_position = arr[head_mapping["cDNA_position"]].replace('"','')
            CDS_position = arr[head_mapping["CDS_position"]].replace('"','')
            Protein_position = arr[head_mapping["Protein_position"]].replace('"','')
            VARIANT_CLASS = arr[head_mapping["VARIANT_CLASS"]].replace('"','')
            Number_of_paralogs = arr[head_mapping["Number_of_paralogs"]].replace('"','')
            CDS_len = arr[head_mapping["CDS_len"]].replace('"','')
            Inheritance = arr[head_mapping["Inheritance"]].replace('"','')
            RSA_class = arr[head_mapping["RSA_class"]].replace('"','')
            Pfam_dom = arr[head_mapping["Pfam_dom"]].replace('"','')
            Amino_acids = arr[head_mapping["Amino_acids"]].replace('"','')
            DOMAINS_VEP = arr[head_mapping["DOMAINS_VEP"]].replace('"','')
            Clarks_distance = arr[head_mapping["Clarks_distance"]].replace('"','')
            if head_Flag:
                out_head = ["LOFGOF","CHROM","Nuc-Pos", "REF-Nuc", "ALT-Nuc", 'Consequence','IMPACT',"Ensembl-Gene-ID", "Ensembl-Protein-ID", "Ensembl-Transcript-ID", "Uniprot-Accession",
                        'ClinVar_preferred_disease_name_in_CLNDISDB', 'cDNA_position', 'CDS_position', 'Protein_position',
                        'VARIANT_CLASS', 'Number_of_paralogs', 'CDS_len', 'Inheritance', 'RSA_class', 'Pfam_dom', 'Amino_acids',
                        'DOMAINS_VEP', 'Clarks_distance']
                h = ",".join(out_head)
                out_fp.write(h)
                out_fp.write("\n")
                head_Flag = False
            out = [LOFGOF, CHROM,Nuc_Pos, REF_Nuc, ALT_Nuc, Consequence, IMPACT, Ensembl_Gene, Ensembl_Protein, Ensembl_Transcript,Uniprot_Accession,
                   ClinVar_preferred_disease_name_in_CLNDISDB,cDNA_position,CDS_position,Protein_position,
                   VARIANT_CLASS,Number_of_paralogs,CDS_len,Inheritance,RSA_class,Pfam_dom,Amino_acids,
                   DOMAINS_VEP,Clarks_distance]
            l = ",".join(out)
            out_fp.write(l)
            out_fp.write("\n")
            break
