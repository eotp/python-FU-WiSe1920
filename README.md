# Main repository for the Python class at FU Berlin, summer term 2021

Dates, location and outline of the class are presented [here](https://www.fu-berlin.de/vv/de/lv/658261).
Starts at 13:30 to 17:00 CET

## Content

- 01 - 2021/04/23

  - Introduction into computational thinking
  - Programming languages and IDEs
  - Why Python?

- 02 - 2021/04/30

  - Python 101

- 03 - 2021/05/07

  - Python 101 continued
  - Plotting with Python

- 04 - 2021/05/14

  - Introduction to `pandas`
  - Simple data analysis using `pandas`

- 05 - 2021/05/21

  - Pandas recap
  - Simple data analysis using `pandas`

- 06 - 2020/05/28

  - Reporting using `jupyterbook`
  - Exploratory data analysis (EDA)
  - Study project - WW2

- 07 - 2021/06/04

  - Study project - WW2 (Group Session)

- 08 - 2021/06/11

  - Presentations study projects

- 09 - 2021/06/18

  - Object Oriented Programming (OOP)

- 10 - 2021/06/25
  
  - Interpolation and curve fitting
  - Inferential statistics
  - Population vs. sample statistics
  - Central Limit Theorem
  - Point and interval estimates (confidence intervals)
  - Hypothesis testing
  - Bootstrapping
  - Introduction to Machine Learning
  - Skipped:
    - Regression analysis
    - Logisitic regression
    - Hyperparamter tuning
    - Polynomial Regression

* 11 - 2021/07/02
  
  - `Spyder IDE`
  - Web scraping
  - Wordclouds

* 12 - 2021/07/09

  - Feedback round
  - Dashboarding with `streamlit`
  - Creating dynamic Maps with `folium` 
  
* 13 - 2021/xx/xx (optional lecture)

  - APIs (FastAPI)
  
---

In order to re-run the class materials I encourage you to use the [conda](https://conda.io/docs/) package manager. Once installed, create an environment and install all required dependencies on your machine by typing

`conda env create -f environment.yml`

into your console (_Windows users: please use the Anaconda Powershell Prompt_). You activate your new environment by typing

`conda activate fupy`

Then you are ready to go (if you are stuck check out the [conda documentation site](https://conda.io/docs/user-guide/tasks/manage-environments.html#)). Alternatively, you may launch [binder](https://mybinder.org/) to get a reproducible executable environment immediately in your browser. Simply click the _launch binder_ icon below.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/eotp/python-FU-class/master?urlpath=lab)

---

> We should mention that the conda environments created during this course will take up a lot of space!
> Feel free to run `conda env list` to display all created environments and delete them if you choose using `conda env remove -n env_name`.
> Remember that you can always recreate any of the environments using `conda env create -f environment.yml` in any given sub- or the root-directory of this repo. 
