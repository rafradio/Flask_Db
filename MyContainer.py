import docker

class MyContainer():
    def __init__(self):
        self.container = None

    def start(self):
        client = docker.from_env()
        ports = {'5432/tcp': 6444}
        environment = {"POSTGRES_USERNAME":"postgres", 
                       "POSTGRES_PASSWORD": "postgres", 
                       "POSTGRES_DB": "flask"
        }
        self.container = client.containers.run('postgres:15.4', ports=ports, environment=environment, detach=True)
        print('OK')