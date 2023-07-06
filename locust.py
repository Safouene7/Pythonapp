from locust import HttpUser, between, TaskSet, task
from datetime import timedelta

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        headers = {"message": "User created"}
        response = self.client.post("/xxx", headers=headers, json={"id": 1, "name": "LPM", "lastname": "WMP"})

class MyUser(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(1, 5)

if __name__ == "__main__":
    my_user = MyUser()
    my_user.run()


