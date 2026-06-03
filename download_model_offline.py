import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from sentence_transformers import SentenceTransformer
import time

# 带重试的下载
for i in range(3):
    try:
        print(f"Attempt {i+1} to download model...")
        model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        # 保存到本地
        model.save('./local_model_cache')
        print("Model downloaded and saved to ./local_model_cache")
        break
    except Exception as e:
        print(f"Attempt {i+1} failed: {e}")
        time.sleep(5)