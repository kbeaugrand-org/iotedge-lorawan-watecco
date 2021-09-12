
import base64
import binascii
import json 

from typing import Optional
from fastapi import FastAPI
from datetime import datetime

from .Standard.Decoding_Functions import Decoding_JSON, version
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
            result[x["data"]["label_name"]] = x["data"]["value"]
        
        return result
    else:
        return parseUnitaryFrame(payload)

def parseUnitaryFrame(payload: str): 
    inputData = base64.b64decode(payload).hex()

    frame = json.loads(Decoding_JSON(inputData, False))

    result = {}
    result[frame['ClusterID']] = frame['Data'] 

    return result

@app.get("/api/stdframe")
def S0Decoder(devEUI: str, payload: str, fport: int):
    return parseUnitaryFrame(payload)

@app.get("/api/s0")
def S0Decoder(devEUI: str, payload: str, fport: int):
    return parseFor(1, ['0,1,10,Index1', '1,100,6,BatteryLevel'], payload)

@app.get("/api/thr")
def THRDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,10,7,Temperature', '1,100,6,RelativeHumidity', ' 2,10,12,Luminosity', '3,100,6,Disposable_BatteryLevel', '4,100,6,Rechargeable_BatteryLevel'], payload)

@app.get("/api/senso")
def SensoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,1,4,Status', '1,1,11,Index', '2,1,5,MinFlow', '3,1,5,MaxFlow'], payload)

@app.get("/api/pulsesenso")
def PulseSensoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(4, ['0,1,10,Index1', '1,1,10,Index2', '2,1,10,Index3', '3,1,1,State1', '4,1,1,State2', '5,1,1,State3', '6,100,6,BatteryLevel', '7,1,6,MultiState'], payload)

@app.get("/api/presso")
def PressoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,0.004,12,4-20mA', '1,1,12,0-10V', '2,100,6,BatteryLevel', '3,100,6,ExtPowerLevel', '4,1,10,Index'], payload)

@app.get("/remotetemperature")
def RemoteTemperatureDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(1, ['0,10,7,Temperature', '1,100,6,BatteryLevel'], payload)

@app.get("/api/celso")
def CelsoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(1, ['0,10,7,Temperature', '1,100,6,BatteryLevel'], payload)

@app.get("/api/th")
def THDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(2, ['0,10,7,Temperature', '1,100,6,RelativeHumidity', '2,1,6,BatteryLevel', '3,1,1,OpenCase'], payload)

@app.get("/api/flasho")
def FlashoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(1, ['0,1,10,Index', '1,100,6,BatteryLevel'], payload)

@app.get("/api/vaquaoplus")
def VAQAOPlusDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,1,4,OCC', '1,10,7,T', '2,100,6,H', '3,10,6,CO2', '4,10,6,COV', '5,10,6,LUX', '6,10,6,P'], payload)

@app.get("/api/t")
def TDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(2, ['0,10,7,Temperature', '2,1,6,BatteryLevel', '3,1,1,OpenCase'], payload)

@app.get("/api/atmo")
def AtmoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,1,7,Temperature', '1,1,6,RelativeHumidity', '2,1,7,Pressure', '3,1,10,Index1', '4,1,10,Index2', '5,1,6,BatteryLevel'], payload)

@app.get("/api/ventilo")
def VentiloDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,1,7,Mean_differential_pressure_since_last_report', '1,1,7,Minimal_differential_pressure_since_last_report', '2,1,7,Maximal_differential_pressure_since_last_report', '3,1,6,BatteryLevel', '4,10,7,Temperature', '5,1,7,DifferentialPressure', '6,1,10,Index', '7,1,1,State'], payload)

@app.get("/api/closo")
def ClosoDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(2, ['0,1,1,OpenClose', '1,100,6,BatteryLevel'], payload)

@app.get("/api/pulsesensoatexz1")
def PulseSensoAtexZ1Decoder(devEUI: str, payload: str, fport: int):
    return parseFor(4, ['0,1,10,Index1', '1,1,10,Index2', '2,1,10,Index3', '3,1,1,State1', '4,1,1,State2', '5,1,1,State3', '6,100,6,BatteryLevel', '7,1,6,MultiState'], payload)

@app.get("/api/remotetemperature2ctn")
def RemoteTemperature2CTNDecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['0,10,7,Temperature1', '1,10,7,Temperature2'], payload)

@app.get("/api/vaquao")
def VAQAODecoder(devEUI: str, payload: str, fport: int):
    return parseFor(3, ['1,10,7,T' ,'2,100,6,H', '3,10,6,CO2', '4,10,6,COV'], payload)