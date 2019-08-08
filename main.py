from google.cloud import firestore
from tqdm import tqdm

db = firestore.Client()

allDocs = {}
docs = db.collection(
    "ls-restful-api-scrape").where("productStatus", "==", "Active").stream()
for doc in tqdm(docs):
    allDocs[doc.id] = len(
        list(filter(None, doc.to_dict()['featuredArticles'].split(','))))
