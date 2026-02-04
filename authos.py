from agno.os import AgentOS
from agno.os.middleware import JWTMiddleware
from agent import agent
from fastapi import FastAPI
from datetime import datetime, timedelta
import jwt


JWT_SECRET = "SECRET"

base_app = FastAPI(
    title="Bot Collection",
    version="0.0.1",
)

base_app.add_middleware(
    JWTMiddleware,
    verification_keys=[JWT_SECRET],
    excluded_route_paths=[
        "/auth/login",
        "/docs",
        "/openapi.json",
    ],
    algorithm="HS256",
)

@base_app.post("/auth/login")
async def login(username: str, password: str):
    if username == "admin" and password == "admin":
        token = jwt.encode(
            {
                "sub": username,
                "username": username,
                "exp": datetime.utcnow() + timedelta(hours=24),
                "iat": datetime.utcnow(),
            },
            JWT_SECRET,
            algorithm="HS256"
        )
        return {
            "access_token": token,
            "token_type": "bearer",
        }
    raise HTTPException(status_code=401, detail="Invalid username or password")


agent_os = AgentOS(agents=[agent], base_app=base_app)
app = agent_os.get_app()

