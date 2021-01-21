# How to Automatic Testing with GitHub Actions

- This repo is used for BU EC500 A2(2021 Spring)

## Create a new repository on GitHub

- Select a different repository name than your colleagues (otherwise forking the same name will be strange)

- Before you create the repository, select “Initialize this repository with a README”

- Also, you can choose to add .gitignore or license for you repo

## Clone your own repository, add code, commit, and push

- Clone this repository, or add a file ```example.py``` like following:

```
import numpy as np
# ============================================================
# Defining your own functions here
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ============================================================
# Defining your own testing here
# ============================================================

def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'


def test_subtract():
    assert subtract(2, 3) == -1
```

(Optional) If you want to upload a file from your PC to GitHub, there are two methods:

- Click the ```Add file - Upload files``` in your GitHub repo, then drop files here

- Clone repo to local and push to GitHub

```
# Clone this repo to my MAC Destop
cd Destop
git clone https://github.com/zhangyanyu0722/Github_Action_Test.git

# Make some change to the files that in this folder

# Select all files under the current directory
cd Github_Action_Test
git add .

# Add some commits
git commit -m "add something here"

# Push to GitHub
git push -u origin main
```

## Enable GitHub Actions

- Select ```Actions``` from your GitHub repository page. You get to a page ```Get started with GitHub Actions```. Select the button for ```Set up this workflow``` under ```Python package``` or ```Python Application```

- GitHub creates the following file for you in the subfolder .github/workflows. Add ```pytest example.py``` to the last line

## Verify that tests have been automatically run

- Observe in the repository how the test succeeds. While the test is executing, the repository has yellow marker. This is replaced with a green check mark, once the test succeeds




