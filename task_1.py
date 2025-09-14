import argparse
import shutil
from pathlib import Path

def copy_files_recursive(src: Path, dst: Path, root_src: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files_recursive(item, dst, root_src)
            elif item.is_file():
                ext = item.suffix[1:] if item.suffix else "no_ext"
                
                relative_path = item.relative_to(root_src)
                target_dir = dst / relative_path.parent / ext
                target_dir.mkdir(parents=True, exist_ok=True)
                target_file = target_dir / item.name
                shutil.copy2(item, target_file)
                print(f"Скопійовано: {item} → {target_file}")
    except PermissionError:
        print(f"⚠️ Немає доступу до: {src}")
    except Exception as e:
        print(f"❌ Помилка при обробці {src}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширенням"
    )
    parser.add_argument("src", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument(
        "dst", type=Path, nargs="?", default=None,
        help="Шлях до директорії призначення (за замовчуванням: dist поруч із src)"
    )
    args = parser.parse_args()

    src = args.src
    if not src.exists() or not src.is_dir():
        print("❌ Вихідна директорія не існує або не є папкою")
        return

    dst = args.dst or src.parent / "dist"
    dst.mkdir(parents=True, exist_ok=True)

    copy_files_recursive(src, dst, root_src=src)

if __name__ == "__main__":
    main()
