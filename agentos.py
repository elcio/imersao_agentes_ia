from agno.os import AgentOS
from agent import agent

agent_os = AgentOS(
    agents=[agent],
    cors_allowed_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
)
app = agent_os.get_app()

