from Utils.getApiResponse import getApiResponse
from Utils.dbSaving import dbSaving
from datetime import datetime
import time

def main():
    json=getApiResponse()
    jsonData=json['DATA']['GENRE_LIST'][2]['CHNL_LIST']
    ranking=0

    for info in jsonData:
        # Data Mapping
        curTime=datetime.now().strftime("%Y-%m-%d %H:%M")
        chnlNo=info["CHNL_NO"]
        chnlName=info["CHNL_NM"]
        pgmName=info["TOP10_PGRM_NM"]
        pgmTm=info["TOP10_PRGM_TM"]
        pgmStart=info["TOP10_STRT_TM"]
        pgmFinish=info["TOP10_FIN_TM"]
        rating=info["TOP10_RATING"]
        ranking+=1
        pgmDuration=datetime.strptime(pgmFinish,"%H:%M")-datetime.strptime(pgmStart,"%H:%M")

        # Saving it to DB
        dbSaving(curTime,chnlNo,chnlName,pgmName,pgmTm,pgmStart,pgmFinish,rating,ranking,pgmDuration)

if __name__=="__main__":
    while True:
        main()
        time.sleep(60)