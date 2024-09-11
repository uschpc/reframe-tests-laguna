import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class MatrixOpenMPI(rfm.RegressionTest):
    descr = "Matrix-vector multiplication example using gcc/13.3.0 and openmpi/5.0.5 with pmix_v5"
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0-openmpi-5.0.5"
    ]
    sourcesdir = "./src/matrix-mpi"
    sourcepath = "matrix-vector-multiplication-mpi-openmp.c"
    executable_opts = [
        "4200",
        "10000"
    ]
    build_system = "SingleSource"
    num_tasks = 4
    num_tasks_per_node = 2
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "ulimit -s unlimited"
    ]
    env_vars = {
        "OMP_NUM_THREADS": "1",
        "SLURM_MPI_TYPE": "pmix_v5"
    }
    reference = {
        "*": {
            "elapsed_time": (1.4, None, 0.25, "seconds")
        }
    }

    @run_before("compile")
    def set_compiler_flags(self):
        self.build_system.cflags = [
            "-march=native",
            "-fopenmp"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"time for single matrix vector multiplication", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"multiplication\s(?P<time_ret>[0-9]+.[0-9]+)", self.stdout, "time_ret", float)
