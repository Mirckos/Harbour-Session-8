import gradio as gr


def reverse(text: str) -> str:
    """Return the input string reversed."""
    return text[::-1]


# Interface definition: single text input/output bound to `reverse`
demo = gr.Interface(
    fn=reverse,  # callable executed when user submits
    inputs="text",
    outputs="text",
    title="Password‑Protected Reverse",
)


if __name__ == "__main__":
    # Launch with basic authentication
    app, _, url = demo.launch(
        auth=("admin", "pass1234"),  # username / password combo
        share=True,  # expose a public URL via ngrok
        inline=False,  # open in a separate tab
    )
