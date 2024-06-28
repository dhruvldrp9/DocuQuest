import torch
from transformers import pipeline
from helper_get_context import get_context


class LLM():
    def __init__(self):
        self.pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto",  return_full_text=False)

    def _create_prompt(self, question, docs):
        context = docs
        prompt_start = "Context information is below. \n####\n" + "CONTEXT: "
        prompt_end = f"\n\nGiven the context information and not prior knowledge, answer the question: {question}.if context information is not relevant please return no context avaliable. \n####\nANSWER: "
        prompt = prompt_start + f"{context} \n####\n" + prompt_end
        return prompt

    def get_response(self, question, docs):
        prompt = self._create_prompt(question, docs)
        messages = [
            {
                "role": "chatbot",
                "content": """Act as an experienced goverment policies report analyst.
                    Please follow these instructions.
                    if you found relavent context to question, answer the question only, else tell the user there is no relevant context found. and don't generate whole prompt""",
            },
            {"role": "user", "content": f"""{prompt}"""},
        ]
        return messages


    def get_answer(self, doc, question):
        messages = self.get_response(question, doc)

        prompt = self.pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.9, top_k=50, top_p=0.95)
        result = outputs[0]["generated_text"]
        return result

def api_ans(question):
    llm = LLM()
    doc = get_context(question)
    result = llm.get_answer(doc, question)
    return result