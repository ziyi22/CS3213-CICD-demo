# CS3213-CICD-demo
This repo is a demonstration of using GitHub Actions for CI/CD. Designed as part of NUS CS3213.

## Setup
Make a fork of this repo on GitHub into your own GitHub account. Enable GitHub Action on forked repo.
DO NOT fork it into the course GitHub organization as we already have one fork here.

## Demo: Hello World
`.github/workflows/main.yml` comes with a simple job `helloworld` that prints "Hello World".
Take a look at the file to understand how it is configured, then navigate to the `Actions` tab on GitHub webpage to see how it runs.

## Demo: Check Prefix
Uncomment the block for job `checkprefix` in `.github/workflows/main.yml`.
This job will check if the filename of all the `.py` files in the root directory begins with "CS3213".
Push the commit to GitHub, check the `Actions` tab to see that the job has failed (since `check_doc.py` violates this rule).

Rename `check_doc.py` to `CS3213_check_doc.py`. Push the change to GitHub, verify that the job now succeeds.

## Exercise: Check Documentation
Add a job in `.github/workflows/main.yml` to check if there is a file `Documentation.md` in the root directory and verify that the file is not empty.
A template has been provided to you in `.github/workflows/main.yml`.
The actual check logic is provided in `CS3213_check_doc.py` (previously `check_doc.py`), simply execute that in your workflow.

## A Real-World Example
Sadly, there is nothing for us to deploy, so there is no hands-on here. 
However, `.github/workflows/release.yml.txt` is a real world CD workflow from SQLancer which you can take a look at.

## Post Scriptum: Self-Hosted Runner
GitHub has a limited quota on GitHub Action runner time for private repos.
For CS3213, we work around this by using self-hosted runners served by our own servers.
To use these self-hosted runners, you can replace the `runs-on: ubuntu-latest` line with `runs-on: self-hosted` in your workflow YAML file.

Do notice that self-hosted runners are only available for private repositories in our course GitHub organization.
