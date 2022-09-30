import os
import logging
import shutil

class folder:
    
    
  #  def __init__():
        #logging.basicConfig(filename="folder_log.txt", format="%(asctime)s %(message)s")
        #year = datetime.now().strftime("%Y")
        #month = datetime.now().strftime("%m-%Y")
        
            
    def createFolder(pPath):

        if not os.path.exists(pPath):
            try:
                os.mkdir(pPath)
            except OSError as error:
                logging.error(error)

    def delFolder(pTransfer):
        try:
            shutil.rmtree(pTransfer)
        except Exception as e:
            logging.error(e)
                    
            
    def transfer (pFile, pTransfer):
        
        try:
            shutil.copy(pFile, pTransfer)
            #shutil.make_archive(pTransfer,'zip', pTransfer)
        except Exception as e:
            logging.error(e)
            
    def compress(pTransfer):
        
        try:
            shutil.make_archive(pTransfer,'zip', pTransfer)
        except Exception as e:
            logging.error(e)
