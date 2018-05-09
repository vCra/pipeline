from pprint import pprint
from threading import Thread

from pipeline.jobs.job_status import JobStatus


class Job(Thread):
    config = None
    client = None
    status = JobStatus.NotStarted
    container = None

    def __init__(self, config, client):
        """
        A job that will get run
        :param config: A config object that stores the configuration for the docker run command
        :param client: A docker client
        """
        self.config = config
        self.client = client
        super(Job, self).__init__()

    def pre_run(self):
        pass

    def post_run(self):
        pass

    def on_error(self):
        pass

    def on_pass(self):
        for line in self.container.logs(stream=True):
            print(line.decode('ascii'), end="")

    def on_fail(self):
        for line in self.container.logs(stream=True):
            print(line.decode('ascii'), end="")

    def task(self):
        self.container = self.client.containers.run(**self.config.as_dict())
        exit_code = self.container.wait()["StatusCode"]
        return exit_code

    def run(self):
        # noinspection PyBroadException
        try:
            self.status = JobStatus.Starting
            self.pre_run()
            self.status = JobStatus.Running
            code = self.task()
            if code != 0:
                self.status = JobStatus.Failed
                self.on_fail()
            else:
                self.status = JobStatus.Passed
                self.on_pass()
        # except:
        except KeyboardInterrupt:  # Catch any errors that occur and set the status as errored - present to user
            self.status = JobStatus.Errored
            self.on_error()
        self.post_run()
