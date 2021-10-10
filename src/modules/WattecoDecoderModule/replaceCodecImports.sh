#!/bin/sh

sed -i 's/from ZCL/from .ZCL/'                          ./Standard/Decoding_Functions.py
sed -i 's/from ZCL/from .ZCL/'                          ./Standard/ZCL_FRAME.py
sed -i 's/from ZCL/from .ZCL/'                          ./Standard/ZCL.py
sed -i 's/from WTC_CodecTools/from .WTC_CodecTools/'    ./Standard/ZCL.py
sed -i 's/from TICs/from .TICs/'                        ./Standard/ZCL.py
sed -i 's/from WTC_CodecTools/from ..WTC_CodecTools/'   ./Standard/TICs/_TIC_Tools.py
sed -i 's/import constants/from . import constants/'    ./Batch/br_uncompress.py