import getApiResponse
from datetime import datetime
import os, glob, json
from dateutil.relativedelta import relativedelta

def fileMaking(fileName):
    if not os.path.isfile(fileName): #오늘 날짜 파일 없으면 만들기
        twoMonthAgo = str((datetime.now() - relativedelta(months=3)).date())[:-3] #세달 전 데이터는 다 삭제
        for oldFile in glob.glob("./data/"+twoMonthAgo+"*"):
            os.remove(oldFile)
        with open(fileName,'w') as f:
            json.dump({},f)

def isKeyPresent(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    return True

def fileWriting(fileName, data):
    with open(fileName,'r+',encoding='UTF-8') as jsonFile:
        log=json.load(jsonFile)
        if isKeyPresent(log,"data"):
            log["data"]+=[data]
        else:
            log["data"]=[data]
        jsonFile.seek(0)
        jsonFile.truncate()
        json.dump(log,jsonFile,ensure_ascii=False,indent=4)

def dataSaving():
    now=datetime.now()
    fileName="./data/"+str(now.date())+".json"
    fileMaking(fileName)

    data = {
        "time": str(now.time()),
        "channels": []
    }
    response=getApiResponse.getApiResponse()
    channelCnt=int(response["DATA"]["GENRE_LIST"][2]["CHNL_CNT"]) #실시간 인기채널 수
    ChannelList=response["DATA"]["GENRE_LIST"][2]["CHNL_LIST"] #인기채널 리스트
    for i in range(channelCnt):
        channelData = {
            "channelNum": int(ChannelList[i]["CHNL_NO"]),
            "channelName": ChannelList[i]["CHNL_NM"],
            "channelRating": ChannelList[i]["TOP10_RATING"],
            "pgmName": ChannelList[i]["TOP10_PGRM_NM"],
            "channelRanking": i + 1            
        }
        
        data["channels"].append(channelData)
        print(channelData["channelNum"], channelData["channelName"], ":", channelData["channelRating"])
    
    fileWriting(fileName,data)

if __name__=="__main__":
    dataSaving()