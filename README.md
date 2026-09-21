# Python Scripts used in Investigating the impact of Social Media to the Quality of Life of its Users 🤖 📈

## Overview

- This repository contains the python scripts used for the statistical analysis of the master's thesis. The repository contains two parts:

- the statistical analysis scripts that provided the published results
- the scripts used to further extend the statistical analysis beyond the scope of the thesis (for purposes of analyzing the collected data).

## 📃 Project Structure

- ### The core scripts exist in the app subfolder and the data rest in the data subfolder.
- ### Below is an outline of the project's folder structure

```text
msc-analysis-full-scripts/
├── README.md
├── LICENSE.md
├── pyproject.toml
├── src/
├──── notebooks/
│       ├── thesis_notebook.ipynb         <-- the notebook using the core thesis findings scripts
│       ├── thesis_notebook_extras.ipynb  <-- the notebook with scripts that are used 
|                                             to further analyze the data and fit more methods and models
├──── scripts/
│       └── analysis_of_variance/
│       └── data/
│           ├── encoded_data.xlsx         <-- the .xlsx file containing sheets with the encoded data
|       └── descriptive_statistics/
│       └── distribution_finders/
│       └── non_parametric_statistics/
|       └── parametric_tests/
│       └── plotcode/
│       └── regressions/
│   
└── utilities/
|   └── copy_recursively.ps1
|   └── copy_recursively.sh
|   └── install_dependencies_python.ps1
|   └── install_dependencies_python.sh  
|
└── @msc-thesis-repository/
    └── symlink to the thesis repository containing the LaTeX code for the publication PDF
```

## 🚀🚀🚀 Deployment

- ### 🔗 To run the scripts or the jupyter notebooks you must have Python 3.12 or above installed. Clone the repository and then create a virtual environment to install the dependencies with the following commands.

```text
    https://github.com/indecisive-kraken/msc-thesis-analysis-full
  
    # Windows (you can use forward slashes too, but for demonstration purposes backslashes are used)
    python3 -m venv .\msc-analysis-full-scripts
    .\bin\activate
  
    # Unix-Based
    python3 -m venv msc-analysis-full-scripts/
    source ./bin/activate
```

- ### Or you can run the provided scripts in the utilities folder. After that you can run any script you like by navigating to its folder.
- ### 📜 After that, the most straightforward way to get the results is to run the code in the individual cells of the jupyter notebooks
- ### For individual scripts open a terminal/console and use the command outlined below:

```text
    python3 -m filename.py
```

## 🔑 LICENSE

## 🔐 Data Access

- ### The repository contains an excel file with the encoded representations of the collected data in Likert Scales and Dummy Variable Encoding . If you want to get access to the complete version of the file with all the collected descriptions etc don't hesitate to contact me.
