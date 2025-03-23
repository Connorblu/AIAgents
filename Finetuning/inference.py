from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "lora_music_model4", # YOUR MODEL YOU USED FOR TRAINING
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True,
)
FastLanguageModel.for_inference(model) # Enable native 2x faster inference

#This ensures that we are using the correct chat template for our chosen model
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "llama-3.1",
)

messages = [
    {"role": "user", "content": "Recommend me a song. It should be grunge, post-grunge,and/or alternative metal. "},
]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize = True,
    add_generation_prompt = True, # Must add for generation
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(input_ids = inputs, streamer = text_streamer, max_new_tokens = 128,
                   use_cache = True, temperature = 1.5, min_p = 0.1)