from google.cloud import firestore
from tqdm import tqdm


def getNumArticles():
    '''
    Takes no arguments.
    Returns an object of objects with SKU keys and values containing the number of featured articles
    '''
    print('Connecting to Firestore')
    db = firestore.Client()

    allDocs = {}

    docs = db.collection(
        "ls-restful-api-scrape").where("productStatus", "==", "Active").stream()

    print('Fetching all Active SKUs...')

    for doc in tqdm(docs):
        allDocs[doc.id] = len(
            list(filter(None, doc.to_dict()['featuredArticles'].split(','))))

    return(allDocs)
