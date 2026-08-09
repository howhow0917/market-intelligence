from dataclasses import dataclass


@dataclass
class Config:
    project_name: str = "market-intelligence"
    version: str = "0.1.0"
    debug: bool = True


config = Config()
