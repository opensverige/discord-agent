#!/usr/bin/env python3
"""
OpenSverige Discord-agent — entry point.
Kräver .env med DISCORD_BOT_TOKEN (och valfritt DISCORD_GUILD_ID).
"""
import os
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent / "config" / "agent.yaml"
    if not config_path.exists():
        return None
    try:
        import yaml
        return yaml.safe_load(config_path.read_text())
    except Exception:
        return None

def main():
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        print("Sätt DISCORD_BOT_TOKEN i .env. Committa aldrig .env.")
        return

    config = load_config()
    print("Discord-agent — OpenSverige")
    print("Config:", "OK" if config else "ej läst (pip install pyyaml)")

    # TODO: starta Discord-bot (discord.py / nextcord / etc.)
    # Exempel med discord.py:
    # import discord
    # client = discord.Client(intents=...)
    # @client.event async def on_ready(): ...
    # client.run(token)
    print("Lägg Discord-klient och agent-logik här (src/).")

if __name__ == "__main__":
    main()
