#!/bin/bash
echo "uasge: ./tflite2kmodel.sh xxx.tflite"
name=`echo $1 | cut -d '.' -f 1`
name=$name.kmodel
/content/Maix_Toolbox/ncc/ncc -i tflite -o k210model --dataset /content/Maix_Toolbox/images $1 /$name
#Nedan är om man anvädner ncc 2.0, funkar inte.
# /content/Maix_Toolbox/ncc/ncc compile /content/Yolo-digit-detector/model.tflite /content/Maix_Toolbox/model.kmodel -i tflite -o kmodel -t k210 --dataset

