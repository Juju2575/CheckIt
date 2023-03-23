from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import numpy as np

# torch.device("cuda")

model = SentenceTransformer("all-MiniLM-L6-v2")

articles_df = pd.read_csv("../LDA/datasets/news-article-categories.csv")
articles_df.head(5)
articles_df = articles_df.reset_index().drop(columns="index")


sentences = articles_df["title"].to_list()
print(len(sentences))


# Compute embeddings
embeddings = model.encode(sentences[:300], convert_to_tensor=True)
print("done")

# Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.cos_sim(embeddings, embeddings)
print("encoded")
cosine_scores_np = cosine_scores.numpy()
print("converted")

# Find the pairs with the highest cosine similarity scores
n = cosine_scores_np.shape()[0]
pairs = np.zeros(n * n)
for i in range(n - 1):
    for j in range(i + 1, n):
        pairs[i + n * j] = (i, j, cosine_scores_np[i, j])

print(cosine_scores.shape())

print("just sorting")

# Sort scores in decreasing order
pairs = sorted(pairs, key=lambda x: x["score"], reverse=True)

for pair in pairs[0:10]:
    i, j = pair["index"]
    print(
        "{} \t\t {} \t\t Score: {:.4f}".format(
            sentences[i], sentences[j], pair["score"]
        )
    )
