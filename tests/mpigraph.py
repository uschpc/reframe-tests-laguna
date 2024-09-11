import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Mpigraph(rfm.RunOnlyRegressionTest):
    descr = "mpiGraph benchmark using gcc/13.3.0 and openmpi/5.0.5 with pmix_v5"
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-mpigraph"
    ]
    sourcesdir = None
    executable = "mpiGraph 1048576 10 10"
    num_tasks = 8
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    time_limit = "5m"
    prerun_cmds = [
        "ulimit -s unlimited"
    ]
    env_vars = {
        "SLURM_MPI_TYPE": "pmix_v5"
    }
    reference = {
        "*": {
            "send_avg": (8800, -0.1, None, "msg_bandwidth"),
            "recv_avg": (9500, -0.1, None, "msg_bandwidth")
        }
    }

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"END mpiGraph", self.stdout)

    @performance_function("msg_bandwidth", perf_key = "send_avg")
    def extract_perf_send(self):
        return sn.extractsingle(r"Send avg\s+(?P<S_ret>[0-9]+\.[0-9]+)", self.stdout, "S_ret", float)

    @performance_function("msg_bandwidth", perf_key = "recv_avg")
    def extract_perf_recv(self):
        return sn.extractsingle(r"Recv avg\s+(?P<R_ret>[0-9]+\.[0-9]+)", self.stdout, "R_ret", float)
