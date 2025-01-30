# DeepSeek LLM Interface Template


## Description
This template provides a simple local interface to interact with the DeepSeek R1 LLM model using the `mlx_lm` library. The backend is powered by a Flask app, while the frontend leverages Next.js with shadcn UI components.


## Features
- Lightweight local deployment
- Customizable prompts
- Easy extension for LLM (interface) exploration


## Installation
1. Clone the repository:
```
git clone https://github.com/seowoonam/llm-interface-setup
cd llm-interface-setup
```

2. Create and activate a virtual environment (optional):
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Run the flask app:
```
python app.py
```
2. Run the Next.js app in another terminal:
Make sure that you are in the virtual environment
```
npm install
```
```
cd lets-chat
npm run dev
```

## Notes
Ensure that `curl http://localhost:5000` works for verifying the connection.
Change `max_tokens: int = 256` in line 213 of `.venv/lib/python3.12/site-packages/mlx_lm/utils.py` to `max_tokens: int = 1024` if you want to increase your token.

## License
MIT License
