import os
import subprocess
import shutil

# Paths to sources
SRC_CPP = [
    "src/cpu/interpreter.cpp",
    "src/compiler/avion_compiler.cpp",
    "src/bytecode/generator.cpp",
    "src/bytecode/opcodes.cpp"
]
SRC_HEADERS = [
    "include/cpu/interpreter.hpp",
    "include/compiler/avion_compiler.hpp",
    "include/bytecode/opcodes.hpp"
]
TUI_SCRIPT = "tools/repl/avion_repl.py"
OUTPUT_DIR = "dist"
EXEC_NAME = "avion_runtime"

# Flags for C++ compiler
CXX = "g++"
CXX_FLAGS = "-O3 -std=c++20 -Wall -Wextra -march=native"

# Entry point for integration
MAIN_CPP = "src/main.cpp"

# Unified Avion Launch Wrapper
AVION_LAUNCHER = f"""
#!/bin/bash
echo "[AVION RUNTIME] :: Linking bytecode ↔ REPL ↔ CPU Engine ↔ Compiler ..."
python3 {TUI_SCRIPT} &
./{EXEC_NAME}
"""

def compile_cpp():
    print("🛠️  Compiling C++ core...")
    cpp_command = f"{CXX} {CXX_FLAGS} {' '.join(SRC_CPP)} {MAIN_CPP} -o {OUTPUT_DIR}/{EXEC_NAME}"
    result = subprocess.run(cpp_command, shell=True)
    if result.returncode != 0:
        print("❌ Compilation failed.")
        exit(1)
    print("✅ C++ core compiled.")

def setup_output():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    shutil.copy(TUI_SCRIPT, OUTPUT_DIR + "/avion_repl.py")
    with open(OUTPUT_DIR + "/launch_avion.sh", "w") as launcher:
        launcher.write(AVION_LAUNCHER)
    os.chmod(OUTPUT_DIR + "/launch_avion.sh", 0o755)

def build():
    print("🚀 Building Avion full runtime...")
    setup_output()
    compile_cpp()
    print("✅ Avion runtime is ready in 'dist/' directory.")
    print("👉 Run with: ./dist/launch_avion.sh")

if __name__ == "__main__":
    build()
