#!/bin/bash

set -e

API_URL=http://localhost:6788

echo "🔎 Testing single prediction..."

single_payload='{
  "text": "campera-gris-azulada-art7578"
}'

echo -e "\n📤 Request Payload:"
echo "$single_payload"

echo -e "\n📥 Response:"
curl -s -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d "$single_payload" | jq

echo "----------------------------------------------------"

echo "🔎 Testing batch prediction..."

batch_payload='{
  "texts": [
    "campera-gris-azulada-art7578",
    "pantalon-hombre-verde",
    "zapatillas-running-azul"
  ]
}'

echo -e "\n📤 Request Payload:"
echo "$batch_payload"

echo -e "\n📥 Response:"
curl -s -X POST "$API_URL/batch_predict" \
  -H "Content-Type: application/json" \
  -d "$batch_payload" | jq

