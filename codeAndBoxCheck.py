import sys
from codeAndBoxState import CodeState,BoxState,InputDataState
from mysqlTool import MysqlTool
from YamlTool import Yaml_Tool
from sqliteTool import SqliteTool

class CodeAndBoxCheck:

    def __init__(self):
        self.mysqlTool=MysqlTool()
        self.yamlTool=Yaml_Tool()
        self.sqliteTool=SqliteTool()
        pass

    def checkBoxNumber(self, data):
        if data['isCheckBoxNumberLength'] and len(data['boxNumber'])!=int(data['boxNumberLength']):
            return BoxState.UNDEFINED_BOX_NUMBER,0
        return self.mysqlTool.checkDuplicateBoxNumber(data)
        pass

    def checkCodeValidity(self,data):
        checkResult = CodeState.PACKED_POINT
        if data['isCheckCodeLength'] and data['codeLength'] != len(data['code']):
            checkResult = CodeState.ERROR_CODE_LENGTH
        elif data['isCheckFixCode'] and self.checkFixCode(data):
            checkResult = CodeState.ERROR_FIXED_CODE_POINT
        elif data['isCheckUntest'] and self.mysqlTool.checkUnTestCode(data):
            checkResult = CodeState.UNTEST_CODE_POINT
        elif data['isCheckDuplicate'] and self.mysqlTool.checkDuplicateCode(data):
            checkResult = CodeState.DUPLICATE_CODE_POINT
        elif data['isCheckWeekNum'] and self.checkWeekNum(data):
            checkResult = CodeState.ERROR_WEEKNUM_CODE_POINT
        return checkResult
        pass

    def savePackedDataToServer(self, data,checkResult):
        return self.mysqlTool.savePackData(data,checkResult)
        pass

    def checkWeekNum(self, data):
        if str(data['weekNum']) in data['code']:
            return False
        else:
            return True
        return False
        pass

    def checkFixCode(self,data):
        if data['fixCode'] in data['code']:
            return False
        else:
            return True
        return False
        pass

    def preProcessCodeRange(self,data):
        pass

    def saveDataToLocal(self,data):
        self.sqliteTool.savePackData(data)
        # self.yamlTool.saveParam("configure.yaml",data)

    def loadPackData(self):
        # data=self.yamlTool.getValue('configure.yaml')
        data=self.sqliteTool.getPackData()
        # print(data)
        return data
        pass

    def savePackData(self,data):
        self.yamlTool.saveParam('configure.yaml',data)

    def loadDayPackedData(self,data):
        return self.mysqlTool.getDayPackedData(data)
        pass

    def checkInputDataIsValid(self,data):
        if not data["isCommonPackMode"]:
            if data['weekNumPosition'] == 0 or data['model'] == '' or data['boxNumber'] == '' or \
                    data['weekNum'] == 0 or data["maxPackNum"] == 0 or data['maxPackNum']>22 or data['codeRange']=='':
                return InputDataState.INPUTDATA_INVALID
        elif data['weekNumPosition'] == 0 or data['model'] == '' or data['boxNumber'] == '' or \
            int(data['weekNum']) == 0 or data['lineNumEachLayer'] == 0 or data['layerNumEachBox'] == 0 \
                or data['pointNumEachLine'] == 0 or data['adapterNumEachPoint'] == 0:
            return InputDataState.INPUTDATA_INVALID
        return InputDataState.INPUTDATA_VALID
        pass

    def mysqlConnectState(self):
        return self.mysqlTool.connectState()

    def updateCodeBoxNumber(self,data):
        self.mysqlTool.updateCodeBoxNumber(data)

    def clearUntestCodeRecord(self):
        self.mysqlTool.clearErrorCodeRecord()

    def preProcessCode(self, code):
        if code == "":
            return code, False
        code = code.replace(' ', '')
        return code, True
