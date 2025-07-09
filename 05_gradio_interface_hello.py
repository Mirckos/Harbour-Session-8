import gradio as gr


def greet(name: str) -> str:
    return f"Hello, {name}!"


# Interactive interface
#   • fn: callable executed on submit
#   • inputs / outputs: simple text widgets
#   • title / description: shown above the UI

demo = gr.Interface(
    fn=greet,  # Python function to invoke
    inputs="text",  # single text input
    outputs="text",  # single text output
    title="Gradio Hello Demo",
    description="Enter your name to receive a greeting.",
)


if __name__ == "__main__":
    demo.launch(
        share=True,
        inbrowser=True,  # create public tunnel instantly
    )  # open a new browser tab automatically
