class AIClient:
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

        if not api_key:
            raise ValueError("API key is required.")

    def generate(self, prompt):
        print(f"Sending prompt to {self.model}...")

        return {
            "status": "success",
            "model": self.model,
            "prompt": prompt,
            "response": "This is a simulated AI response."
        }

    def summarize(self, text):
        if not text:
            return {
                "status": "error",
                "message": "Text cannot be empty."
            }

        return {
            "status": "success",
            "summary": text[:50] + "..."
        }


if __name__ == '__main__':
    client = AIClient(api_key="your-api-key")
    print(client.generate("Explain Python classes."))
    print(
        client.summarize(
            "Python is a popular programming language used for web development, "
            "data science, and artificial intelligence."
        )
    )
