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
        "ls-restful-api-scrape").where("productStatus", "==", "Active").where("inStock", "==", True).stream()

    print('Fetching all Active SKUs...')

    holderDict = {}

    for doc in tqdm(docs):
        if doc.to_dict()['hardKitComponent'] != 'yes':
            holderDict[doc.id] = doc.to_dict()

    for item in holderDict.keys():
        allDocs[item] = len(
            list(filter(None, holderDict[item]['featuredArticles'].split(','))))

    numArticles = []

    for doc in allDocs:
        numArticles.append(allDocs[doc])

    return(numArticles)
