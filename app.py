from flask import Flask, request, jsonify
from flask_cors import CORS
from mlx_lm import load, generate

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the model and tokenizer once during startup
model, tokenizer = load("mlx-community/DeepSeek-R1-Distill-Qwen-1.5B-4bit")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "").strip()
        
        if not user_input:
            return jsonify({"reply": "Please enter a message."}), 400

        # Apply template and generate response
        prompt = tokenizer.apply_chat_template(
            [{"role": "user", "content": user_input}],
            add_generation_prompt=True
        )
        
        response = generate(model, tokenizer, prompt=prompt, verbose=False)

        return jsonify({"reply": response.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8080)
