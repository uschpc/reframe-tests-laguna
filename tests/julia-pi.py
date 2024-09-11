import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class JuliaPi(rfm.RunOnlyRegressionTest):
    descr = "Estimating pi using Julia with multiple threads"
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-julia"
    ]
    sourcesdir = "./src/julia-pi"
    executable = "julia --threads 8 pi.jl"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "1m"
    reference = {
        "*": {
            "elapsed_time": (2.1, None, 0.1, "seconds")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"3.14", self.stdout)

    @performance_function("seconds", perf_key = "elapsed_time")
    def extract_perf(self):
        return sn.extractsingle(r"Elapsed time:\s(?P<elapsed_ret>[0-9]+.[0-9]+)", self.stdout, "elapsed_ret", float)
