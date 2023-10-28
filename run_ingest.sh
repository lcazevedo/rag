#!/bin/bash
# Submission script for HMEM
#SBATCH --job-name=ingest
#SBATCH --time=4-00:00:00 # days-hh:mm:ss
#
#SBATCH --ntasks=16
#SBATCH --mem=90GB
#SBATCH --partition=long
#
#SBATCH --comment=Doutorado
#
#SBATCH --output=logHPC_ingest.txt

python main.py ingest -v
