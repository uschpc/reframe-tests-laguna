import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class STREAMGpu(rfm.RunOnlyRegressionTest):
    descr = "STREAM benchmark for gpu partition nodes"
    valid_systems = [
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-gcc-13.3.0"
    ]
    sourcesdir = None
    executable = "/project/jkhong_1307/rfm/resources/STREAM/stream_c.exe"
    num_tasks = 1
    num_cpus_per_task = 64
    time_limit = "5m"
    env_vars = {
        "OMP_SCHEDULE": "static",
        "OMP_DYNAMIC": "false",
        "OMP_STACKSIZE": "256M",
        "OMP_PROC_BIND": "true",
        "OMP_PLACES": "cores",
        "OMP_NUM_THREADS": "64"
    }
    reference = {
        "*": {
            "copy_best": (703000, -0.1, None, "MB/s"),
            "scale_best": (472000, -0.1, None, "MB/s"),
            "add_best": (527000, -0.1, None, "MB/s"),
            "triad_best": (528000, -0.1, None, "MB/s")
        }
    }

    @run_before("run")
    def set_job_options(self):
        self.job.options += [
            "--mem=0"
        ]

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Solution Validates", self.stdout)

    @performance_function("MB/s", perf_key = "copy_best")
    def extract_perf_copy(self):
        return sn.extractsingle(r"Copy:\s+(?P<copy_ret>[0-9]+\.[0-9]+)", self.stdout, "copy_ret", float)

    @performance_function("MB/s", perf_key = "scale_best")
    def extract_perf_scale(self):
        return sn.extractsingle(r"Scale:\s+(?P<scale_ret>[0-9]+\.[0-9]+)", self.stdout, "scale_ret", float)

    @performance_function("MB/s", perf_key = "add_best")
    def extract_perf_add(self):
        return sn.extractsingle(r"Add:\s+(?P<add_ret>[0-9]+\.[0-9]+)", self.stdout, "add_ret", float)

    @performance_function("MB/s", perf_key = "triad_best")
    def extract_perf_triad(self):
        return sn.extractsingle(r"Triad:\s+(?P<triad_ret>[0-9]+\.[0-9]+)", self.stdout, "triad_ret", float)
