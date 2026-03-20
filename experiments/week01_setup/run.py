import json
import random
from pathlib import Path

import numpy as np
import torch
from transformer_lens import HookedTransformer


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def main() -> None:
    config_path = Path("experiments/week01_setup/config.yaml")
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("PyYAML is required. Install with: pip install pyyaml") from exc

    config = yaml.safe_load(config_path.read_text())
    seed = int(config.get("seed", 42))
    model_name = config.get("model_name", "gpt2")
    prompt = config.get("prompt", "Hello world")
    hook_name = config.get("target_hook", "blocks.5.hook_resid_post")
    output_path = Path(config.get("output_path", "experiments/week01_setup/results.json"))

    set_seed(seed)
    model = HookedTransformer.from_pretrained(model_name)
    tokens = model.to_tokens(prompt)
    _, cache = model.run_with_cache(tokens)

    resid = cache[hook_name]
    resid_cpu = resid.detach().float().cpu()

    payload = {
        "model_name": model_name,
        "seed": seed,
        "prompt": prompt,
        "hook_name": hook_name,
        "shape": list(resid_cpu.shape),
        "resid_mean": float(resid_cpu.mean().item()),
        "resid_std": float(resid_cpu.std().item()),
        "resid_l2": float(torch.linalg.vector_norm(resid_cpu).item()),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
