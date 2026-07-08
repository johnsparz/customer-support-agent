from dataclasses import dataclass


@dataclass
class RetrievalResult:
    context: str
    source: str | None = None


@dataclass
class AgentResponse:
    answer: str
    route: str