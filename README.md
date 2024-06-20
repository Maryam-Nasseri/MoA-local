# MoA-local

## Introduction
This is a simplified agentic workflow process based on the Mixture of Agents (MoA) system by Wang et al. (2024). "Mixture-of-Agents Enhances Large Language Model Capabilities".
This demo is a 3-layer MoA with 4 open-source models of Qwen2, Qwen 1.5, Mixtral, and dbrx. Qwen2 acts as the aggregator in the final layer.

## Run MoA
1. Export your Together AI API key as an environment variable using `bash_profile` or `Zshrc` and update your shell with the new variable
2. `git clone` the MoA GitHub project `https://github.com/togethercomputer/MoA.git` into your project directory
3. `pip install -r requirements.txt` from the MoA directory
4. Run the Python file `bot.py`
