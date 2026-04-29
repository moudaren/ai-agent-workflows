# AI Agent Workflows (LLM + Automation)

This repository contains a collection of lightweight AI Agent workflows built on top of LLMs (e.g. ChatGPT API) combined with rule-based tools.

## 🚀 Overview

This project demonstrates how to build practical AI-powered automation pipelines:

- Game Build Analyzer (Path of Exile)
- Script Translation Agent (Ren'Py .rpy)
- Probability Simulation Tools
- General Agent Workflow Orchestration

## 🧠 Architecture

The core pattern follows:

Task → Decomposition → Tool Use → LLM Reasoning → Output Validation

### Components:

- **LLM Layer**: reasoning, explanation, text generation
- **Tool Layer**: parsing, simulation, structured processing
- **Agent Orchestration**: workflow control & iteration

---

## 🛠 Features

### 1. PoE Build Analyzer (Simplified)

- Parse build data
- Analyze item modifiers
- Generate optimization suggestions using LLM

### 2. Translation Agent

- Extract structured text from `.rpy`
- Translate with context awareness
- Preserve code structure

### 3. Crafting Simulator (Basic)

- Simulate probabilities
- Estimate expected cost
- Provide strategy suggestions

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
