#!/usr/bin/env bash

# Run fio randrw test and remove test files
# For /project file system

set -e

cd /project/jkhong_1307/rfm/tmp

fio --name=fio-randrw-"$SLURM_JOB_ID" --ioengine=posixaio --rw=randrw --bs=64K --size=16G --numjobs=8 --iodepth=64 --direct=1 --runtime=60 --time_based --end_fsync=1

rm fio-randrw-"$SLURM_JOB_ID"*
