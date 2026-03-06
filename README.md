# Discord-agent — OpenSverige

AI-agent för OpenSveriges Discord. Vi bygger tillsammans — få invit till [GitHub-org](https://github.com/opensverige), pusha fritt, koordinera i [Discord](https://www.opensverige.se/).

---

## Vad är detta?

Eget repo för att bygga **en bra AI-agent** som lever i vår Discord: svarar, hjälper, följer [manifesto](https://github.com/opensverige/.github/blob/main/manifesto.md) och [agent-infra](https://github.com/opensverige/.github/tree/main/agent-infra) (identity, memory, tools). Inga nycklar i repot — alla credentials i `.env`.

---

## Körmiljö / spec

Agenten kör på **Mac mini**, 24/7, 16 GB RAM.

| | |
|--|--|
| **Maskin** | Mac mini |
| **Körning** | 24/7 |
| **RAM** | 16 GB |

**Agent-framework (välj ett):**

- **nanoclaw** — lättvikt, bra för enkel bot-logik.
- **Hermes** ([NousResearch](https://github.com/nousresearch)) — Hermes Agent framework; starkare stöd för **long-term memory**, bra om agenten ska logga och minnas vad som hänt i communityt (kanaler, beslut, sammanfattningar över tid).

Bygg och testa med dessa resurser i åtanke.

---

## Long-term memory (logga vad som hänt i communityt)

Om agenten ska **logga och minnas** vad som händer i Discord (viktiga händelser, beslut, sammanfattningar) rekommenderas **Hermes (NousResearch)** framför nanoclaw: bättre stöd för persistent minne och retrieval. Definiera vad som ska loggas i `memory/` och följ [agent-infra/memory](https://github.com/opensverige/.github/tree/main/agent-infra/memory) (transparens, ingen känslig data). Alternativ: egen memory-layer (t.ex. vektordatabas eller strukturerad logg) oavsett framework — dokumentera i `tools/` eller `memory/`.

---

## Snabbstart

1. **Klona** (kräver access till opensverige-org).
2. **Kopiera** `.env.example` → `.env`, fyll i `DISCORD_BOT_TOKEN` och andra nycklar. Committa aldrig `.env`.
3. **Installera:** `pip install -r requirements.txt`
4. **Kör:** `python src/main.py` (när bot-logik är på plats).

---

## Struktur

```
discord-agent/
├── README.md
├── .env.example        ← Discord + LLM-nycklar (inga värden)
├── config/
│   └── agent.yaml      ← identity, memory, tools
├── identity/           ← vem boten är (roll, gränser)
├── memory/             ← runtime-minne
├── tools/              ← tool-specar (länk till org eller egna)
├── src/                ← Discord-bot + agent-logik
│   └── main.py
├── docs/
│   └── BUILD.md
└── requirements.txt
```

---

## Regler (org)

- [Manifesto](https://github.com/opensverige/.github/blob/main/manifesto.md) — transparens, öppenhet, inga hemligheter i repo.
- [FOR_AGENTS](https://github.com/opensverige/.github/blob/main/FOR_AGENTS.md) — för AI som jobbar i org.
- [agent-infra](https://github.com/opensverige/.github/tree/main/agent-infra) — mallar för memory, tools, identity.

---

## Skapa repot på GitHub och pusha

1. Skapa ett nytt repo i [opensverige](https://github.com/opensverige)-org:en, t.ex. `discord-agent`. Välj inte "Add README" (ni har redan filer).
2. I denna mapp:  
   `git init && git add -A && git commit -m "feat: Discord-agent scaffold — OpenSverige"`  
   `git branch -M main && git remote add origin https://github.com/opensverige/discord-agent.git`  
   `git push -u origin main`
3. Sätt regler (branch protection, secrets) på repot som ni vill. Här bygger och pushar vi fritt.
