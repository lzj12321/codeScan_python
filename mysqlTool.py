import pymysql
from YamlTool import Yaml_Tool
from codeAndBoxState import CodeState,BoxState,InputDataState
from PyQt5.QtCore import *
from time import sleep

class MysqlTool:
    def __init__(self):
        self.yamlTool=Yaml_Tool()
        self.params=self.yamlTool.getValue('deviceParam.yaml')['mysql']
        self._connectState=self.connectServer()
        self._deviceSerial=self.yamlTool.getValue('deviceParam.yaml')['deviceParam']['deviceSerial']
        pass

    def connectServer(self):
        try:
            self.db = pymysql.connect(self.params['ip'],
                                  self.params['user'],
                                  self.params['password'],
                                  self.params['database'])
            self.cursor = self.db.cursor()
            return True
        except:
            return False

    def executeSql(self,sql):
        if not self._connectState:
            return False
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            # self.db.rollback()
            return False
        pass

    def connectState(self):
        return self._connectState

    def checkDuplicateCode(self, data):
        # yearTime=QDateTime.currentDateTime().toString('yyyy')
        timeSql="select DATE_FORMAT(NOW(),'%Y-%m');"
        if not self.executeSql(timeSql):
            return True
        yearTime = str(self.cursor.fetchone()[0])

        if data['isCommonPackMode']:
            sql="select 1 from packedData where code=\'"+data['code']+"\' and packFlag='PACKED_CODE'"\
                +" and model=\'"+data['model']+"\' and weekNumber=\'"\
                +str(data['weekNum'])+"\' and time1 like \'"+yearTime+"%"+"\' limit 1;"
            # print('check duplicate sql:' + sql)
        else:
            sql = "select 1 from CodeRetest where Model=\'" + data['model'] + "\' and Code=\'" + data[
                'code'] + "\' and LFP='1';"
            print('check duplicate sql:' + sql)
        if not self.executeSql(sql):
            return True
        # print('checkDuplicateCode self.cursor.rowcount:' + str(self.cursor.rowcount))
        if self.cursor.rowcount == 0:
            return False
        else:
            return True
        pass

    def checkUnTestCode(self, data):
        # return False
        if data['isCommonPackMode']:
            sql = "select 1 from TestOkCode where code=\'" + data['code'] + "\' limit 1;"
        else:
            sql = "select 1 from CodeRetest where Model=\'" + data['model'] + "\' and Code=\'" + data[
                'code'] + "\' and LF='1';"
            print('check untest sql:' + sql)
        # print('checkUnTestCode sql:' + sql)
        if not self.executeSql(sql):
            return True
        if self.cursor.rowcount == 0:
            return True
        else:
            return False
        pass

    def savePackData(self,data,checkResult):
        timeSql="select DATE_FORMAT(NOW(),'%Y-%m-%d %H:%i:%S');"
        if not self.executeSql(timeSql):
            return False
        _time = str(self.cursor.fetchone()[0])
        date=_time.split(' ')[0]
        time=_time.split(' ')[1]
        codeState=""
        if checkResult == CodeState.PACKED_POINT:
            codeState = 'PACKED_CODE'
        elif checkResult == CodeState.ERROR_CODE_LENGTH:
            codeState = 'ERROR_LENGTH_CODE'
        elif checkResult == CodeState.ERROR_FIXED_CODE_POINT:
            codeState = 'ERROR_FIXED_CODE'
        elif checkResult == CodeState.UNTEST_CODE_POINT:
            codeState = 'UNTEST_CODE'
        elif checkResult == CodeState.DUPLICATE_CODE_POINT:
            codeState = 'DUPLICATE_CODE'
        elif checkResult == CodeState.ERROR_WEEKNUM_CODE_POINT:
            codeState = 'ERROR_WEEKNUM_CODE'

        sql = "insert into packedData(model,code,time1,time2,boxNumber," \
              "weekNumber,packedNum,maxPackNum,packFlag,serialNumber) " \
                "values(\'" + data['model'] + "\',\'" + data['code'] + "\',\'" + \
              date + "\',\'" + time + "\',\'" + data['boxNumber'] + "\',\'"\
              +str(data['weekNum']) + "\'," + str(data['packedNum']) + "," +\
              str(data['maxPackNum']) \
                + ",\'" + codeState + "\',\'" + self._deviceSerial + "\');"
        #print(sql)

        if not data['isCommonPackMode'] and data['codeState']==CodeState.PACKED_POINT:
            time=QDateTime.currentDateTime().toString('yyyyMMdd-hh:mm:ss')
            _sql="update CodeRetest set LFP='1' Time_I=\'"+time+"\' where Model=\'"\
                 + data['model'] + "\' and Code=\'" + data[
                'code'] + "\';"
            self.executeSql(_sql)
            # print(_sql)
        else:
            pass

        if self.executeSql(sql):
            sleep(0.1) 
            #############check the data is success save to server############
            _checkSql='select 1 from packedData where model=\''+data['model']+'\' and \
                        code=\''+data['code']+'\' and \
                        boxNumber=\''+data['boxNumber']+'\' and \
                        serialNumber=\''+self._deviceSerial+'\' and \
                        time1=\''+date+'\' and time2=\''+time+'\';'
            # print(_checkSql)
            if not self.executeSql(_checkSql):
                return False
            # print("check result:"+str(self.cursor.rowcount))
            if self.cursor.rowcount == 0:
                return False
            return True
        else:
            return False
        return True
        pass

    def checkDuplicateBoxNumber(self,data):
        timeSql="select DATE_FORMAT(NOW(),'%Y-%m');"
        if not self.executeSql(timeSql):
            return BoxState.DUPLICATE_BOX_NUMBER, 0
        date = str(self.cursor.fetchone()[0])
        sql = "select 1 from packedData where boxNumber=\'" + data['boxNumber']\
              + "\' and model=\'" + data['model'] + "\' and time1 like \'" + date + "%" + \
              "\' and packFlag='PACKED_CODE' limit 1;"
        # print('checkDuplicateBoxNumberSql:'+sql)
        if not self.executeSql(sql):
            return BoxState.DUPLICATE_BOX_NUMBER, 0
        if self.cursor.rowcount == 0:
            return BoxState.VALID_BOX_NUMBER, 0
        elif self.cursor.rowcount != 0:
            _sql = "select maxPackNum from packedData where boxNumber =\'" \
                   + data['boxNumber'] + "\' and model=\'" + data['model'] + "\' and time1 like \'" \
                   + date + "%" + "\' and packFlag='PACKED_CODE' limit 1;"
            __sql = "select max(packedNum) from packedData where boxNumber =\'" \
                   + data['boxNumber'] + "\' and model=\'" + data['model'] + "\' and time1 like \'" \
                   + date + "%" + "\' and packFlag='PACKED_CODE' limit 1;"

            # print(_sql)
            # print(__sql)
            if not self.executeSql(_sql):
                return BoxState.DUPLICATE_BOX_NUMBER, 0
            _result = self.cursor.fetchone()
            maxPackAdapterNum = _result[0]

            if not self.executeSql(__sql):
                return BoxState.DUPLICATE_BOX_NUMBER, 0
            __result = self.cursor.fetchone()
            packedAdapterNum= __result[0]

            if packedAdapterNum<maxPackAdapterNum:
                return BoxState.UNFILLED_BOX_NUMBER, packedAdapterNum
            else:
                return BoxState.DUPLICATE_BOX_NUMBER, 0
        pass

    def getServerTime(self):
        sql = "select current_timestamp;"
        self.executeSql(sql)
        result=str(self.cursor.fetchone()[0])
        date=result.split(' ')[0]
        pass

    def getDayPackedData(self, data):
        # self.getServerTime()
        data['dayPackedAdapterNum'] = 0
        data['dayPackedBoxNum'] = 0
        data['dayErrorCodeNum'] = 0
        data['dayUntestCodeNum'] = 0
        data['dayDuplicateCodeNum'] = 0

        timeSql="select DATE_FORMAT(NOW(),'%Y-%m-%d');"
        if self.executeSql(timeSql):
            date = str(self.cursor.fetchone()[0])
        else:
            return data
        # print('date:'+date)
        # date=QDateTime.currentDateTime().toString('yyyy-MM-dd')

        getDayPackedBoxNumSql="select count(distinct boxNumber) from packedData where time1=\'" \
                           + date + "\' and packFlag='PACKED_CODE' and packedNum=maxPackNum and serialNumber=\'" \
                           + self._deviceSerial + "\';"
        # print('getPackedBoxNumSql sql:' + getDayPackedBoxNumSql)
        if self.executeSql(getDayPackedBoxNumSql):
            result=self.cursor.fetchone()
            data['dayPackedBoxNum']=result[0]
        # print('dayPackedBoxNum:'+str(_data['dayPackedBoxNum']))

        getDayPackedAdapterNumSql="select count(code) from packedData where time1=\'" \
                           + date + "\' and packFlag='PACKED_CODE'  and serialNumber=\'" \
                           + self._deviceSerial + "\';"
        # print('getDayPackedAdapterNumSql sql:' + getDayPackedAdapterNumSql)
        if self.executeSql(getDayPackedAdapterNumSql):
            result=self.cursor.fetchone()
            data['dayPackedAdapterNum']=result[0]
        # print('dayPackedAdapterNum:'+str(_data['dayPackedAdapterNum']))

        getDayErrorCodeNumSql="select count(code) from packedData where time1=\'" \
                           + date + "\' and packFlag in('ERROR_LENGTH_CODE','ERROR_FIXED_CODE','ERROR_WEEKNUM_CODE')\
                                and serialNumber=\'" +self._deviceSerial + "\';"
        # print('getDayErrorCodeNumSql sql:' + getDayErrorCodeNumSql)
        if self.executeSql(getDayErrorCodeNumSql):
            result=self.cursor.fetchone()
            data['dayErrorCodeNum']=result[0]
        # print('dayErrorCodeNum:'+str(_data['dayErrorCodeNum']))

        getDayUntestCodeNumSql="select count(code) from packedData where time1=\'" \
                           + date + "\' and packFlag='UNTEST_CODE'  and serialNumber=\'" \
                           + self._deviceSerial + "\';"
        # print('getDayUntestCodeNumSql sql:' + getDayUntestCodeNumSql)
        if self.executeSql(getDayUntestCodeNumSql):
            result=self.cursor.fetchone()
            data['dayUntestCodeNum']=result[0]
        # print('dayUntestCodeNum:'+str(_data['dayUntestCodeNum']))

        getDayDuplicateCodeNumSql="select count(code) from packedData where time1=\'" \
                           + date + "\' and packFlag='DUPLICATE_CODE'  and serialNumber=\'" \
                           + self._deviceSerial + "\';"
        # print('getDayDuplicateCodeNumSql sql:' + getDayDuplicateCodeNumSql)
        if self.executeSql(getDayDuplicateCodeNumSql):
            result=self.cursor.fetchone()
            data['dayDuplicateCodeNum'] = result[0]
        # print('dayDuplicateCodeNum:'+str(_data['dayDuplicateCodeNum']))
        return data

    def updateCodeBoxNumber(self,data):
        _sql = "update CodeRetest set m1=\'" + data['boxNumber'] + "\' where Model=\'" \
               + data['model'] + "\' and Code=\'" + data['code'] + "\';"
        # print('update boxNumber '+_sql)
        self.executeSql(_sql)
        pass

    def clearErrorCodeRecord(self):
        _clearSql="delete from packedData where packFlag !=\'PACKED_CODE\' and serialNumber=\'"+self._deviceSerial+"\';"
        # print(_clearSql)
        self.executeSql(_clearSql)
        pass


