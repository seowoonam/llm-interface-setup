"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);
    try {
      const res = await fetch("http://localhost:8080/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      setResponse(data.reply || "No response received.");
    } catch (error) {
      setResponse("Error connecting to the server.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Chat Interface</h1>
      <div className="flex gap-2 mb-4">
        <Input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
        />
        <Button onClick={handleSendMessage} disabled={loading}>
          {loading ? "Sending..." : "Send"}
        </Button>
      </div>
      {response && (
        <div className="mt-4 p-2 border rounded-md bg-gray-100">
          <strong>Response:</strong> {response}
        </div>
      )}
    </div>
  );
}
