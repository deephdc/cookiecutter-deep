{{cookiecutter.project_name}}
==============================

[![Build Status](https://jenkins.indigo-datacloud.eu/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/{{ cookiecutter.repo_name }}/master)](https://jenkins.indigo-datacloud.eu/job/Pipeline-as-code/job/DEEP-OC-org/job/{{ cookiecutter.repo_name }}/job/master)

{{cookiecutter.description}}

To launch it, first install the package then run [deepaas](https://github.com/indigo-dc/DEEPaaS):
```bash
git clone {{ cookiecutter.git_base_url }}/{{ cookiecutter.repo_name }}
cd {{ cookiecutter.repo_name }}
pip install -e .
deepaas-run --listen-ip 0.0.0.0
```
The associated Docker container for this module can be found in {{ cookiecutter.git_base_url }}/DEEP-OC-{{ cookiecutter.repo_name }}.

## Project structure
```
├── LICENSE
├── README.md              <- The top-level README for developers using this project.
├── data
│   └── raw                <- The original, immutable data dump.
│
├── docs                   <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                 <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials (if many user development), 
│                             and a short `_` delimited description, e.g.
│                             `1.0-jqp-initial_data_exploration.ipynb`.
│
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                             generated with `pip freeze > requirements.txt`
├── test-requirements.txt  <- The requirements file for the test environment
│
├── setup.py               <- makes project pip installable (pip install -e .) so {{cookiecutter.repo_name}} can be imported
├── {{cookiecutter.repo_name}}    <- Source code for use in this project.
│   ├── __init__.py        <- Makes {{cookiecutter.repo_name}} a Python module
│   │
│   ├── dataset            <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features           <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models             <- Scripts to train models and make predictions
│   │   └── deep_api.py    <- Main script for the integration with DEEP API
│   │
│   ├── tests              <- Scripts to perfrom code testing
│   │
│   └── visualization      <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini                <- tox file with settings for running tox; see tox.testrun.org
```
