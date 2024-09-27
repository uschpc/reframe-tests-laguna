#!/usr/bin/env bash

apptainer build --fakeroot debian-"$SLURM_JOB_ID".sif debian.def
apptainer exec debian-"$SLURM_JOB_ID".sif echo "Hello world"
rm debian-"$SLURM_JOB_ID".sif
