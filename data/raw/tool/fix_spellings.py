import argparse
import json
import re

def load_corrections(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def fix_token(token, corrections):
    # Split into leading punctuation, core word, trailing punctuation
    m = re.match(r"^(\W*)(.*?)(\W*)$", token, re.DOTALL)
    lead, core, trail = m.groups()

    # Try the whole token first (handles entries like "fi-ee" or "registi'ation")
    if token in corrections:
        return corrections[token]
    if core in corrections:
        return lead + corrections[core] + trail
    return token

def fix_text(text, corrections):
    # Split on whitespace but keep the whitespace so formatting is preserved
    parts = re.split(r"(\s+)", text)
    return "".join(
        p if p.isspace() or not p else fix_token(p, corrections)
        for p in parts
    )

def main():
    parser = argparse.ArgumentParser(description="Fix misspelled words in a text file.")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("output", help="Path to output text file")
    parser.add_argument(
        "-j", "--json",
        default="misspelled.json",
        help="Path to corrections JSON file (default: misspelled.json)",
    )
    args = parser.parse_args()

    corrections = load_corrections(args.json)

    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(fix_text(text, corrections))

    print(f"Done. Wrote corrected text to {args.output}")

if __name__ == "__main__":
    main()