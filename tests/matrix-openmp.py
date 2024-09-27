import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class MatrixOpenMP(rfm.RegressionTest):
    descr = "Matrix-vector multiplication example using OpenMP"
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0"
    ]
    build_locally = False
    sourcesdir = "./src/matrix-openmp"
    sourcepath = "matrix-vector-multiplication-openmp.c"
    executable_opts = [
        "4200",
        "10000"
    ]
    build_system = "SingleSource"
    num_tasks = 1
    num_cpus_per_task = 4
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "4"
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
