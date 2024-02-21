import asyncio
import os

import redis.asyncio as redis
import uvloop
from starlette.middleware.base import BaseHTTPMiddleware

# from core.models.models import AdminAccount
# from providers.login_provider import LoginProvider
# from resources import resources_list
# from routers import router as root_router
from core.models import init as init_database
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import router
from settings import config_parameters
from starlette.middleware.cors import CORSMiddleware
# from fastapi_admin.app import app as admin_app, FastAPIAdmin
from fastapi_admin.exceptions import (
    forbidden_error_exception,
    not_found_error_exception,
    server_error_exception,
    unauthorized_error_exception,
)
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from fastapi_admin import template as template_root
# from middlewares import lang_middleware

#
# def create_app() -> (FastAPI, FastAPIAdmin):
#     app = FastAPI(title='X10-AdminPanel', debug=True)
#     app.mount("/admin/static", StaticFiles(directory="static"), name="static")
#     print(admin_app.routes)
#
#     admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
#     admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
#     admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
#     admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)
#     for i in range(len(admin_app.routes)):
#         del admin_app.routes[0]
#     admin_app.include_router(root_router)
#     print(admin_app.routes)
#
#
#     @app.on_event("startup")
#     async def startup():
#         r = redis.from_url(url=config_parameters.REDIS_URL,
#                            decode_responses=True,
#                            encoding="utf8",
#                            )
#         await admin_app.configure(
#             default_locale="en_US",
#             # logo_url="https://static.tildacdn.com/tild3866-3665-4264-a465-313835306266/logotypes_1.svg",
#             # favicon_url='https://static.tildacdn.com/tild3866-3665-4264-a465-313835306266/logotypes_1.svg',
#             logo_url='/admin/static/logo/Logo_X10_white.svg',
#             favicon_url='/admin/static/logo/Logo_X10_white.svg',
#             template_folders=[config_parameters.TEMPLATES_DIR],
#
#             providers=[
#                 LoginProvider(
#                     login_logo_url="/admin/static/logo/Logo_X10_white.svg",
#                     admin_model=AdminAccount,
#                 )
#             ],
#             redis=r,
#         )
#
#     template_root.add_template_folder(config_parameters.TEMPLATES_DIR)
#     admin_app.register_resources(*resources_list)
#     admin_app.user_middleware.pop(0)
#     admin_app.add_middleware(BaseHTTPMiddleware, dispatch=lang_middleware.language_processor)
#
#     app.mount("/admin", admin_app)
#
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#         expose_headers=["*"],
#     )
#
#     # app.include_router(routes_users)
#
#     return app, admin_app
#
#
# # uvloop.install()
# # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# server, admin_server = create_app()

# server.include_router(root_router)

server = FastAPI(title='portfolio', debug=True)
server.include_router(router)
server.mount("/static", StaticFiles(directory="static"), name="static")

init_database(server)
# init_database(admin_server)

#
# @server.on_event("startup")
# async def on_startup():
#     await bot_on_startup()
#
#
# @server.on_event("shutdown")
# async def on_shutdown():
#     await bot_on_shutdown()
