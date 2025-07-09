import gradio as gr
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# ------------------ Model & Pipeline ------------------
MODEL = "unitary/toxic-bert"  # switch to another checkpoint if desired

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

pipe = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    return_all_scores=True,  # keep probabilities for all 5 labels
    function_to_apply="sigmoid",
)


# ------------------ Inference Function ------------------


def classify(text: str):
    """Return a mapping: {label: probability}."""
    scores = {d["label"]: round(d["score"], 3) for d in pipe(text)[0]}
    return scores


# ------------------ UI Definition ------------------
demo = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(lines=3, placeholder="Enter text..."),
    outputs=gr.Label(num_top_classes=5),
    title="Text Toxicity Classifier (BERT)",
    description="Multi‑label output: non‑toxic, insult, obscenity, threat, dangerous",
)


if __name__ == "__main__":
    # share=True instantly exposes a public HTTPS tunnel
    demo.launch(share=True)
