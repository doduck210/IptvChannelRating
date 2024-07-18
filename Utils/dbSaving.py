import pymysql
import pymysql.cursors
import Utils.config as config

def dbSaving(CUR_TIME,CHNL_NO,CHNL_NAME,PGM_NM,PGM_TM,PGM_START_TIME,PGM_FIN_TIME,RATING,RANKING,PGM_DURATION):
    host=config.HOST
    port=config.PORT
    user=config.USER
    password=config.PASSWORD
    database=config.DATABASE

    conn=pymysql.connect(host=host,port=port,user=user,password=password,db=database,charset='utf8')
    curs=conn.cursor(pymysql.cursors.DictCursor)

    sql="INSERT INTO KTIPTV "
    sql+="(CUR_TIME,CHNL_NO,CHNL_NAME,PGM_NM,PGM_TM,PGM_START_TIME,PGM_FIN_TIME,RATING,RANKING,PGM_DURATION) "
    sql+="VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    curs.execute(sql,(CUR_TIME,CHNL_NO,CHNL_NAME,PGM_NM,PGM_TM,PGM_START_TIME,PGM_FIN_TIME,RATING,RANKING,PGM_DURATION))

    conn.commit()

    curs.close()
    conn.close()

if __name__ =="__main__":
    print("no test anymore")