#!/bin/bash

echo "installing helm..."
if ! command -v helm &> /dev/null
then
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
fi

echo "installing up cli..."
if ! command -v up &> /dev/null
then
    curl -sL "https://cli.upbound.io" | sh
    sudo mv up /usr/local/bin
fi

echo "installing universal crossplane..."
up uxp install # creates upbound-system namespace
echo "sleep 30 seconds for CRDs to become available from helm chart install..."
sleep 30
kubectl apply -f /home/martinfleming/src/upbound/provider.yaml

echo "sleep 60 seconds for provider to become healthy..."
sleep 60
kubectl get pkg
echo ''

echo "creating creds secret for arn:aws:iam::011882408883:user/iamadmin in general account..."
if kubectl get secret aws-creds -n upbound-system >/dev/null 2>&1
    then kubectl delete secret aws-creds -n upbound-system
fi

echo "creating secret and applying providerConfig..."
kubectl create secret generic aws-creds -n upbound-system --from-file=creds=./creds.conf
echo applying aws-creds
kubectl apply -f aws-creds.yaml