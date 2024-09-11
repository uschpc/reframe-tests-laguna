import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class ContainerHello(rfm.RunOnlyRegressionTest):
    descr = "Container hello world"
    valid_systems = [
        "laguna:gpu"
    ]
    valid_prog_environs = [
        "env-apptainer"
    ]
    sourcesdir = None
    executable = "apptainer exec /apps/containers/ood/desktop/rocky8-xfce-desktop-ood3.sif echo \"Hello world\""
    num_tasks = 1
    num_cpus_per_task = 1
    time_limit = "5m"

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r"Hello world", self.stdout)
