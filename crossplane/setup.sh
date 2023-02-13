#!/bin/bash

echo "installing helm..."
if ! command -v helm &> /dev/null
then
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
fi

helm repo add \
crossplane-stable https://charts.crossplane.io/stable && helm repo update

helm install crossplane \
crossplane-stable/crossplane \
--namespace crossplane-system \
--create-namespace

kubectl apply -f /home/martinfleming/src/crossplane/aws-provider.yaml

echo "creating creds secret for arn:aws:iam::011882408883:user/iamadmin in general account..."
if kubectl get secret aws-creds -n upbound-system >/dev/null 2>&1
    then kubectl delete secret aws-creds -n crossplane-system
fi

echo "creating secret and applying providerConfig..."
kubectl create secret generic aws-creds -n crossplane-system --from-file=creds=./creds.conf
echo applying aws-creds

kubectl apply -f /home/martinfleming/src/crossplane/aws-providerconfig.yaml