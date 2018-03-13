from enum import Enum


class JobStatus(Enum):
    NotStarted = "Not Started"
    Starting = "Starting"
    Running = "Running"
    Errored = "Errored"
    Failed = "Failed"
    Passed = "Passed"
