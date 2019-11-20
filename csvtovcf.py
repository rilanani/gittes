#! /usr/bin/env python
import os
import sys
import csv
import json
import subprocess

def convert_to_vcf(input_file, input_file_format):
    FN = input_file_format['name']-1 if 'name' in input_file_format else None
    MIS = input_file_format['mis']-1 if 'mis' in input_file_format else None
    BRANCH = input_file_format['branch']-1 if 'branch' in input_file_format else None
    TEL = input_file_format['tel']-1 if 'tel' in input_file_format else None
    BDAY = input_file_format['bday']-1 if 'bday' in input_file_format else None
    EMAIL = input_file_format['email']-1 if 'email' in input_file_format else None
    CGPA = input_file_format['cgpa']-1 if 'cgpa' in input_file_format else None
    
    
    with open( input_file, 'r' ) as source_file:
            reader = csv.reader( source_file )
            vcf_file = open('students.vcf', 'w+')
            for row in reader:
            
                FN_VAL = row[FN] if FN is not None else ''
                MIS_VAL = row[MIS] if MIS is not None else ''
                BRANCH_VAL = row[BRANCH] if BRANCH is not None else ''
                TEL_VAL = row[TEL] if TEL is not None else ''
                BDAY_VAL = row[BDAY] if BDAY is not None else ''
                EMAIL_VAL = row[EMAIL] if EMAIL is not None else ''
                CGPA_VAL = row[CGPA] if CGPA is not None else ''
                
                vcf_file.write( 'BEGIN:VCARD' + "\n")
                vcf_file.write( 'VERSION:3.0' + "\n")
                vcf_file.write( 'Name:' + FN_VAL + "\n")
                vcf_file.write( 'TEL:' + TEL_VAL + "\n")
                vcf_file.write( 'EMAIL:' + EMAIL_VAL + "\n")
                vcf_file.write( 'BDAY:' + BDAY_VAL + "\n")
                vcf_file.write( 'MIS:' + MIS_VAL + "\n")
                vcf_file.write( 'BRANCH:' + BRANCH_VAL + "\n")
                vcf_file.write( 'CGPA:' + CGPA_VAL + "\n")
                vcf_file.write( 'END:VCARD' + "\n")
                vcf_file.write( "\n")

            vcf_file.close()
      
        
def main(args):
        args_len = len(args)
        if args_len != 3 :
                print ( "wrong argument")
                sys.exit()
        
        elif args_len == 3 :
                input_file = args[1]
                input_file_format = json.loads(args[2])
               
        
        
        subprocess.call(['./test.sh',args[1]])
       
        convert_to_vcf(input_file,input_file_format)
if __name__ == '__main__':
        main(sys.argv)
