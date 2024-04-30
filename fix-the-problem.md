# Fix the problem 

When the pr-report shows a problem in a PR, you need to fix the problem before you can approve the PR.

The problems that will break our build are:

* A file that we reference is being deleted.
* An id or notebook cell name is being deleted.

Before the PR can be approved, we need to make sure that the docs that reference these files or ids are updated.  The PR report gives the name of the referencing file(s) that need to be fixed.

## No fix necessary

In some cases, the name of the notebook cell or id that was deleted is not actually used in the referencing file.  In that case, you can approve the PR without making any changes.  

### Example

You'll see the following output from `python GitHub/pr-report.py 2779`:

```
MODIFIED FILES: 4
Modified File: sdk/python/endpoints/batch/deploy-pipelines/hello-batch/sdk-deploy-and-test.ipynb 
  Referenced in:
   https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-use-batch-pipeline-deployments.md
   Notebook cells deleted: 1
   * previews
*azureml-examples temp-fix branch has the same version of this file as main

Fix these references in our docs before approving this PR.

Modified File: sdk/python/endpoints/batch/deploy-pipelines/training-with-components/sdk-deploy-and-test.ipynb 
  Referenced in:
   https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-use-batch-training-pipeline.md
   Notebook cells deleted: 1
   * python38-azureml
*azureml-examples temp-fix branch has the same version of this file as main

Fix these references in our docs before approving this PR.
```

But when you go to https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-use-batch-pipeline-deployments.md, you won't find the cell name "previews" referenced anywhere in the document. So there's nothing to fix here.

Likewise, when you go to https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-use-batch-training-pipeline.md, you won't find a reference to a cell named "python38-azureml".  So again, there is nothing to fix here.

## Quick fix in azure-docs-pr

If you can quickly fix the reference in azure-docs-pr, do so.  For example, if the reference is no longer necessary, remove it.  Or perhaps if it is a single line of code, replace the reference with the hard-coded line.  (Don't do this for anything longer than one or two lines, though.)

* Create a PR in azure-docs-pr to apply this fix.  
* After your azure-docs-pr PR with the fix is merged, you can approve the azureml-examples PR.

## Move to a temporary branch

If you can't do a quick fix, follow this process:

1. If temp-fix has the same version of the file, skip 2 and proceed to #3.
1. If temp-fix does not have the same version of the file, use the steps below to first [update the temp-fix branch](#temp-fix) in azureml-examples.
1. <a name="three"></a> Create a PR in azure-docs-pr to use **~/azureml-examples-temp-fix** instead of **~/azureml-examples-main** for the reference(s) to the problem file/id(s).
1. Once your PR in azure-docs-pr is merged to main, you can approve the azureml-examples PR.
   > NOTE FOR RELEASE BRANCHES: During Build or Ignite, when there are release branches, this process is more complex. All those release branches also need your update.  Coordinate with the Build/Ignite roadshow owner before you approve the PR.  They'll need to sync main into the release branches before you can approve the original azureml-examples PR.
1. Create a work item to update these articles to again use ~/azureml-examples-main after the azureml-examples PR has merged.  We want to minimize the time that an article references a file on the temp-fix branch.
### Example

You'll see the following output from `python GitHub/pr-report.py 2888`:

```
MODIFIED FILES: 1
Modified File: cli/setup.sh 
  Referenced in:
   https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-deploy-automl-endpoint.md
   https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-configure-cli.md
   Code cells deleted: 2
   * # <az_configure_defaults>
   * # </az_configure_defaults>
*azureml-examples temp-fix branch has the same version of this file as main

Fix these references in our docs before approving this PR.
```

There are two docs that reference the file cli/setup.sh.  The ID `az_configure_defaults` is being deleted in the PR. 

My first question would to be ask the PR author why they are deleting this section.  Is it no longer necessary?  If so, delete the references to it in the docs as well, (https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-deploy-automl-endpoint.md & 
   https://github.com/MicrosoftDocs/azure-docs-pr/edit/main/articles/machine-learning/how-to-configure-cli.md)

If it was a mistake (they didn't think the comments mattered and just deleted them), ask them to put the comments back.

If the rename was for some good reason (the old name was confusing, perhaps), the temp-fix branch contains the same version of the file as main.  So you can switch the references in the docs to point to the temp-fix branch (instead of main) for this particular id.  That is, change:

:::code language="azurecli" source="~/azureml-examples-**main**/cli/setup.sh" id="az_configure_defaults":::

to:

:::code language="azurecli" source="~/azureml-examples-**temp-fix**/cli/setup.sh" id="az_configure_defaults":::

Once your change has merged to main in azure-docs-pr, you can approve the PR in azureml-examples.

Once the azureml-examples change has merged, you can go back to the docs and update the references to point back to main.  This is a temporary fix, so we want to minimize the time that the docs reference the temp-fix branch.

## <a href="temp-fix"></a> Update the temp-fix branch

Check to see if the temp-fix branch is currently in use in azure-docs-pr before you update it.  Run `python GitHub/find-snippet.py` to see if the temp-fix is one of the active branches.

* If temp-fix is NOT an active branch.
    
    You just need to update the files in the temp-fix branch to the latest versions from the main branch.  You can do this by pulling from upstream main.  This will update all the files in the temp-fix branch to the latest versions.

1. In azureml-docs - checkout the branch temp-fix.
1. Pull from upstream main.  
1. Commit changes in the branch.  For the commit message, use "Update from main".
1. Push your changes to upstream/temp-fix. 

* If temp-fix IS an active branch.  

    You don't want to mess with other referenced files that haven't been fixed yet, so you can't just pull all of upstream main. Instead, add just the main branch version of the files that are causing the problem to the temp-fix branch:
    
1. Checkout the **main** branch in azureml-examples.
1. COPY the file(s) from the main brnch that are causing you to reject the PR. Stash them somewhere on your computer outside the azureml-examples repo.
1. Checkout the **temp-fix** branch in azureml-examples
1. Paste those files from main back to the temp-fix branch.  At this point, the only changes in the temp-fix branch should be the files you just pasted in.
1. Commit in the changes to the temp-fix branch. For the commit message, reference the PR number that you are fixing.
1. Push your changes to upstream/temp-fix. This will update the files you want to reference in the temp-fix branch to their latest versions prior to the new PR.
1. Now proceed to [step 3 above](#three).
