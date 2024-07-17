from getApiResponse import getApiResponse
from dbSaving import dbSaving
from datetime import datetime
import pymysql

def main():
    json=getApiResponse()
    jsonData=json['DATA']['GENRE_LIST'][2]['CHNL_LIST']
    ranking=0
    dataStr=""

    for info in jsonData:
        curTime=datetime.now().strftime("%Y-%m-%d %H:%M")
        chnlNo=info["CHNL_NO"]
        chnlName=info["CHNL_NM"]
        pgmName=info["TOP10_PGRM_NM"]
        pgmTm=info["TOP10_PRGM_TM"]
        pgmStart=info["TOP10_STRT_TM"]
        pgmFinish=info["TOP10_FIN_TM"]
        rating=info["TOP10_RATING"]
        ranking+=1
        pgmDuration=str(datetime.strptime(pgmFinish,"%H:%M")-datetime.strptime(pgmStart,"%H:%M"))[:4]
        dbSaving(curTime,chnlNo,chnlName,pgmName,pgmTm,pgmStart,pgmFinish,rating,ranking,pgmDuration)

if __name__=="__main__":
    main()