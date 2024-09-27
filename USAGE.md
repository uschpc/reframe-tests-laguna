# Using ReFrame on the Laguna regional cluster

## Installing ReFrame

Currently, tests are developed and run using ReFrame v4.6.3. A shared install is available on CARC HPC clusters in `/project/jkhong_1307/rfm/reframe-4.6.3`.

The following steps were used to install ReFrame:

```
cd /project/jkhong_1307/rfm
module purge
module load gcc/13.3.0 python/3.11.9 curl tar gzip
curl -LO https://github.com/reframe-hpc/reframe/archive/refs/tags/v4.6.3.tar.gz
tar -xf v4.6.3.tar.gz
rm v4.6.3.tar.gz
cd reframe-4.6.3
./bootstrap.sh
py="$(type -p python3)"
sed -i "1s%.*%#\!${py}%" ./bin/reframe
unset py
module purge
cd ..
chmod -R ug-w reframe-4.6.3
./reframe-4.6.3/bin/reframe -V
```

## Installing the Laguna test suite

A shared install of the test suite is available on Laguna in `/project/jkhong_1307/rfm/reframe-tests-laguna`.

To install the CARC test suite, clone the repo:

```
git clone https://github.com/uschpc/reframe-tests-laguna
cd reframe-tests-laguna
```

## Listing and validating tests

To list and validate tests, use the `--list` option:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/ --list
```

The `-C` option specifies the path to a configuration file, and the `-c` option specifies the path to the test files.

## Running tests

The ReFrame tests can be run individually, as a subset, or as the entire suite. To run tests, use the `-r` option.

### Individual test

To run an individual test, use the path to the test file. For example:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/julia-pi.py -r
```

### Subset of tests

To run a subset of tests, use the `-n` option with grep-like syntax. For example:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/ -n 'Python|Julia' -r
```

### Tagged tests

To run tests with a specific tag, use the `-t` option and specify the tag value. For example:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/ -t daily -r
```

### Tests for specific partition

To run tests for a specific partition, use the `--system` option and specify the cluster and partition. For example:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/ --system=laguna:gpu -r
```

### Tests for every node in specific partition

To run tests for every node in a specific partition, use the `--system` and `--distribute` options. For example:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/julia-pi.py --system=laguna:compute --distribute=all -r
```

### Entire test suite

To run the entire suite of tests, use the path to the tests directory:

```
cd /project/jkhong_1307/rfm
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/ -r
```

### Reservations

A reservation may be required to run tests, like during maintenance periods.

First, find the reservation name to use:

```
scontrol show reservation
```

Then, specify the reservation name using the `SBATCH_RESERVATION` environment variable. For example:

```
export SBATCH_RESERVATION=res_12345
```

The variable will then be exported to the ReFrame Slurm jobs and allow them to run.

## Checking test logs

Various log files can be found in `/project/jkhong_1307/rfm/`.

## Reference guide for test suite

A reference guide for specific tests to run during testing or maintenance periods.

```
module purge
cd /project/jkhong_1307/rfm
export SBATCH_RESERVATION=<res>

# All tests
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/ -r

# Test every node using Julia test
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/julia-pi.py --distribute=all -r

# Test every node using file download test
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/file-download.py --distribute=all -r

# Test every node using Apptainer test
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/apptainer-hello.py --distribute=all -r

# Test GPU access for every node in gpu partition using Apptainer test
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/apptainer-gpu-hello.py --distribute=all -r

# Test every node in compute and gpu partitions using STREAM test
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/stream-compute.py --distribute=all -r
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/stream-gpu.py --distribute=all -r

# Test every node in compute and gpu partitions using HPCG test
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/hpcg-compute.py -r
./reframe-4.6.3/bin/reframe -C ./reframe-tests-laguna/config/laguna.py -c ./reframe-tests-laguna/tests/hpcg-gpu.py -r
```
