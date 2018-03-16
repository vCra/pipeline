from pipeline.jobs.job import Job
from pipeline.module import Module


class Flake8CIModule(Module):
    config = {
        "image": "eeacms/flake8",
    }

    class Flake8Job(Job):
        def post_run(self):
            print(self.container.logs)

    def __init__(self, *args, **kwargs):
        super(Flake8CIModule, self).__init__(*args, **kwargs)
        self.job_manager.job_class = self.Flake8Job

pipeline_ci_module = Flake8CIModule
