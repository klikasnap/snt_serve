from rich.pretty import pprint;{"detail":"Server Error","message":"Error occured","error":true,"traceback":"Traceback (most recent call last):\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/streams\/memory.py\", line 105, in receive\n    return self.receive_nowait()\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/streams\/memory.py\", line 100, in receive_nowait\n    raise WouldBlock\nanyio.WouldBlock\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/streams\/memory.py\", line 118, in receive\n    return receiver.item\n           ^^^^^^^^^^^^^\nAttributeError: 'MemoryObjectItemReceiver' object has no attribute 'item'\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/middleware\/base.py\", line 159, in call_next\n    message = await recv_stream.receive()\n              ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/streams\/memory.py\", line 120, in receive\n    raise EndOfStream\nanyio.EndOfStream\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/main.py\", line 82, in add_process_time_header\n    response = await call_next(request)\n               ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/middleware\/base.py\", line 165, in call_next\n    raise app_exc\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/middleware\/base.py\", line 151, in coro\n    await self.app(scope, receive_or_disconnect, send_no_error)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/middleware\/sessions.py\", line 85, in __call__\n    await self.app(scope, receive, send_wrapper)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/middleware\/exceptions.py\", line 65, in __call__\n    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/_exception_handler.py\", line 64, in wrapped_app\n    raise exc\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/_exception_handler.py\", line 53, in wrapped_app\n    await app(scope, receive, sender)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/routing.py\", line 756, in __call__\n    await self.middleware_stack(scope, receive, send)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/routing.py\", line 776, in app\n    await route.handle(scope, receive, send)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/routing.py\", line 297, in handle\n    await self.app(scope, receive, send)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/routing.py\", line 77, in app\n    await wrap_app_handling_exceptions(app, request)(scope, receive, send)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/_exception_handler.py\", line 64, in wrapped_app\n    raise exc\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/_exception_handler.py\", line 53, in wrapped_app\n    await app(scope, receive, sender)\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/routing.py\", line 72, in app\n    response = await func(request)\n               ^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/fastapi\/routing.py\", line 278, in app\n    raw_response = await run_endpoint_function(\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/fastapi\/routing.py\", line 193, in run_endpoint_function\n    return await run_in_threadpool(dependant.call, **values)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/concurrency.py\", line 42, in run_in_threadpool\n    return await anyio.to_thread.run_sync(func, *args)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/to_thread.py\", line 56, in run_sync\n    return await get_async_backend().run_sync_in_worker_thread(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/_backends\/_asyncio.py\", line 2177, in run_sync_in_worker_thread\n    return await future\n           ^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/anyio\/_backends\/_asyncio.py\", line 859, in run\n    result = context.run(func, *args)\n             ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/main.py\", line 122, in code_get\n    return TEMPLATES.TemplateResponse(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/templating.py\", line 229, in TemplateResponse\n    template = self.get_template(name)\n               ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/starlette\/templating.py\", line 143, in get_template\n    return self.env.get_template(name)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/jinja2\/environment.py\", line 1013, in get_template\n    return self._load_template(name, globals)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/jinja2\/environment.py\", line 972, in _load_template\n    template = self.loader.load(self, name, self.make_globals(globals))\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/jinja2\/loaders.py\", line 126, in load\n    source, filename, uptodate = self.get_source(environment, name)\n                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"\/home\/lyra\/lyra\/3\/projects\/business\/codebases\/snt-serve\/.venv\/lib\/python3.12\/site-packages\/jinja2\/loaders.py\", line 207, in get_source\n    raise TemplateNotFound(template)\njinja2.exceptions.TemplateNotFound: code.j2.html\n","status":{"code":500}}