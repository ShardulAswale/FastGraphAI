def run_chain(message: str, stream_target) -> str:
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    full_reply = ""
    for chunk in response:
        content = chunk.choices[0].delta.content or ""
        full_reply += content
        stream_target.markdown(full_reply + "▌")  # ONLY temporary UI
    stream_target.markdown(full_reply)  # Final update
    return full_reply  # ONLY append this to the chat history!
