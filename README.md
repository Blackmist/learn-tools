![tools](media/toolbox.png) 
# learn-tools

Some handy scripts for working with markdown articles on learn.microsoft.com


##  ![Python](media/python-logo.png) Python scripts:

* [fix-nb.py](fix-nb.py) - Change notebook links and images to markdown syntax.
* [move-to-v1.py](move-to-v1.py) - Fix links in a file that you're going to move to the v1 folder.
* [create-codeowners.py](create-codeowners.py) - create a CODEOWNERS file for the azureml-examples repo.  Add/replace the lines in https://github.com/Azure/azureml-examples/blob/main/.github/CODEOWNERS with contents of this new file.
* [find-sippets.py](find-snippets.py) - Useful for reviewing and summarizing the snippets. Reads through your local repo to find instances of code snippets pulled from azureml-examples. Creates a csv file with the following columns:

    * **from_file** - the file in the docs repo that contains the snippet
    * **match** - the full text of the snippet being pulled
    * **branch** - the branch of azureml-examples that the snippet is from, using the path_to_root specified in 
    .openpublishing.publish.config.json in our repo
    * **path** - path to the file in azureml-examples
    * **ref_file** - the file where the code is located
    * **notebook_cell** - if a cell in a notebook, this is the name of the cell.  Otherwise, blank.



## Other repos

Also see these repos for other handy tools:

* ![Python](media/python-logo.png) (Python) [Search images](https://github.com/sdgilley/search-images) - find text inside images 
* ![R](media/r-logo.png) (R) [toc-to-csv](https://github.com/sdgilley/toc-to-csv) - convert a markdown table of contents to a csv file 
*  ![R](media/r-logo.png) (R) [MonthlyReport](https://github.com/sdgilley/MonthlyReport) - Summarizes file modification from git logs 