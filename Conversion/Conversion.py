import json
from pathlib import Path


INPUT_PATH = r"INPUT_PATH_HERE.jsonl"
OUTPUT_PATH = r"OUTPUT_PATH_HERE.jsonl"
SYSTEM_PROMPT_PATH = r"react_soc_prompt.txt"


with open(
    SYSTEM_PROMPT_PATH,
    "r",
    encoding="utf-8"
) as f:

    SYSTEM_PROMPT = f.read().strip()

def build_assistant_output(label):

    output = {
        "thought_process": label.get(
            "analyst_rationale",
            ""
        ),

        "mitre_tactics": label.get(
            "mitre_tactics",
            ["Unknown"]
        ),

        "mitre_techniques": label.get(
            "mitre_techniques",
            ["Unknown"]
        ),

        "risk_level": label.get(
            "risk_level",
            "Unknown"
        ),

        "recommended_actions": label.get(
            "recommended_actions",
            []
        ),

        "summary": label.get(
            "summary",
            ""
        )
    }

    # Optional fields
    if "verdict" in label:
        output["verdict"] = label["verdict"]

    if "label_source" in label:
        output["verdict_source"] = label["label_source"]

    return json.dumps(
        output,
        ensure_ascii=False
    )


# =========================
# CONVERT
# =========================

def convert_record(record):

    narrative = record.get(
        "narrative",
        ""
    )

    label = record.get(
        "label",
        {}
    )

    new_record = {
        "messages": [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": narrative
            },

            {
                "role": "assistant",
                "content": build_assistant_output(
                    label
                )
            }
        ]
    }

    return new_record


# =========================
# RUN
# =========================

def main():

    input_path = Path(INPUT_PATH)
    output_path = Path(OUTPUT_PATH)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    total = 0
    converted = 0
    failed = 0

    with input_path.open(
        "r",
        encoding="utf-8"
    ) as fin, output_path.open(
        "w",
        encoding="utf-8"
    ) as fout:

        for line in fin:

            line = line.strip()

            if not line:
                continue

            total += 1

            try:

                record = json.loads(line)

                converted_record = convert_record(
                    record
                )

                fout.write(
                    json.dumps(
                        converted_record,
                        ensure_ascii=False
                    ) + "\n"
                )

                converted += 1

            except Exception as e:

                failed += 1

                print(
                    f"[ERROR] line {total}: {e}"
                )

    print("\n========== DONE ==========")
    print(f"Input records : {total}")
    print(f"Converted     : {converted}")
    print(f"Failed        : {failed}")
    print(f"Output file   : {output_path}")

if __name__ == "__main__":
    main()