import reflex as rx,cloudinary,os

class WebuiConfig(rx.Config):
    pass

cloudinary.config(
    cloud_name = os.environ.get('CLOUD_NAME'),
    api_key = os.environ.get('API_KEY'),
    api_secret = os.environ.get('API_SECRET'),
    secure = True
)

config = WebuiConfig(
    app_name="webui",
    db_url="sqlite:///reflex.db",
    api_url="https://reflex-chat-w1pj.onrender.com",
    env=rx.Env.PROD,
    frontend_packages=[
        "react-loading-icons",
    ],
)
