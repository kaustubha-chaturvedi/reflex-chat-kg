import reflex as rx


class WebuiConfig(rx.Config):
    pass


config = WebuiConfig(
    app_name="webui",
    db_url="sqlite:///reflex.db",
    api_url="http://localhost:8000",
    env=rx.Env.PROD,
    frontend_packages=[
        "react-loading-icons",
    ],
)
