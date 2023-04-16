from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import numpy as np

# torch.device("cuda")

model = SentenceTransformer("all-MiniLM-L6-v2")

articles_df = pd.read_csv("../LDA/datasets/training_set.csv")
articles_df.head()
articles_df = articles_df.reset_index().drop(columns="index")

articles_en_df = articles_df[articles_df["Lang1"] == "en"]

articles_list_1 = articles_en_df["Text1"].to_list()
articles_list_2 = articles_en_df["Text2"].to_list()
print(len(articles_list_1))
print(len(articles_list_2))


# Compute embeddings
embeddings_1 = model.encode(articles_list_1, convert_to_tensor=True)
embeddings_2 = model.encode(articles_list_2, convert_to_tensor=True)
print("done")

# Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.cos_sim(embeddings_1, embeddings_2)
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
            articles_list_1[i][:100], articles_list_2[j][:100], pair["score"]
        )
    )
