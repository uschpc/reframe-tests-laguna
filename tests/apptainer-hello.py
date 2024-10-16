import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class ApptainerHello(rfm.RunOnlyRegressionTest):
    descr = "Apptainer hello world"
    valid_systems = [
        "laguna:compute",
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = "./src/apptainer-hello"
    executable = "bash build-and-run.sh"
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Hello world", self.stdout)
