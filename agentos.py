from agno.os import AgentOS
from agent import agent

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

