# AIRecon-Colab

## 🚀 AI-Powered Security Reconnaissance using Google Colab, Ollama & Cloudflare Tunnel

AIRecon-Colab demonstrates how to run AIRecon using a remote Large Language Model (LLM) hosted on **Google Colab GPU** and securely connected to **Kali Linux** through **Cloudflare Tunnel**.

This project shows how AI can assist penetration testing by combining traditional security tools (Nmap, HTTP analysis, browser automation) with an LLM for intelligent analysis and reporting.

---

# 📌 Features

- AI-assisted penetration testing
- Google Colab GPU (Tesla T4)
- Ollama remote inference
- Cloudflare Tunnel integration
- Docker sandbox
- Nmap integration
- HTTP Observe
- Browser Automation
- Technology Fingerprinting
- Service Detection
- Open Port Discovery
- CVE Identification
- Security Header Analysis
- Interactive AIRecon TUI
- AI-generated Security Reports

---

# 🏗 Architecture

                    Google Colab
                 (Tesla T4 GPU)

                        │

                Ollama (Qwen3.5:9B)

                        │

             Cloudflare Tunnel (HTTPS)

                        │

                 Kali Linux (AIRecon)

                        │

        Nmap • Browser • HTTP Observe

                        │

               AI Security Assessment

---

# 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| OS | Kali Linux |
| Language | Python |
| AI Model | Qwen3.5:9B |
| LLM Server | Ollama |
| GPU | Google Colab Tesla T4 |
| Tunnel | Cloudflare Tunnel |
| Container | Docker |
| Scanner | Nmap |
| Framework | AIRecon |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Saikiranr27/AIRecon-Colab.git

cd AIRecon-Colab
```

---

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -e .
```

or

```bash
pip install -r requirements.txt
```

---

## Verify Installation

```bash
python -m airecon status
```

---

# ☁ Google Colab Setup

1. Open the Colab Notebook.
2. Enable GPU Runtime.
3. Start Ollama.
4. Load Qwen3.5:9B.
5. Start Cloudflare Tunnel.
6. Copy the Tunnel URL.

Example:

```
https://xxxxx.trycloudflare.com
```

---

# 🔧 Configure AIRecon

Update:

```
~/.airecon/config.yaml
```

Example

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

## Check Status

```bash
python -m airecon status
```

---

## Start AIRecon

```bash
python -m airecon
```

---

## Show Help

```text
/help
```

---

## Clear Screen

```text
/clear
```

---

## Show Skills

```text
/skills
```

---

## Exit

```text
/exit
```

---

# 🧪 Example Assessment Prompt

```
Target: https://portswigger.net/

Tasks:

1. Identify all open ports.

2. Identify running services.

3. Detect technologies.

4. Identify potential vulnerabilities.

5. Identify matching CVEs.

6. Display results only.

7. Do not exploit vulnerabilities.
```

---

# 📊 Workflow

```
Target

↓

Nmap Scan

↓

Technology Detection

↓

HTTP Analysis

↓

Browser Automation

↓

AI Analysis

↓

CVE Mapping

↓

Security Report
```

---

# 🎯 Tested Targets

- PortSwigger
- scanme.nmap.org
- testaspnet.vulnweb.com

---

# 📈 Sample Output

The tool identifies:

- Open Ports
- Services
- Technologies
- Security Headers
- CVEs
- Risk Level
- Security Posture
- Potential Vulnerabilities

---

# 📸 Screenshots

Add screenshots:

```
screenshots/

├── airecon-home.png

├── colab-gpu.png

├── cloudflare.png

├── status.png

├── portswigger.png

└── vulnweb.png
```

---

# 🚀 Future Improvements

- Gemini API Support
- OpenAI API Support
- Multi-LLM Support
- Better CVE Ranking
- Automatic PDF Reports
- RAG Integration
- Agent Memory Improvements

---

# 🙋 Frequently Asked Questions

### Why Google Colab?

To use a free Tesla T4 GPU for running Ollama.

### Why Cloudflare Tunnel?

To securely connect the Ollama server running in Colab with AIRecon on Kali Linux.

### Why Ollama?

To run open-source LLMs locally/remotely without relying on paid cloud APIs.

### Why AIRecon?

To automate reconnaissance and organize security findings using AI.

---

# 📚 Project Learnings

- Google Colab GPU integration
- Ollama deployment
- Cloudflare Tunnel setup
- Remote AI inference
- AI-assisted penetration testing
- Passive reconnaissance
- CVE mapping
- Docker sandbox usage

---

# 🤝 Credits

This repository is based on the open-source AIRecon project.

My contributions include:

- Google Colab integration
- Ollama remote deployment
- Cloudflare Tunnel configuration
- AIRecon setup on Kali Linux
- Testing and benchmarking
- Documentation and workflow improvements

---

# 📄 License

This repository follows the original AIRecon project license.
