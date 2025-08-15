def process_pdf_text(text, chunk_size=300):
    chunks = []
    current_chunk = ""
    for line in text.split('\n'):
        if len(current_chunk) + len(line) < chunk_size:
            current_chunk += line + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = line + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks