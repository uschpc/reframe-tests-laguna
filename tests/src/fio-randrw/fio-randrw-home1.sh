#!/usr/bin/env bash

# Run fio randrw test and remove test files
# For /home1 file system

set -e

cd /home1/"$USER"

fio --name=fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=1G --numjobs=4 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1

rm fio-randrw-"$SLURM_JOB_ID"*
