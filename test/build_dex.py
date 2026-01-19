#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def _run(cmd: list[str], *, cwd: Path | None = None) -> None:
    p = subprocess.run(cmd, cwd=str(cwd) if cwd else None)
    if p.returncode != 0:
        raise SystemExit(p.returncode)


def _run_capture(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def _find_dx_jar(repo_root: Path) -> Path:
    env = os.environ.get("DX_JAR")
    if env:
        p = Path(env)
        if p.is_file():
            return p

    local = repo_root / "test" / "dx.jar"
    if local.is_file():
        return local

    candidates = [
        repo_root / "build-dx" / "dx.jar",
        repo_root / "cmake-build-debug-wsl" / "dalvik" / "dx" / "dx.jar",
        repo_root / "cmake-build-release-wsl" / "dalvik" / "dx" / "dx.jar",
    ]
    for c in candidates:
        if c.is_file():
            return c

    raise FileNotFoundError(
        "dx.jar not found. Provide --dx-jar or set DX_JAR env var, or build it under build-dx/."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile Java sources under test/ and build classes.dex using dx.jar")
    parser.add_argument(
        "--src",
        default=str(Path(__file__).resolve().parent / "java"),
        help="Java source root (default: test/java)",
    )
    parser.add_argument(
        "--out",
        default=str(Path(__file__).resolve().parent / "out"),
        help="Output directory (default: test/out)",
    )
    parser.add_argument(
        "--dx-jar",
        default="",
        help="Path to dx.jar (default: auto-detect or DX_JAR env)",
    )
    parser.add_argument(
        "--javac",
        default=os.environ.get("JAVAC", "javac"),
        help="javac executable (default: env JAVAC or 'javac')",
    )
    parser.add_argument(
        "--mode",
        choices=["release", "source-target"],
        default="source-target",
        help="Compilation mode. 'source-target' is for legacy dx compatibility.",
    )
    parser.add_argument("--release", default="8", help="javac --release (used when --mode=release)")
    parser.add_argument("--source", default="1.7", help="javac -source (used when --mode=source-target)")
    parser.add_argument("--target", default="1.7", help="javac -target (used when --mode=source-target)")
    parser.add_argument("--clean", action="store_true", help="Clean output directory before building")

    args, extra_javac = parser.parse_known_args()

    repo_root = Path(__file__).resolve().parents[1]
    src_root = Path(args.src).resolve()
    out_root = Path(args.out).resolve()
    classes_dir = out_root / "classes"
    dex_out = out_root / "classes.dex"

    dx_jar = Path(args.dx_jar).resolve() if args.dx_jar else _find_dx_jar(repo_root)

    java_files = sorted(p for p in src_root.rglob("*.java") if p.is_file())
    if not java_files:
        print(f"No .java files under: {src_root}", file=sys.stderr)
        return 2

    if args.clean and out_root.exists():
        shutil.rmtree(out_root)

    classes_dir.mkdir(parents=True, exist_ok=True)

    if args.mode == "release":
        javac_cmd = [
            args.javac,
            "--release",
            str(args.release),
            "-encoding",
            "UTF-8",
            "-d",
            str(classes_dir),
            *extra_javac,
            *[str(p) for p in java_files],
        ]
    else:
        javac_cmd = [
            args.javac,
            "-source",
            str(args.source),
            "-target",
            str(args.target),
            "-encoding",
            "UTF-8",
            "-d",
            str(classes_dir),
            *extra_javac,
            *[str(p) for p in java_files],
        ]

    p = _run_capture(javac_cmd)
    if p.returncode != 0:
        out = p.stdout or ""
        sys.stderr.write(out)
        if "no longer supported" in out.lower():
            sys.stderr.write(
                "\nHINT: Your javac is too new to target Java 7/6. "
                "This dx.jar is legacy and cannot process Java 8+ classfiles.\n"
                "Install JDK 8 and rerun with e.g.:\n"
                "  python3 test/build_dex.py --clean --javac /path/to/jdk8/bin/javac --mode source-target --source 1.7 --target 1.7\n"
            )
        return p.returncode

    dx_cmd = [
        "java",
        "-jar",
        str(dx_jar),
        "--dex",
        f"--output={dex_out}",
        str(classes_dir),
    ]

    _run(dx_cmd)

    print(dex_out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
