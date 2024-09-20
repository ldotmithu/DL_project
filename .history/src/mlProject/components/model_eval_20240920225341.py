import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlpars
from mlProject.config.configuration import *

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config