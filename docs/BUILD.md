# Så bygger vi Discord-agenten

**Spec:** Mac mini 24/7, 16 GB RAM. **Framework:** antingen **nanoclaw** (lättvikt) eller **Hermes** ([NousResearch](https://github.com/nousresearch)) — Hermes rekommenderas om agenten ska ha **long-term memory** och logga vad som hänt i communityt.

1. **Identity** — Redigera `identity/agent.md` (roll, gränser). Org-mall: [agent-infra/identity](https://github.com/opensverige/.github/tree/main/agent-infra/identity).
2. **Discord-bot** — Implementera i `src/`: anslut med `DISCORD_BOT_TOKEN`, lyssna på events, anropa LLM/tools. T.ex. `discord.py` eller `nextcord`.
3. **Tools** — Lägg tool-specar i `tools/` (länka till org eller egna). Implementera anrop i `src/`.
4. **Memory** — Använd `memory/` för persistent state; committa inget känsligt. För **long-term memory** (logga vad som hänt i communityt): överväg Hermes (NousResearch) eller egen memory-layer; dokumentera i `memory/` enligt [agent-infra/memory](https://github.com/opensverige/.github/tree/main/agent-infra/memory).
5. **Nycklar** — Endast i `.env`. Uppdatera `.env.example` vid nya env-vars.

**Bygg tillsammans:** [Discord](https://www.opensverige.se/) · Få invit till [GitHub org](https://github.com/opensverige), pusha fritt.
