import ast
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT_FILE = ROOT / "combined_agro_dataset.json"
TARGET_VARS = {"qa_data", "master_qa_data", "master_qa_data_pashto"}

# Fallback for files that are not valid Python but still contain tuple rows.
TRIPLE_TUPLE_PATTERN = re.compile(
    r"""\(\s*(['"])(?P<prompt>.*?)(?<!\\)\1\s*,\s*(['"])(?P<answer>.*?)(?<!\\)\3\s*,\s*(['"])(?P<category>.*?)(?<!\\)\5\s*\)""",
    re.DOTALL,
)


def normalize_item(item, source_file, source_var):
    rec = {"source_file": source_file, "source_var": source_var}
    if isinstance(item, dict):
        rec.update(item)
    elif isinstance(item, (list, tuple)):
        if len(item) > 0:
            rec["prompt"] = item[0]
        if len(item) > 1:
            rec["answer"] = item[1]
        if len(item) > 2:
            rec["category"] = item[2]
        if len(item) > 3:
            rec["extra"] = list(item[3:])
    else:
        rec["value"] = item
    return rec


def extract_with_ast(file_path):
    text = file_path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(file_path))
    rows = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        if not names:
            continue
        var_name = names[0]
        if var_name not in TARGET_VARS:
            continue
        if not isinstance(node.value, (ast.List, ast.Tuple)):
            continue
        data = ast.literal_eval(node.value)
        if isinstance(data, list):
            rows.extend((var_name, item) for item in data)
    return rows


def extract_with_regex(file_path):
    text = file_path.read_text(encoding="utf-8")
    rows = []
    for match in TRIPLE_TUPLE_PATTERN.finditer(text):
        rows.append(
            (
                "regex_tuple_extract",
                (
                    match.group("prompt"),
                    match.group("answer"),
                    match.group("category"),
                ),
            )
        )
    return rows


def main():
    records = []
    py_files = sorted(
        p for p in ROOT.rglob("*.py") if p.is_file() and p.parent != ROOT
    )

    for py_file in py_files:
        source_file = str(py_file.relative_to(ROOT)).replace("\\", "/")
        try:
            rows = extract_with_ast(py_file)
        except SyntaxError:
            rows = extract_with_regex(py_file)

        for source_var, item in rows:
            records.append(normalize_item(item, source_file, source_var))

    OUT_FILE.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Processed {len(py_files)} files")
    print(f"Wrote {len(records)} records to {OUT_FILE}")


if __name__ == "__main__":
    main()
