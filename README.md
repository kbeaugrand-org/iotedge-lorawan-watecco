
# Azure IoT Edge LoRaWAN Watteco Sensors Support

[![Build](https://github.com/kbeaugrand-org/iotedge-lorawan-watteco/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/kbeaugrand-org/iotedge-lorawan-watteco/actions/workflows/ci.yml)
[![Continuous Deployment](https://github.com/kbeaugrand-org/iotedge-lorawan-watteco/actions/workflows/cd.yml/badge.svg)](https://github.com/kbeaugrand-org/iotedge-lorawan-watteco/actions/workflows/cd.yml)

## Description

This repository stores the code for executing an Azure IoT Edge LoRaWAN Decoder module for watteco Sensors.

### Batch Uncompress

By default this module will uncompress batch data coming from sensors with default configuration once they are provisioned on the IoT Platform.
The uncompress function is made by the br_uncompress_py module that can be downloaded at : [http://support.nke-watteco.com/downloads/](http://support.nke-watteco.com/downloads/)

### Batch V.S Standard

NKE Sensors can send multiple frame types.
Some of them can send batch frames (which can be disabled) rather than other can only send unitary frames.

To distinguish which kind of frame is present, the decoding function will be aware of the first bit on the first Byte of the payload.

- 0 : Batch
- 1 : Standard

### Current Sensors Available

__Current Version__ of NKE uncompress module used is __1.0.5__.

| Sensor Name                             | Decoder Endpoint                |
|-----------------------------------------|---------------------------------|
| 50-70-001 S0                            | /api/s0                         |
| 50-70-007 THr harvesting                | /api/thr                        |
| 50-70-011 Senso                         | /api/senso                      |
| 50-70-[014/039/051/072/079] PulseSenso  | /api/pulsesenso                 |
| 50-70-123 PulseSenso AtEX Zone 1        | /api/pulsesenso                 |
| 50-70-016 Presso                        | /api/presso                     |
| 50-70-[043/142] Remote temperature      | /api/remotetemperature          |
| 50-70-139 Remote temperature 2CTN       | /api/remotetemperature2ctn      |
| 50-70-049 Celso                         | /api/celso                      |
| 50-70-053 TH                            | /api/th                         |
| 50-70-071 Flasho                        | /api/flasho                     |
| 50-70-074 VAQAO+Plus                    | /api/vaqaoplus                  |
| 50-70-085 T                             | /api/t                          |
| 50-70-099 Atmo                          | /api/atmo                       |
| 50-70-101 Ventilo                       | /api/ventilo                    |
| 50-70-108 Closo                         | /api/closo                      |
| 50-70-168 VAQAO                         | /api/vaqao                      |
| 50-70-098 Intens'O                      | /api/intenso                    |

## Deploy

You can add this module to you IoT Edge Deployment by adding this module definition:

```json
{
...
    "WattecoDecoder": {
        "settings": {
            "image": "kbeaugrand/az-iotedge-watteco-decoder-module:latest",
            "createOptions": ""
        },
        "type": "docker",
        "version": "1.0",
        "status": "running",
        "restartPolicy": "always"
    }
...
}
```

## Tests

You can use this project to launch the decoder and test manually test it.

### Prerequisites

* VSCode (with Azure IoT Toolkit extension installed)
    * [VS Code](https://code.visualstudio.com/)
    * [Azure IoT Toolkit Extension](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)
* Azure Subscription
* Azure IoT Hub Resource in your subscription
* Setup Azure IoT Edge Simulator

> For more information about prerequisites: [Use VS Code as IoT Hub Device Simulator — Say Hello to Azure IoT Hub in 5 Minutes](https://devblogs.microsoft.com/iotdev/use-vs-code-as-iot-hub-device-simulator-say-hello-to-azure-iot-hub-in-5-minutes/)

### Launch

Simply execute the "Azure IoT Edge: Build and Run IoT Edge Solution in Simulator" command in Visual Studio Code and in terminal type: 

```sh
curl --location --request GET 'http://localhost:8080/api/vaquaoplus?payload=cjAAAAExAiHxvgRfuAfwkOwVZER7CS7pHsBXsJPYABmAAGQFIGuZ2Q4MySmlqtkXyG5Z&devEUI=000000000000000000&fport=125'
```

## Credits

* [https://support.nke-watteco.com/](https://support.nke-watteco.com/)
* [https://github.com/Azure/iotedge-lorawan-starterkit](https://github.com/Azure/iotedge-lorawan-starterkit)
* [https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md](https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md)
