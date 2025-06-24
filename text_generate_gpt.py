# GENERATIVE-TEXT-MODEL
!pip install transformers
from transformers import pipeline, set_seed
pip install huggingface_hub[hf_xet]
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
topic = "The future of artificial intelligence in healthcare"
generated = generator(topic, max_length=1000, num_return_sequences=2)
print(generated[0]['generated_text'])
