from functions.firestore import getNumArticles
from functions.graphing import makeHisto
from functions.sendEmail import sendEmailWithAttachment

figureFileName = 'articleDistroHisto.png'

articleNumList = getNumArticles()
makeHisto(articleNumList, figureFileName)

### Email Params ###
fromEmailFriendly = "Featured Article Distribution Histogram"
recipientList = ['josh.simmons@livingspaces.com', 'pete.franco@livingspaces.com',
                 'brandon.nguyen@livingspaces.com', 'leo.garcia@livingspaces.com']
subject = "Featured Article Distribution Histogram"
bodyString = "Please find attached a histogram showing current distribution of featured articles."
localFile = figureFileName
####################

sendEmailWithAttachment(fromEmailFriendly, recipientList,
                        subject, bodyString, localFile)
