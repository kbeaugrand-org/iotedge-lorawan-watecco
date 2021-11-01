
import base64
import binascii
import json 

from typing import Optional
from fastapi import FastAPI
from datetime import datetime

from .Standard.srcWatteco.Decoding_Functions import Decoding_JSON, version
from .Batch import br_uncompress
from .Batch.br_uncompress import hex_to_array

app = FastAPI()

def parseFor(tagz: int, commands, payload: str):
    splited_commands=br_uncompress.split_commands(commands)

    inputData = base64.b64decode(payload).hex()

    if ((hex_to_array(inputData)[0] % 2) == 0): 
        batch = br_uncompress.uncompress(tagz, splited_commands, inputData, datetime.now().isoformat(timespec='milliseconds'))

        result = {}
        result["timestamp"] = batch["batch_absolute_timestamp"]

        for x in batch["dataset"]: 
            value = x["data"]["value"]
            label = x["data"]["label_name"]

            if (label ==  "Temperature"):
                value = value / 100

            if (label ==  "RelativeHumidity"):
                value = value / 100

            result[label] = value
      
        return result
    else:
        return parseUnitaryFrame(payload)

def parseUnitaryFrame(payload: str): 
    inputData = base64.b64decode(payload).hex()

    return json.loads(Decoding_JSON(inputData, False))

@app.get("/api/s0")
def S0Decoder(devEUI: str, payload: str, fport: int):
    result = parseFor(1, ['0,1,10,Pulse', '1,100,6,DisposableBatteryVoltage'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes': 
        if result['AttributeID'] == 'PresentValue':
            return {
                'State': result['Data']
            }
        if result['AttributeID'] == 'Count':
            return {
                'Pulse': result['Data']
            }
    else:
        result['DisposableBatteryVoltage'] = result['DisposableBatteryVoltage'] / 1000
        return result

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes': 
        if result['AttributeID'] == 'PresentValue':
            return {
                'State': result['Data']
            }
        if result['AttributeID'] == 'Count':
            return {
                'Pulse': result['Data']
            }
    else:
        result['DisposableBatteryVoltage'] = result['DisposableBatteryVoltage'] / 1000
        return result

@app.get("/api/thr")
def THRDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(3, ['0,10,7,Temperature', '1,100,6,RelativeHumidity', ' 2,10,12,Illuminance', '3,100,6,DisposableBatteryVoltage', '4,100,6,RechargeableBatteryVoltage'], payload)
    
    if 'AnalogInput' in result.keys():
        result['Illuminance'] = result.pop('AnalogInput')

    result['DisposableBatteryVoltage'] = result['DisposableBatteryVoltage'] / 1000
    result['RechargeableBatteryVoltage'] = result['RechargeableBatteryVoltage'] / 1000

    return result
@app.get("/api/senso")
def SensoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(1, ['0,1,11,Volume', '1,100,6,DisposableBatteryVoltage'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes': 
        if result['AttributeID'] == 'Volume':
            return {
                'Volume': result['Data']
            }
        if result['AttributeID'] == 'Status':
            return {
                'Status': {
                    'Freeze': result['Data']['b7'],
                    'Installation': result['Data']['b6'],
                    'Battery': result['Data']['b5'],
                    'Fraud': result['Data']['b4'],
                    'BackWaterLevel3': result['Data']['b3'],
                    'BackWaterLevel2': result['Data']['b2'],
                    'BackWaterLevel1': result['Data']['b1'],
                    'Leak': result['Data']['b0']
                }
            }
    else:
        result['DisposableBatteryVoltage'] = result['DisposableBatteryVoltage'] / 1000
        return result

@app.get("/api/pulsesenso")
def PulseSensoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(4, ['0,1,10,Index1', '1,1,10,Index2', '2,1,10,Index3', '3,1,1,State1', '4,1,1,State2', '5,1,1,State3', '6,100,6,BatteryLevel', '7,1,6,MultiState'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'PresentValue':
        return {
            "State{endpoint}".format(endpoint = result['EndPoint'] + 1): result['Data']
        }
    
    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'Count': 
        return {
            "Index{endpoint}".format(endpoint = result['EndPoint'] + 1): result['Data']
        }
    
    return result


@app.get("/api/presso")
def PressoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(3, ['0,0.004,12,mA', '1,1,12,V', '2,100,6,BatteryLevel', '3,100,6,ExtPowerLevel', '4,1,10,Index'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes': 
        if result['AttributeID'] == 'PresentValue' and result['EndPoint'] == 0:
            return {
                'mA': result['Data']
            }
        if result['AttributeID'] == 'PresentValue' and result['EndPoint'] == 1:
            return {
                'V': result['Data'] / 1000
            }

    result['BatteryLevel'] = result['BatteryLevel'] / 1000
    result['V'] = result.pop('V') / 1000

    return result

@app.get("/api/remotetemperature")
def RemoteTemperatureDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(1, ['0,10,7,Temperature', '1,100,6,BatteryLevel'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'MeasuredValue':
        return {
            "Temperature": result['Data'] / 100
        }

    return result

@app.get("/api/celso")
def CelsoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(1, ['0,10,7,Temperature', '1,100,6,BatteryLevel'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'MeasuredValue':
        return {
            "Temperature": result['Data'] / 100
        }


    return result

@app.get("/api/th")
def THDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(2, ['0,10,7,Temperature', '1,100,6,RelativeHumidity', '2,1,6,BatteryLevel', '3,1,1,OpenCase'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'MeasuredValue':
        return{
            "Temperature": result['Data'] / 100
        }

    result['BatteryLevel'] = result['BatteryLevel'] / 1000
    return result

@app.get("/api/flasho")
def FlashoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(1, ['0,1,10,Index', '1,100,6,BatteryLevel'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'Count':
        return {
            "Index": result['Data']
        }

    result['BatteryLevel'] = result['BatteryLevel'] / 1000
    return result

@app.get("/api/t")
def TDecoder(devEUI: str, payload: str, fport: int):
    return THDecoder(devEUI, payload, fport)

@app.get("/api/atmo")
def AtmoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(3, ['0,1,7,Temperature', '1,1,6,RelativeHumidity', '2,1,7,Pressure', '3,1,10,Index1', '4,1,10,Index2', '5,1,6,BatteryLevel'], payload)

    result.pop('Index1')
    result.pop('Index2')

    return result

@app.get("/api/ventilo")
def VentiloDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(3, ['0,1,7,MeanDifferentialPressureSinceLastReport', '1,1,7,MinimalDifferentialPressureSinceLastReport', '2,1,7,MaximalDifferentialPressureSinceLastReport', '3,1,6,BatteryLevel', '4,10,7,Temperature', '5,1,7,DifferentialPressure', '6,1,10,Index', '7,1,1,State'], payload)
    
    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'MeasuredValue':
        result = {
            result['ClusterID']: result['Data'] 
        }

    if 'BatteryLevel' in result:
        result['BatteryLevel'] = result['BatteryLevel'] / 1000
    
    if 'Temperature' in result:
        result['Temperature'] = result['Temperature'] / 100

    return result

@app.get("/api/closo")
def ClosoDecoder(devEUI: str, payload: str, fport: int):
    result = parseFor(2, ['0,1,1,Closed', '1,100,6,BatteryLevel'], payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributes'and result['AttributeID'] == 'PresentValue':
        clusterName = 'Closed'

        if result['EndPoint'] == 0:
            clusterName = 'CaseStatus'

        return {
            clusterName: result['Data'] 
        }

    if 'Closed' in result:
        result['Closed'] = bool(result['Closed'])

    return result

@app.get("/api/intenso")
def IntensoDecoder(devEUI: str, payload: str, fport: int):
    result = parseUnitaryFrame(payload)

    if 'CommandID' in result and result['CommandID'] == 'ReportAttributesAlarm'and result['AttributeID'] == 'PresentValue':
        return {
            'Current': result['Data']
        }

    return result

@app.get("/api/remotetemperature2ctn")
def RemoteTemperature2CTNDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,10,7,Temperature1', '1,10,7,Temperature2'], payload)

@app.get("/api/vaqao")
def VAQAODecoder(devEUI: str, payload: str, fport: int):
    frame = parseFor(3, ['1,10,7,Temperature' ,'2,100,6,RelativeHumidity', '3,10,6,CO2', '4,10,6,COV'], payload)
    return frame

@app.get("/api/vaqaoplus")
def VAQAOPlusDecoder(devEUI: str, payload: str, fport: int):
    frame = parseFor(3, ['0,1,4,Occupancy', '1,10,7,Temperature', '2,100,6,RelativeHumidity', '3,10,6,CO2', '4,10,6,COV', '5,10,6,LUX', '6,10,6,Pressure'], payload)
    return frame