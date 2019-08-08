from google.cloud import firestore
from tqdm import tqdm


def getNumArticles():
    '''
    Takes no arguments.
    Returns a list of number of articles for all active skus
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

    numArticles=[]

    for doc in allDocs:
        numArticles.append(allDocs[doc])

    return(numArticles)
