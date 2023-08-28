from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import requests

class HttpFileUploadOperator(BaseOperator):

    @apply_defaults
    def __init__(self, endpoint, file_path, *args, **kwargs):
        super(HttpFileUploadOperator, self).__init__(*args, **kwargs)
        self.endpoint = endpoint
        self.file_path = file_path

    def execute(self, context):
        with open(self.file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(self.endpoint, files=files)
            response.raise_for_status()  # Check for errors

        self.log.info(f"Response status code: {response.status_code}")
        self.log.info(f"Response text: {response.text}")
