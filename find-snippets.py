'''
This script reads through the files in your local repo and finds code snippets from azureml-examples
See readme for details of the columns in the output file.
'''

###################### INPUT HERE ############################
# Name the file and the path to your repo.
repo_path = 'c:\\GitPrivate\\azure-docs-pr\\articles\\machine-learning\\v1'
result_fn = "codeowners.txt"
############################ DONE ############################

# open the file to write the results to.
f = open(result_fn, 'w+')
# f.write("from_file, match, branch, path, ref_file, notebook_cell \n")

# iterate through the files in the folder.  
import os
import re
files = os.listdir(repo_path)
# find the file names from the directory.  
for file in files:
    if file.endswith('.md'):
        file_path = os.path.join(repo_path,file)
        # open the file and read through it line by line.
        with open(file_path, 'r') as target_file:
            try: # some of our files contain characters that cause errors.  skip them.
                for line in target_file.readlines():
                    # snippets have ~\azureml-examples in them.  Find all snippets and write them to the file.
                    match_snippet = re.findall(r'\(~\/azureml-examples[^)]*\)|source="~\/azureml-examples[^"]*"', line)
                    if match_snippet:
                        for match in match_snippet:
                            match= match.replace('(', '').replace(')', '').replace('"', '').replace(',', '').replace('source=', '')
                            # split up the match into parts here.
                            path = os.path.dirname(match)
                            ref_file = os.path.basename(match)
                            branch = path.split('/')[1]
                            path = path.replace('~', '').replace(branch,'')
                            if "?" in ref_file:
                                ref_file, name = ref_file.split('?',1)
                            else:
                                name = ''

                            # f.write(f"{file}, {match}, {branch}, {path}, {ref_file}, {name} \n")
                            f.write(f"{ref_file}, mldocs@microsoft.com \n")
            except: # record the files that wouldn't open
                f.write(f"{file}, error\n")
# close the csv file.
f.close()

# I usually open the .csv in Excel and create some pivot tables to summarize.  
