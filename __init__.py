"""
Number Guessing Game package.

Expose the play_game entry point for users,
and optionally the main() CLI entry.
"""

from .game import play_game, main

__version__ = "1.0.0"
__author__ = "Bhimesh"
__description__ = "An interactive number guessing game where players try to guess a random number between 1 and 100."

__all__ = ["play_game", "main"]
