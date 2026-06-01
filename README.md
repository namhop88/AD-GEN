# AD-GEN: Evidence-Preserving Generation of Validated ATT&CK-Aligned Narratives from Large-Scale Endpoint Telemetry

<p align="center">
  <img src="docs/pipeline.png" width="100%">
</p>

<p align="center">
  <b>LLM-ready endpoint security dataset for SOC automation, ATT&CK reasoning, and instruction tuning</b>
</p>

---

# Overview

AD-GEN transforms large-scale Windows Sysmon telemetry from the COMISET corpus into process-centric, privacy-preserving, compressed, and validated ATT&CK-aligned narrative records.

It is designed for:

- LLM-based SOC automation
- ATT&CK-aware instruction tuning
- Threat hunting assistant development
- Endpoint behavior reasoning
- Security narrative generation

---

# Dataset Scale

| Metric | LAB | REAL | Total |
|---|---:|---:|---:|
| Raw Sysmon Events | 49,914,325 | 202,304,790 | 252,219,115 |
| Post-Squash Events | 21,360,985 | 31,571,618 | 52,932,603 |
| Step 2 Narratives | 49,745 | 185,978 | 235,723 |
| Step 3 LLM Outputs | 50,671 | 190,109 | 240,780 |
| Step 4 Validated Outputs | 50,622 | 190,085 | 240,707 |

---

# Compression Statistics

| Environment | Raw Events | Post-Squash Events | Compression Ratio | Event Reduction |
|---|---:|---:|---:|---:|
| LAB | 49,914,325 | 21,360,985 | 2.34× | 57.20% |
| REAL | 202,304,790 | 31,571,618 | 6.41× | 84.39% |
| Overall | 252,219,115 | 52,932,603 | 4.76× | 79.01% |

---

# Risk Distribution

| Risk Level | Count | Percentage |
|---|---:|---:|
| Low | 234,046 | 97.26% |
| Medium | 3,131 | 1.30% |
| High | 2,607 | 1.08% |
| Critical | 847 | 0.35% |

---

# Top MITRE ATT&CK Tactics

| Tactic ID | Tactic Name | Frequency |
|---|---|---:|
| TA0004 | Privilege Escalation | 3,157 |
| TA0005 | Defense Evasion | 2,511 |
| TA0003 | Persistence | 2,451 |
| TA0002 | Execution | 1,763 |
| TA0007 | Discovery | 727 |
| TA0006 | Credential Access | 603 |

---

# Output Format

Each record is stored as JSONL.

```json
{
  "sample_id": "ADGEN_0000001",
  "environment": "LAB",
  "source_dataset": "COMISET",
  "narrative": "...",
  "sysmon_hints": ["T1055"],
  "label": {
    "risk_level": "Medium",
    "mitre_tactics": ["TA0005"],
    "mitre_techniques": ["T1055"],
    "recommended_actions": [
      {
        "tool_name": "get_file_metadata",
        "parameters": {}
      }
    ],
    "summary": "Process access behavior consistent with process injection.",
    "analyst_rationale": "Evidence-based analyst reasoning.",
    "verdict": "suspicious",
    "label_source": "llm_validated"
  }
}
```

---

# Supported SOC Actions

```text
check_threat_intel
get_file_metadata
query_registry
get_network_flow
terminate_process
isolate_host
no_action
```

---

# Label Quality

| Metric | LAB | REAL |
|---|---:|---:|
| Parse Success | 100.00% | 100.00% |
| Schema Validity | 99.93% | 99.98% |
| Verdict Consistency | 95.98% | 98.64% |
| Unknown Tactics After Validation | 0.032% | 0.007% |
| Unknown Techniques After Validation | 0.041% | 0.013% |
| Invalid Actions | 0 | 0 |

---
# Cross-Model Audit

| Metric | Value |
|---|---:|
| Audit Samples | 300 |
| Auditor Models | 3 |
| GPT-5.5 Composite Score | 0.748 |
| Claude Opus 4.8 Composite Score | 0.748 |
| Minimum Evidence Support Score | >0.72 |
| Minimum ATT&CK Alignment Score | >0.72 |

Three independent frontier language models (GPT-5.5, Claude Opus 4.8, and Gemini 3.5 Flash) were used to evaluate stratified samples from both LAB and REAL environments. Independent audits converged to nearly identical quality assessments, supporting the reliability and consistency of the validated ATT&CK-aligned labels.

# Repository Structure

```text
AD-GEN
├── README.md
├── LAB
│   └── NEW_LAB.jsonl
├── REAL
│   └── NEW_REAL.jsonl
├── docs
│   └── pipeline.png
└── Conversion
    ├── Conversion.py
    └── react_soc_prompt.txt
```

---

# Installation

```bash
git clone https://github.com/namhop88/AD-GEN.git
cd AD-GEN
```

---

# Files

| File | Description |
|---|---|
| `LAB/NEW_LAB.jsonl` | AD-GEN processed records derived from the COMISET laboratory environment |
| `REAL/NEW_REAL.jsonl` | AD-GEN processed records derived from the COMISET real university network environment |
| `docs/pipeline.png` | Overview of the AD-GEN transformation pipeline |
| `Conversion/Conversion.py` | Utility for converting records to the release format |
| `Conversion/react_soc_prompt.txt` | ReAct-style SOC labeling prompt used during generation |
---
AD-GEN is derived from the COMISET Windows endpoint telemetry corpus; it does not claim to be the original raw telemetry source.
# Important Note

AD-GEN labels are **validated synthetic analyst labels**, not human-adjudicated forensic ground truth.

The dataset is intended for research in instruction tuning, weak supervision, SOC assistant development, ATT&CK-aware reasoning, and endpoint narrative modeling. Additional expert review is recommended before operational use.

---

# Citation

```bibtex
@article{nam2026adgen,
  title   = {AD-GEN: Evidence-Preserving Generation of Validated ATT\&CK-Aligned Narratives from Large-Scale Endpoint Telemetry},
  author  = {Dinh Phuong Nam and Nguyen Tan Cam},
  year    = {2026},
  journal = {Preprint}
}
```

---

# License

| Component | License |
|---|---|
| Source Code | MIT License |
| Dataset | CC BY-NC 4.0 |

---

# Disclaimer

AD-GEN is released for academic and defensive cybersecurity research only. It should not be used as the sole basis for operational security decisions without expert validation.

---

# Contact

**Dinh Phuong Nam**  
University of Information Technology (UIT), VNU-HCM  

HUTECH University

GitHub: `@namhop88`