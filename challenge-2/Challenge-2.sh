Challenge-2:-
================
i opted for Azure instance metadata retrival and convert to JSON format as below :

#!/bin/bash
echo "path of the pem file: "
read pemfile
echo "public VM IP: "
read publicvm_IP
if [[ ${pemfile} =~ " " ]]||[[ ${publicvm_IP} =~ " " ]]; then
    echo 'Inputs cannot be blank please try again!'
    exit 1
else
    finalop=$(ssh -i $pemfile azureuser@$publicvm_IP "curl -H Metadata:true "http://169.254.169.254/metadata/instance?api-version=2017-08-01" | jq")
    echo $finalop
fi
