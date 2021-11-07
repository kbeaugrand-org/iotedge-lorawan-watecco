from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_vaqaoplus():
    response = client.get("/api/vaqaoplus?devEUI=70B3D5E75E009F8F&fport=125&payload=EYqADAAAIQAZmLA=")
    assert response.status_code == 200
    json = response.json()
    assert json == {"Concentration": 25}

    response = client.get("/api/vaqaoplus?devEUI=70B3D5E75E009F8F&fport=125&payload=MYoEAgAAKQhnmNCx")
    assert response.status_code == 200
    json = response.json()
    assert json == {"Temperature": 21.51}

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

def test_celso():
    response = client.get("/api/celso?payload=EQoEAgAAKQdh&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"Temperature": 18.89}

    response = client.get("/api/celso?payload=EAFAgDY0AQwMtHuhdy%2FU7oUM&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')

    assert json == {"Temperature": 24.00}

def test_th():
    response = client.get("/api/th?payload=MgIAAEGYwI20V2gO%2Fw4hIQD55JYoKw%3D%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')

    assert json == {"Temperature": 5.17, "RelativeHumidity": 27.65, "BatteryLevel": 3.617 }

def test_flasho():
    response = client.get("/api/flasho?payload=EQoADwQCIwAAAAI%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"Index": 2}

    response = client.get("/api/flasho?payload=JhUAIOBgAdceAACgZQ8%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')

    assert json == {"Index": 45, "BatteryLevel": 3.00 }

def test_t():
    response = client.get("/api/th?payload=EQoEAgAAKQfQ&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 

    assert json == {"Temperature": 20.0 }

def test_ventilo():
    response = client.get("/api/ventilo?payload=EQoEAgAAKQfQ&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "Temperature": 20
        }

    response = client.get("/api/ventilo?payload=EQqACAAAKQGQ&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "DifferentialPressure": 400
        }

    response = client.get("/api/ventilo?payload=RjEAAAGzBkjsATiyByDQHqBmAQ%3D%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
    
    assert json == {
            "MeanDifferentialPressureSinceLastReport": 28,
            "MinimalDifferentialPressureSinceLastReport": 4,
            "MaximalDifferentialPressureSinceLastReport": 53,
            "BatteryLevel": 3.472
        }

    response = client.get("/api/ventilo?payload=NgcAgAD3gMPsAdi1FxBZAA%3D%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
    
    assert json == {
        "MeanDifferentialPressureSinceLastReport": 391,
        "MinimalDifferentialPressureSinceLastReport": 236,
        "MaximalDifferentialPressureSinceLastReport": 546
        }

def test_closo():
    response = client.get("/api/closo?payload=EQoADwBVEAA%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "CaseStatus": False # Teard Off
        }

    response = client.get("/api/closo?payload=EQoADwBVEAE%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "CaseStatus": True # OK
        }

    response = client.get("/api/closo?payload=MQoADwBVEAA%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "Closed": False
        }

    response = client.get("/api/closo?payload=MQoADwBVEAE%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "Closed": True
        }

    response = client.get("/api/closo?payload=EAMAQd12wMCAAxS0cAgdwCcZBwQwpbxrzAE%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
    
    assert json == {
            "Closed": True
        }

def test_intenso():
    response = client.get("/api/intenso?payload=MYoADABVOUEkh9LY0Q%3D%3D&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    
    assert json == {
            "Current": 10.283159255981445
        }

def test_remotetemperature2ctn():
    response = client.get("/api/remotetemperature2ctn?payload=IgUAEDVcBLPInoAODCAAWQHICkBWALICkIUkSZLqdDgA&devEUI=70B3D5E75E009F8F&fport=125")
    assert response.status_code == 200
    json = response.json() 
    json.pop('timestamp')
    
    assert json == {
            "Temperature1": 21.5,
            "Temperature2": 11.5
        }