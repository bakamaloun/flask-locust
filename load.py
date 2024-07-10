from locust import HttpUser, task, constant

class TestLoad(HttpUser):

    host = 'http://localhost:5000'
    wait_time = constant(1)

    @task(5)
    def get_index(self):
        self.client.get('/index')

    @task(1)
    def get_load(self):
        self.client.get('/moreload')






