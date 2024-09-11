import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class RBootstrap(rfm.RunOnlyRegressionTest):
    descr = "Bootstrapping a GLM in parallel using R"
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-r"
    ]
    sourcesdir = "./src/r-bootstrap"
    executable = "Rscript bootstrap.R"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    env_vars = {
        "OMP_NUM_THREADS": "1"
    }
    reference = {
        "*": {
            "elapsed_time": (62.8, None, 0.1, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Elapsed time", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
