# sandbox
Sandbox for debugging Snakemake workflows

## Mamba 

Conda and Mamba are tools that help you install and manage software packages and their dependencies, which are other packages that a software needs to function properly. They're especially useful when different projects need different versions of the same software package. Conda, created by Anaconda, Inc., is well-known for its ability to create isolated spaces (called environments) for your projects, ensuring that the software packages of one project don't interfere with those of another. Mamba is a faster version of Conda, doing the same job but more quickly. Both of them support many programming languages, making them versatile tools for managing software in your projects.

Install [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) in your home directory

## Snakemake 

Snakemake is a versatile, Python-based workflow management system that enables the creation of reproducible and scalable data analyses. It operates on the principle of defining "rules" that explicitly state how to produce output files from input files. These rules, which can incorporate shell commands or scripts in any language, are written in a Snakefile. Snakemake takes care of determining the correct order of rule execution based on their dependencies. It also supports parallelization of jobs, making it suitable for high-throughput computations. Furthermore, Snakemake workflows are self-documenting, meaning they can serve as a record of your data analysis, enhancing reproducibility. It's widely used in bioinformatics, but its application can extend to any field that involves pipeline-based data analysis.

Install [Snakemake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html#) using mamba

## sge-wynton profile
Clone the [sge-wynton profile](https://github.com/AndrewsLabUCSF/sge-wynton) into your home directory for cluster execution of workflows on wynton. 
