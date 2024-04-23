#when both correct: 
import matplotlib.pyplot as plt

# Data
cosine = [7.9, 8.5, 7.5, 8.3, 7.8, 10, 7.6, 7.5, 8.4, 9.1]
chatgpt = [8, 8, 9, 7, 9, 10, 8, 8, 8, 8]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(cosine, label='Cosine Similarity')
plt.plot(chatgpt, label='ChatGPT')
plt.xlabel('Samples')
plt.ylabel('Score')
plt.title('Comparison of Cosine Similarity and ChatGPT Scores')
plt.legend()
plt.grid(True)
#plt.show()

cosine2 = [7.5, 6.7, 8.1, 8.5, 6.4, 5.5, 6.6, 7.8, 7.4, 7.2]
ChatGPT2 = [2, 2, 3, 3, 2, 2, 2, 3, 2, 2]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(cosine2, label='Cosine Similarity')
plt.plot(ChatGPT2, label='ChatGPT')
plt.xlabel('Samples')
plt.ylabel('Score')
plt.title('Comparison of Cosine Similarity and ChatGPT Scores')
plt.legend()
plt.grid(True)
plt.show()