# ReFrame test suite for Laguna regional cluster

## Purpose

The CARC [ReFrame](https://reframe-hpc.readthedocs.io/en/stable/index.html) system regression tests for the Laguna regional cluster are designed to be short-running and to cover broad functionality. The tests include:

- Lmod software modules
- Programming environments (e.g., compilers, toolchains, MPI libraries)
- Parallel programming (e.g., OpenMP, MPI, CUDA)
- Popular applications (e.g., Python, R, Julia)
- I/O on the /home1 and /project file systems
- File downloads
- Containers
- Single-node and multi-node jobs

Currently, tests are developed and run using ReFrame v4.6.2.

## License

[0BSD](LICENSE)
