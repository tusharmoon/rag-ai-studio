# from langchain_mistralai import ChatMistralAI


# class AgenticChunker:
#     def __init__(self, llm=None):
#         self.chunks = []
#         self.llm = llm or ChatMistralAI(
#             model="mistral-small-latest",
#             temperature=0
#         )

#     def _find_relevant_chunk(self, proposition):
#         """
#         Ask the LLM which chunk the proposition belongs to
#         """
#         if len(self.chunks) == 0:
#             return None

#         chunk_descriptions = []

#         for i, chunk in enumerate(self.chunks):
#             text = "\n".join(chunk)
#             chunk_descriptions.append(f"Chunk {i}:\n{text}")

#         chunks_text = "\n\n".join(chunk_descriptions)

#         prompt = f"""
# You are grouping propositions into semantic topics.

# Existing Chunks:
# {chunks_text}

# New Proposition:
# {proposition}

# Which chunk should this belong to?

# Return ONLY the chunk number.
# If none fit, return NEW.
# """

#         response = self.llm.invoke(prompt).content.strip()

#         if response == "NEW":
#             return None

#         try:
#             return int(response)
#         except:
#             return None

#     def add_propositions(self, propositions):
#         for prop in propositions:

#             chunk_index = self._find_relevant_chunk(prop)

#             if chunk_index is None:
#                 self.chunks.append([prop])
#             else:
#                 self.chunks[chunk_index].append(prop)

#     def get_chunks(self):
#         return self.chunks

#     def pretty_print_chunks(self):

#         output = ""

#         for i, chunk in enumerate(self.chunks):

#             output += f"\nChunk {i+1}:\n"

#             for sentence in chunk:
#                 output += f" - {sentence}\n"

#         return output