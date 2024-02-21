import uvicorn
import uvloop
import asyncio

from settings import config_parameters

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


if __name__ == '__main__':

    uvicorn.run(
        'setup:server',
        host=config_parameters.API_HOST,
        port=config_parameters.API_PORT,
        loop='uvloop',
        reload=True,
        use_colors=True
    )
