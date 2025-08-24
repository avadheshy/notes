  # login to ec2
  ```
  ssh -i maven.pem ubuntu@ip
  ```
  # switch to root user
  sudo -i
  # generate ssh key
  ```
  ssh-keygen
  ```
  # install aws cli
  ```
sudo apt update
sudo apt install awscli -y
aws --version
  ```
# configure aws
```
aws configure

```
# install kubectl
```
curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client

```
# install kops 
```
curl -Lo kops https://github.com/kubernetes/kops/releases/latest/download/kops-linux-amd64
chmod +x kops
sudo mv kops /usr/local/bin/
kops version
```
# make a s3 bucket
# make a public hosted zone and add 4 ns recard to hostinger
# make kubernetes cluster
```
kops create cluster --name=crazycoder.shop --state=s3://kops2015 --zones=us-east-1a,us-east-1b --node-count=2 --node-size=t3.small --control-plane-size=t3.medium --dns-zone=crazycoder.shop --node-volume-size=12 --control-plane-volume-size=12 --ssh-public-key ~/.ssh/id_ed25519.pub
# apply cluster that will reflect changes
kops update cluster --name=crazycoder.shop --state=s3://kops2015 --yes --admin
# validate clusetr
kops validate cluster --name=crazycoder.shop --state=s3://kops2015
# delete cluster
kops delete cluster --name=crazycoder.shop --state=s3://kops2015 --yes 
```
# making infress
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.3/deploy/static/provider/aws/deploy.yaml
```
---
read config file
what is kube config file
you can copy this config file to use the cluster from different mathine where you need to paste this file in config file.
```
cat ./kube/config
```
kubectl get nodes

# pod making
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80

```
# validate pod
Save the file as nginx-pod.yaml.
Apply it to your kOps cluster

```
kubectl apply -f nginx-pod.yaml
# Check if the pod is running:
kubectl get pods
# If you want to access it inside the cluster:
kubectl port-forward pod/nginx-pod 8080:80
# Then open http://localhost:8080.
```
# name spaces
- there are 3 types (default/kube public/kube-system)
- you can get all namespaces
- name of resources should be unique within the namespace not across  the namespaces.
- we can build and use our name space
```
kubectl get ns
kubectl get all # it will return all the resources in default namespace
kubectl get all --all-namespaces
kubectl get svc -n kube-system
kubectl create ns kubekart # this will create kubekart namespace
kubeclt run nginx --image=nginx -n kubekart # this will run nginx pod in kubekart namespace
# you can define namespace in .yaml file of pod in which you want to run
kubectl delete ns kubekart # it is going to delete kubekart namespace
```

# different level of logging
- this is used for finding bug in pods
- first setup local and test then go to production

```
kubectl get pod
kubectl delete pod nginx # to delete ngnix pod
kubectl get pod -o wide # this will give more info about the pod
kubectl get pod -o yaml # this also will give more info about pod
kubectl describe  pod nginx # this will show what is happening in pod events
kubectl logs nginx # this will show logs of the container
```
# service 
- it is a way to expose your application running on a set of pods as a network service.
- it is similar to loadbalancer in aws.
- these are 3 type nodePort/clusterip/loadbalacer
- nodeport is used for testing purpose
- clusterip is used for enternal communication
- loadbalance is used for production use case.


# Extra
## 1. taint and tolration
## 2 .limits
- it is used to reserve cpu and memory
- if pod not get that much then it wait
- request is reserving
- limit is restricting
## 3. job
- these type of container run at a defenite period of time
- these is similar to cronjob of machine
- job runs immediately and return response but cronjob runs at a specific time
## daemonset
- it is used for logging,matrix and monitoring the master and worker node
get daemonset
```
kubectl get ds -A
```
# helm
- helm simplifies deployment and maintains of application
  