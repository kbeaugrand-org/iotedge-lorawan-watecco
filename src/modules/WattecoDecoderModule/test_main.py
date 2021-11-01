from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_vaqaoplus():
    response = client.get("/api/vaqaoplus?payload=cEQABqw8ABnA7s4BIGEpaCPjgWxsEdBJGyY%2B0d0bABSCAu1eqN2yDAAFtJuXArCAdsuyBigAOA%3D%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')

    assert json == {"Occupancy":1,"Temperature":19.7,"RelativeHumidity":54.0,"CO2":690.0,"COV":50.0,"LUX":10,"Pressure":9790}

def test_vaqao():
    response = client.get("/api/vaqao?payload=QjOAgKhPAR2g6ADckf2BU2j3QgYOUWgv%2BmYm%2BtaSFn1rSYu%2BmESxRVEUFXFoniAUmxk%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
    
    assert json == {"Temperature":19.6,"RelativeHumidity":30.0,"CO2":500.0,"COV":250.0}

def test_thr():
    response = client.get("/api/thr?payload=UgAAgIGVBLDIPoIytA8CBQAI3hdwYxMAQBBAugbREiuK%2BSgM2REAgCIS&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
    
    assert json == {"Temperature":24.2,"RelativeHumidity":54.0,"Illuminance":320.0, "DisposableBatteryVoltage": 0, "RechargeableBatteryVoltage": 3.0}

def test_s0():
    response = client.get("/api/s0?payload=EQoADwBVEAA%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"State": False}

    response = client.get("/api/s0?payload=EQoADwQCIwAAAAE%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
            
    assert json == {"Pulse": 1}

    response = client.get("/api/s0?payload=JhUAIOBgAdceAACgZQ8%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
            
    assert json == {"Pulse": 45, "DisposableBatteryVoltage": 3.0}

def test_senso():
    response = client.get("/api/senso?payload=EQqAAgAAKwAAAB0%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"Volume": 29}

    response = client.get("/api/senso?payload=EQqAAwAAGGA%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == { 'Status': { "Freeze": False, "Installation": True, 'Battery': True, 'Fraud': False, 'BackWaterLevel3': False, 'BackWaterLevel2': False, 'BackWaterLevel1': False, 'Leak': False }}

    response = client.get("/api/senso?payload=JhUAIOBgAdceAACgZQ8%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
            
    assert json == {'DisposableBatteryVoltage': 3.0, 'Volume': 45}
    
def test_atmo():
    response = client.get("/api/atmo?payload=VgAAAAGTBNDsEyi0H6DfHgAAAIB7AAAAgAU%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')

    assert json == {"Temperature":24.64,"RelativeHumidity":23.24,"Pressure":1012}

def test_presso():
    response = client.get("/api/presso?payload=EQoADABVOUFQAAA%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"mA":13.0}

    response = client.get("/api/presso?payload=MQoADABVOUYU0AA%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"V":9.524}

    response = client.get("/api/presso?payload=IBUAgAH0ok5wgNLeAUISEPmuKVVAu2VpBA%3D%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')

    assert json == {"BatteryLevel":3.5,"V":7.52}

def test_pulsesenso():
    response = client.get("/api/pulsesenso?payload=EQoADwBVEAE%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"State1": True}

    response = client.get("/api/pulsesenso?payload=MQoADwQCIwAAAAE%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"Index2":1}

def test_remotetemperature():
    response = client.get("/api/remotetemperature?payload=EQoEAgAAKQBk&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"Temperature": 1}