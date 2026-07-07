# AIRecon-Colab

> AI-powered security reconnaissance using **AIRecon**, **Google Colab**, **Ollama (Qwen3.5:9B)**, and **Cloudflare Tunnel**.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/OS-Kali%20Linux-success)
![LLM](https://img.shields.io/badge/LLM-Qwen3.5%209B-orange)
![GPU](https://img.shields.io/badge/GPU-Tesla%20T4-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

This repository demonstrates how to run **AIRecon** with a **remote Ollama server hosted on Google Colab** using a **Tesla T4 GPU** and securely connect it to **Kali Linux** through **Cloudflare Tunnel**.

The project explores AI-assisted security reconnaissance by combining traditional penetration testing tools with a Large Language Model (LLM) for intelligent reasoning and reporting.

---

# ✨ Features

- AI-assisted reconnaissance
- Remote Ollama inference
- Google Colab GPU integration
- Cloudflare Tunnel connectivity
- Docker sandbox execution
- Nmap integration
- HTTP observation
- Browser automation
- Open port discovery
- Service detection
- Technology fingerprinting
- Security header analysis
- CVE identification
- AI-generated security reports

---

# 🏗 Architecture

```text
                   Google Colab
                (Tesla T4 GPU)

                       │

               Ollama (Qwen3.5:9B)

                       │

          Cloudflare Tunnel (HTTPS)

                       │

             Kali Linux (AIRecon)

                       │

       ┌────────┬─────────┬──────────┐
       │        │         │
       ▼        ▼         ▼
     Nmap   HTTP Observe  Browser

                       │

                 AI Analysis

                       │

              Security Report
```

---

# 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Operating System | Kali Linux |
| Language | Python |
| AI Framework | AIRecon |
| LLM | Qwen3.5:9B |
| LLM Server | Ollama |
| GPU | Google Colab (Tesla T4) |
| Tunnel | Cloudflare Tunnel |
| Container | Docker |
| Scanner | Nmap |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Saikiranr27/AIRecon-Colab.git
cd AIRecon-Colab
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -e .
```

or

```bash
pip install -r requirements.txt
```

## Verify Installation

```bash
python -m airecon status
```

---

# ☁ Google Colab Setup

1. Open the AIRecon Colab notebook.
2. Enable **GPU Runtime**.
3. Start Ollama.
4. Load the **Qwen3.5:9B** model.
5. Start the Cloudflare Tunnel.
6. Copy the generated Tunnel URL.
7. Update `~/.airecon/config.yaml`.

Example:

```yaml
ollama_url: "https://xxxxx.trycloudflare.com"
ollama_model: "qwen3.5:9b"
ollama_timeout: 300
ollama_chunk_timeout: 300
```

---

# ▶ Running AIRecon

```bash
python -m airecon
```

---

# 📋 Useful Commands

Check Status

```bash
python -m airecon status
```

Start AIRecon

```bash
python -m airecon
```

Show Help

```text
/help
```

Show Skills

```text
/skills
```

Clear Screen

```text
/clear
```

Exit

```text
/exit
```

---

# 🧪 Example Assessment Prompt

```text
Target: https://portswigger.net/

Tasks:

1. Identify open ports.
2. Detect running services.
3. Detect technologies.
4. Identify potential vulnerabilities.
5. Identify related CVEs.
6. Display the assessment.
7. Do not perform exploitation.
```

---

# 📊 Workflow

```text
Target
   │
   ▼
Reconnaissance
   │
   ▼
Nmap Scan
   │
   ▼
Technology Detection
   │
   ▼
HTTP Analysis
   │
   ▼
Browser Automation
   │
   ▼
AI Analysis (Qwen3.5:9B)
   │
   ▼
Security Assessment
```

---

# 🎯 Tested Targets

The project was evaluated on publicly available practice targets:

- https://portswigger.net
- https://scanme.nmap.org
- http://testaspnet.vulnweb.com

Testing focused on:

- Open Port Discovery
- Service Detection
- Technology Fingerprinting
- Security Header Analysis
- CVE Identification
- Passive Vulnerability Assessment

---

# 📈 Sample Results

AIRecon successfully identified:

- Open Ports
- Running Services
- Web Technologies
- Security Headers
- Potential Vulnerabilities
- CVEs (when applicable)
- Risk Level
- Security Posture

---

# 📸 Screenshots

Add your screenshots in the `screenshots/` folder.

```text
screenshots/
├── status.png
├── colab.png
├── tunnel.png
├── portswigger.png
└── vulnweb.png
```

Example:

```markdown
![AIRecon Status](screenshots/status.png)

![Google Colab](screenshots/colab.png)

![PortSwigger Assessment](screenshots/portswigger.png)
```

---

# 🚀 Future Improvements

- Gemini API integration
- Multi-model support
- Improved CVE ranking
- PDF report generation
- RAG integration
- Enhanced agent memory

---

# 📚 What I Learned

Through this project I gained hands-on experience with:

- Google Colab GPU deployment
- Ollama configuration
- Cloudflare Tunnel setup
- Remote LLM inference
- AI-assisted penetration testing
- Docker sandbox execution
- Passive reconnaissance
- CVE mapping
- Security reporting

---

# 🙋 FAQ

### Why Google Colab?

To run the Qwen3.5:9B model on a free Tesla T4 GPU because my local machine does not have sufficient GPU resources.

### Why Cloudflare Tunnel?

To securely expose the Ollama server running inside Google Colab to AIRecon on Kali Linux.

### Why Ollama?

To host and serve open-source LLMs without relying on proprietary cloud-hosted inference.

### Why AIRecon?

To automate reconnaissance and assist with security assessments using AI.

---

# 🤝 Credits

This repository is based on the open-source **AIRecon** project.

My contributions include:

- Integrating Google Colab with AIRecon
- Configuring remote Ollama inference
- Setting up Cloudflare Tunnel
- Testing reconnaissance workflows
- Benchmarking AIRecon
- Creating project documentation

---

# 📄 License

This repository follows the original AIRecon project license (MIT).
