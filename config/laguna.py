# Laguna configuration

site_configuration = {
    "general": [
        {
            "check_search_path": [
                "tests/"
            ],
            "check_search_recursive": True,
            "purge_environment": True,
            "report_file": "/project/jkhong_1307/rfm/reports/laguna-run-report-$(date --iso-8601=seconds).json",
        }
    ],
    "systems": [
        {
            "name": "laguna",
            "descr": "Laguna regional cluster",
            "stagedir": "/project/jkhong_1307/rfm/stage/laguna-stage-$(date --iso-8601=seconds)",
            "outputdir": "/project/jkhong_1307/rfm/output/laguna-output-$(date --iso-8601=seconds)",
            "modules_system": "lmod",
            "hostnames": [
                "laguna1.carc.usc.edu"
            ],
            "partitions": [
                {
                    "name": "compute",
                    "descr": "Laguna compute partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=jkhong_1307",
                        "--partition=compute"
                    ],
                    "max_jobs": 100,
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-hpcg",
                        "env-mpigraph",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-curl",
                        "env-ior",
                        "env-fio"
                    ]
                },
                {
                    "name": "gpu",
                    "descr": "Laguna gpu partition",
                    "scheduler": "slurm",
                    "launcher": "srun",
                    "access": [
                        "--account=jkhong_1307",
                        "--partition=gpu"
                    ],
                    "max_jobs": 100,
                    "environs": [
                        "env-apptainer",
                        "env-gcc-13.3.0",
                        "env-gcc-13.3.0-cuda-12.4.0",
                        "env-gcc-13.3.0-openmpi-5.0.5",
                        "env-hpcg",
                        "env-mpigraph",
                        "env-julia",
                        "env-python",
                        "env-r",
                        "env-curl",
                        "env-ior",
                        "env-fio"
                    ]
                }
            ]
        }
    ],
    "environments": [
        {
             "name": "env-apptainer",
             "modules": [
                 "apptainer/1.3.3"
             ]
        },
        {
            "name": "env-gcc-13.3.0",
            "modules": [
                "gcc/13.3.0"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-cuda-12.4.0",
            "modules": [
                "gcc/13.3.0",
                "cuda/12.4.0"
            ],
            "cc": "gcc",
            "cxx": "g++",
            "ftn": "gfortran"
        },
        {
            "name": "env-gcc-13.3.0-openmpi-5.0.5",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5"
            ],
            "cc": "mpicc",
            "cxx": "mpic++",
            "ftn": "mpif90"
        },
        {
            "name": "env-hpcg",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "hpcg/3.1"
            ]
        },
        {
            "name": "env-mpigraph",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "mpigraph/main"
            ]
        },
        {
            "name": "env-ior",
            "modules": [
                "gcc/13.3.0",
                "openmpi/5.0.5",
                "ior/3.3.0"
            ]
        },
        {
            "name": "env-fio",
            "modules": [
                "gcc/13.3.0",
                "fio/3.37"
            ]
        },
        {
            "name": "env-julia",
            "modules": [
                "julia/1.10.5"
            ]
        },
        {
            "name": "env-python",
            "modules": [
                "gcc/13.3.0",
                "python/3.11.9"
            ]
        },
        {
            "name": "env-r",
            "modules": [
                "gcc/13.3.0",
                "openblas/0.3.28",
                "r/4.4.1"
            ]
        },
        {
            "name": "env-curl",
            "modules": [
                "gcc/13.3.0",
                "curl/8.8.0"
            ]
        }
    ],
    "logging": [
        {
            "handlers": [
                {
                    "type": "file",
                    "level": "debug",
                    "name": "./logs/reframe-laguna.log",
                    "timestamp": "%FT%T",
                    "format": "[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s",
                    "append": True
                }
            ],
            "handlers_perflog": [
                {
                    "type": "filelog",
                    "level": "info",
                    "basedir": "./perflogs",
                    "prefix": "%(check_system)s/%(check_partition)s",
                    "format": (
                        "%(check_job_completion_time)s,%(version)s,"
                        "%(check_display_name)s,%(check_system)s,"
                        "%(check_partition)s,%(check_environ)s,"
                        "%(check_jobid)s,%(check_result)s,%(check_perfvalues)s"
                    ),
                    "format_perfvars": (
                        "%(check_perf_value)s,%(check_perf_unit)s,"
                        "%(check_perf_ref)s,%(check_perf_lower_thres)s,"
                        "%(check_perf_upper_thres)s,"
                    ),
                    "datefmt": "%FT%T",
                    "append": True
                }
            ]
        }
    ]
}
