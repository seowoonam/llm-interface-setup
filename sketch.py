from mlx_lm import load, generate

model, tokenizer = load("mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit")
#model, tokenizer = load("mistralai/Mistral-7B-Instruct-v0.2")

prompt = "Hello?"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    max_tokens: 1024
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
