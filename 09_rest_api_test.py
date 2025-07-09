import asyncio

from gradio_client import Client

# Endpoint exposed by `demo.launch(share=True)`
URL = "https://f54b4cbf25d9dddb93.gradio.live"  # replace with your own tunnel URL
client = Client(URL)

# 1️⃣ List all available REST endpoints for the app
print(client.view_api())  # shows routes and their input/output signatures

# 2️⃣ Synchronous call
resp = client.predict(
    "You are a fool!",  # first positional argument to the endpoint
    api_name="/predict",  # omit if the app exposes a single endpoint
)
print(resp)  # e.g. {'toxic': 0.97, 'insult': 0.88, ...}


# 3️⃣ Asynchronous call
async def run_async() -> None:
    # Fire‑and‑forget submission; returns a Job object immediately
    job = client.submit("I'll beat you!", api_name="/predict")

    # Wait for result in a background thread so the event loop stays free
    result = await asyncio.to_thread(job.result)
    print(result)


asyncio.run(run_async())
