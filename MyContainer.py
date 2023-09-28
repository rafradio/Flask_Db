import docker
import asyncio

class MyContainer():
    def __init__(self):
        self.client = docker.from_env()
        self.container = None
        self.cl = None

    async def start(self, cl):
        if cl == 0:
            ports = {'5432/tcp': 6444}
            environment = {"POSTGRES_USERNAME":"postgres", 
                        "POSTGRES_PASSWORD": "postgres", 
                        "POSTGRES_DB": "flask"
            }
            self.container = await self.client.containers.run('postgres:15.4', ports=ports, environment=environment, detach=True, name='flaskdb')
        else: 
            postgrContainer = self.client.containers.get('flaskdb')
            postgrContainer.start()
        

    async def fidContainer(self):
        conList = self.client.containers.list(all=True, filters={'name':'flaskdb'})
        return len(conList)
    
    async def starter(self):
        task1 = asyncio.create_task(self.fidContainer())
        cl = await task1
        task2 = asyncio.create_task(self.start(cl))
        print(cl)
        await task2
        print("OK")
