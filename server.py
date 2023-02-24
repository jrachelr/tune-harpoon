from fastapi import FastAPI

class ApiServer:
    def __init__(self):
        self.app = FastAPI()

        @self.app.get("/")
        async def read_root():
            # TODO: grab url & download
            return {"Hello": "World"}

server = ApiServer()

server.run()