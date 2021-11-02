#!/bin/sh

sed -i 's/^from ZCL/from .ZCL/'                          ./Standard/srcWatteco/Decoding_Functions.py
sed -i 's/^from ZCL/from .ZCL/'                          ./Standard/srcWatteco/ZCL_FRAME.py
sed -i 's/^from ZCL/from .ZCL/'                          ./Standard/srcWatteco/ZCL.py
sed -i 's/^from WTC_CodecTools/from .WTC_CodecTools/'    ./Standard/srcWatteco/ZCL.py
sed -i 's/^from TICs/from .TICs/'                        ./Standard/srcWatteco/ZCL.py
sed -i 's/^from WTC_CodecTools/from ..WTC_CodecTools/'   ./Standard/srcWatteco/TICs/_TIC_Tools.py
sed -i 's/^import constants$/from . import constants/'  ./Batch/br_uncompress.py