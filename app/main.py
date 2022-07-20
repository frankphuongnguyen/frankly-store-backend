from fastapi import FastAPI

app = FastAPI()

def get_application() -> FastAPI:
    application = FastAPI(**configure_kwargs)

    application.include_router(account_api_router, prefix=settings.account_api_prefix)
    return application

app = get_application()
