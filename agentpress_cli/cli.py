"""Console entrypoint for AgentPress.

The implementation currently lives in `scripts.agentpress` so repo users can run
it without installation. This wrapper makes the same CLI installable via pipx/pip.
"""
from scripts.agentpress import main

__all__ = ["main"]
