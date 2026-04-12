import os
import re


TREE_LINE_RE = re.compile(
    r'^(?P<prefix>(?:\|\s)*)\|--\s(?P<name>.+?)\s*$'
)


def parse_tree_file(structure_file):
    items = []

    with open(structure_file, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")
            if not line.strip():
                continue

            match = TREE_LINE_RE.match(line)
            if not match:
                print(f"Skipping unrecognized line: {line}")
                continue

            prefix = match.group("prefix")
            name = match.group("name").strip()

            # Depth is the number of "| " groups before "|--"
            depth = prefix.count("|")

            items.append({
                "depth": depth,
                "name": name,
            })

    return items


def looks_like_file(name):
    # Basic heuristic: has an extension in the final path component
    base = os.path.basename(name.rstrip("/"))
    return "." in base and not name.endswith("/")


def create_structure_from_file(dest_base, structure_file):
    os.makedirs(dest_base, exist_ok=True)

    items = parse_tree_file(structure_file)

    # paths_by_depth[0] = dest_base
    paths_by_depth = {0: dest_base}

    for i, item in enumerate(items):
        depth = item["depth"]
        name = item["name"]

        parent_path = paths_by_depth.get(depth, dest_base)
        full_path = os.path.join(parent_path, name.rstrip("/"))

        # Decide whether this entry is a directory
        next_depth = items[i + 1]["depth"] if i + 1 < len(items) else None
        is_dir = (
            name.endswith("/") or
            (next_depth is not None and next_depth > depth) or
            (not looks_like_file(name))
        )

        if is_dir:
            os.makedirs(full_path, exist_ok=True)
            paths_by_depth[depth + 1] = full_path
            print(f"📁 Dir:  {full_path}")
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as file_out:
                pass
            print(f"📄 File: {full_path}")


if __name__ == "__main__":
    target_dir = input("Enter the destination directory name: ").strip()
    config_file = input("Enter the path to your .txt structure file: ").strip()

    create_structure_from_file(target_dir, config_file)
    print("\n✅ Task completed.")