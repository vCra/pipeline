from pprint import pprint

from pipeline.jobs.job_status import JobStatus


class Job(object):
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
        pass

    def on_fail(self):
        for line in self.container.logs(stream=True):
            print(line.decode('ascii'), end="")

    def run(self):
        print("Running job " + self.config.name)
        pprint(self.config.as_dict())
        self.container = self.client.containers.run(**self.config.as_dict())
        exit_code = self.container.wait()["StatusCode"]
        return exit_code

    def begin(self):
        # noinspection PyBroadException
        try:
            self.status = JobStatus.Starting
            self.pre_run()
            self.status = JobStatus.Running
            code = self.run()
            if code != 0:
                self.status = JobStatus.Failed
                self.on_fail()
            else:
                self.status = JobStatus.Passed
                self.on_pass()
        # except:
        except:  # Catch any errors that occur and set the status as errored - present to user
            self.status = JobStatus.Errored
            self.on_error()
        self.post_run()
