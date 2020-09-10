import sqlite3

class SqliteTool:
    def __init__(self):
        pass

    def getPackData(self):
        _data={}
        _conn=sqlite3.connect("pack.db")
        _cursor=_conn.cursor()
        _result=_cursor.execute('select code,layerNumEachBox,adapterNumEachPoint,numAdapterEachLine,pointNumEachLine,model,\
                                        boxNumber,weekNum,weekNumPosition,lineNumEachLayer,adapterNumEachLayer,packedNum,\
                                        maxPackNum,fixCode,codeLength,boxNumberLength,isCheckBoxNumberLength,isCheckCodeLength,\
                                        isCheckFixCode,isCheckUntest,isCheckDuplicate,isCheckWeekNum,isCommonPackMode,codeRange from packData')
        for _row in _result:
            _data['code']=_row[0]
            _data['layerNumEachBox']=_row[1]
            _data['adapterNumEachPoint']=_row[2]
            _data['numAdapterEachLine']=_row[3]
            _data['pointNumEachLine']=_row[4]
            _data['model']=_row[5]
            _data['boxNumber']=_row[6]
            _data['weekNum']=_row[7]
            _data['weekNumPosition']=_row[8]
            _data['lineNumEachLayer']=_row[9]
            _data['adapterNumEachLayer']=_row[10]
            _data['packedNum']=_row[11]
            _data['maxPackNum']=_row[12]
            _data['fixCode']=_row[13]
            _data['codeLength']=_row[14]
            _data['boxNumberLength']=_row[15]
            _data['isCheckBoxNumberLength']=bool(_row[16])
            _data['isCheckCodeLength']=bool(_row[17])
            _data['isCheckFixCode']=bool(_row[18])
            _data['isCheckUntest']=bool(_row[19])
            _data['isCheckDuplicate']=bool(_row[20])
            _data['isCheckWeekNum']=bool(_row[21])
            _data['isCommonPackMode']=bool(_row[22])
            _data['codeRange']=_row[23]

            _data['dayPackedAdapterNum']=0
            _data['dayPackedBoxNum']=0
            _data['dayErrorCodeNum']=0
            _data['dayUntestCodeNum']=0
            _data['dayDuplicateCodeNum']=0
        _cursor.close()
        _conn.close()

        # print('connect sql success')
        # print(_data)
        return _data

    def savePackData(self,_data):
        # print("save data to local")
        _conn=sqlite3.connect("pack.db")
        _cursor=_conn.cursor()
        _updateSql='update packData set \
            code=\''+_data['code']+'\',\
            layerNumEachBox='+str(_data['layerNumEachBox'])+',\
            adapterNumEachPoint='+str(_data['adapterNumEachPoint'])+',\
            numAdapterEachLine='+str(_data['numAdapterEachLine'])+',\
            pointNumEachLine='+str(_data['pointNumEachLine'])+',\
            model=\''+_data['model']+'\',\
            boxNumber='+str(_data['boxNumber'])+',\
            weekNum='+str(_data['weekNum'])+',\
            weekNumPosition='+str(_data['weekNumPosition'])+',\
            lineNumEachLayer='+str(_data['lineNumEachLayer'])+',\
            adapterNumEachLayer='+str(_data['adapterNumEachLayer'])+',\
            packedNum='+str(_data['packedNum'])+',\
            maxPackNum='+str(_data['maxPackNum'])+',\
            fixCode=\''+_data['fixCode']+'\',\
            codeLength='+str(_data['codeLength'])+',\
            boxNumberLength='+str(_data['boxNumberLength'])+',\
            isCheckBoxNumberLength='+str(int(_data['isCheckBoxNumberLength']))+',\
            isCheckCodeLength='+str(int(_data['isCheckCodeLength']))+',\
            isCheckFixCode='+str(int(_data['isCheckFixCode']))+',\
            isCheckUntest='+str(int(_data['isCheckUntest']))+',\
            isCheckDuplicate='+str(int(_data['isCheckDuplicate']))+',\
            isCheckWeekNum='+str(int(_data['isCheckWeekNum']))+',\
            isCommonPackMode='+str(int(_data['isCommonPackMode']))+',\
            codeRange='+str(_data['codeRange'])+';'
        # print(_updateSql)
        _cursor.execute(_updateSql)
        _conn.commit()
        _cursor.close()
        _conn.close()
        pass



if __name__=='__main__':
    testSqlite=SqliteTool()
    data=testSqlite.getPackData()
    print(data)