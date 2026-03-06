# Så bygger vi Discord-agenten

**Spec:** Agenten körs i **nanoclaw** på en **Mac mini** (24/7, 16 GB RAM). Håll resursanvändning och beroenden anpassade till det.

1. **Identity** — Redigera `identity/agent.md` (roll, gränser). Org-mall: [agent-infra/identity](https://github.com/opensverige/.github/tree/main/agent-infra/identity).
2. **Discord-bot** — Implementera i `src/`: anslut med `DISCORD_BOT_TOKEN`, lyssna på events, anropa LLM/tools. T.ex. `discord.py` eller `nextcord`.
3. **Tools** — Lägg tool-specar i `tools/` (länka till org eller egna). Implementera anrop i `src/`.
4. **Memory** — Använd `memory/` för persistent state; committa inget känsligt.
5. **Nycklar** — Endast i `.env`. Uppdatera `.env.example` vid nya env-vars.

**Bygg tillsammans:** [Discord](https://www.opensverige.se/) · Få invit till [GitHub org](https://github.com/opensverige), pusha fritt.
