import subprocess
import sys

if len(sys.argv) < 2:
    print("No question provided")
    sys.exit()

question = sys.argv[1]

cmd = [
    "/data/data/com.termux/files/home/llama.cpp/build/bin/llama-cli",
    "-hf",
    "Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q4_K_M",
    "-p",
    question,
    "-n",
    "80",
    "-no-cnv",
    "-st",
    "--no-display-prompt"
]

process = subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

output = []

for line in process.stdout:
    output.append(line)

process.wait()

print("".join(output))
