#!/bin/bash
id_apigateway="xxxxx" # informe o id da API Gateway

apigatewayurl=" https://$id_apigateway.execute-api.us-east-1.amazonaws.com/datadogpoweruser/api-lambda-nodejs"
tableName="api-lambda-nodejs"
id="1"
name="John"
occupation="Developer"

echo -e "\ncreate"
payloadstring='"id":"'$id'", "name":"'$name'", "occupation":"'$occupation'"'
curl -X POST -d "{\"operation\":\"create\",\"tableName\":\"$tableName\",\"payload\":{\"Item\":{ $payloadstring }}}" $apigatewayurl

echo -e "\nUnknown operation"
payloadstring='"id":"'$id'", "name":"'$name'", "occupation":"'$occupation'"'
curl -X POST -d "{\"operation\":\"Unknown\",\"tableName\":\"$tableName\",\"payload\":{\"Item\":{ $payloadstring }}}" $apigatewayurl

echo -e "\nread"
payloadstring='"id":"'$id'"'
curl -X POST -d "{\"operation\":\"read\",\"tableName\":\"$tableName\",\"payload\":{\"Key\":{ $payloadstring }}}" $apigatewayurl

echo -e "\ndelete"
payloadstring='"id":"'$id'"'
curl -X POST -d "{\"operation\":\"delete\",\"tableName\":\"$tableName\",\"payload\":{\"Key\":{ $payloadstring }}}" $apigatewayurl