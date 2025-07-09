import gradio as gr

visitor_count = 0  # persists across requests while the process lives


def echo(msg, history, request: gr.Request):
    """Reverse the input, tag it with a counter and session‑id, and update history."""
    global visitor_count
    visitor_count += 1
    sid = request.session_hash  # unique per browser tab
    response = f"[{visitor_count}/{sid}] {msg[::-1]}"
    history.append((msg, response))
    return history, history


with gr.Blocks(title="Queue & State Demo") as demo:
    gr.Markdown("### Demonstration of **queue()**, global state and `gr.State`.")

    chat_history = gr.State([])  # conversation transcript across reruns

    with gr.Row():
        inp = gr.Textbox(label="Your message")
        btn = gr.Button("Send")

    out = gr.Chatbot(label="History")

    # Enqueue call to echo(); at most 3 executions can run concurrently
    btn.click(
        echo,
        inputs=[inp, chat_history],
        outputs=[out, chat_history],
        concurrency_limit=3,
    )

    demo.queue(max_size=20)  # maximum queued requests before rejecting


if __name__ == "__main__":
    demo.launch(
        inbrowser=True,
        share=True,  # expose a public URL via ngrok
        max_threads=20,  # cap worker threads Gradio can spawn
    )
