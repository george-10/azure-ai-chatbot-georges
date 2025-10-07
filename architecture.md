# Azure AI Chatbot – Architecture & Design Decisions

> This document explains the architecture pictured in the accompanying diagram of the Azure AI chatbot system.

---

## Goals

- Build a chatbot that serves a web UI and calls Azure OpenAI to generate answers.
- Persist user chat data and content in a relational store.
- Keep the design simple to operate, with clear separation of concerns, and room to scale independently.

---

## High‑level topology (what the diagram shows)

- Resource Group scopes all resources.

- Front end: a container app hosting the web client (React).

- Back end: a container app hosting the API (Flask) that communicates with Azure OpenAI and the database.

- Azure OpenAI: the managed LLM endpoint used for chat completions.

- Database: Azure Database for PostgreSQL (flexible server) for durable state: users, chats and messages.

---

## Request flow (end‑to‑end)

1. User opens the Front end.
2. Front end calls the Back end API.
3. API fetches/updates conversation state in PostgreSQL and assembles prompts.
4. API calls Azure OpenAI and sends tokens back to the client.
5. API persists messages to PostgreSQL.


---


