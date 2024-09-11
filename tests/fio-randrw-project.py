import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class FioRandrwProject(rfm.RunOnlyRegressionTest):
    descr = "Fio random read/write benchmark for /project file system"
    tags = {
        "daily"
    }
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-fio"
    ]
    sourcesdir = "./src/fio-randrw"
    executable = "bash fio-randrw-project.sh"
    num_tasks = 1
    num_cpus_per_task = 8
    time_limit = "5m"
    reference = {
        "*": {
            "avg_write_speed": (185.0, -0.1, None, "MiB/sec"),
            "avg_read_speed": (185.0, -0.1, None, "MiB/sec")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"all jobs", self.stdout)

    @performance_function("MiB/sec", perf_key = "avg_write_speed")
    def extract_perf_write(self):
        return sn.extractsingle(r"WRITE:\sbw=(?P<W_ret>\d+.\d+)", self.stdout, "W_ret", float)

    @performance_function("MiB/sec", perf_key = "avg_read_speed")
    def extract_perf_read(self):
        return sn.extractsingle(r"READ:\sbw=(?P<R_ret>\d+.\d+)", self.stdout, "R_ret", float)
