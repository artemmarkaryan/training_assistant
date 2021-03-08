from channels.consumer import AsyncConsumer
import asyncio
from training_assistant_app.helpers import response_wrapper
from sber_backend import db_interface

pool = []


class SessionConsumer(AsyncConsumer):
    GLOBAL_STATS_UPDATE_PERIOD: int = 10

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })
        pool.append(self)
        await self.dispatch_status()

    async def websocket_receive(self, event):
        await self.send(response_wrapper.wrap_ws_message("pong"))

    async def send(self, message):
        await super().send(message)

    async def dispatch_status(self):
        while True:
            connection: SessionConsumer
            statistics = await db_interface.statistics.get_daily_statistics()

            for connection in pool:
                await connection.send(
                    response_wrapper.wrap_ws_data(
                        data=statistics,
                        payload_type="UPDATE_DAILY_GLOBAL_STATS",
                    )
                )
            await asyncio.sleep(self.GLOBAL_STATS_UPDATE_PERIOD)
