![Docker Image CI](https://github.com/nlaaziz/cleaning-operator/workflows/Docker%20Image%20CI/badge.svg)


# cleaning-operator

DockerHub cleaning-operator image url:

https://hub.docker.com/repository/docker/nlaaziz/cleaning-operator


## EphemeralNamespace Custom Resource Definition

The operator adds the possibility to create ephemeralnamespaces that have an expiry date.

The operator ensures that the outdated namespaces are deleted.

The operator is in the developement process

## USAGE

#### Create an EphemeralNamespace resource

```
apiVersion: cleaning.ansible-operator.com/v1
kind: EphemeralNamespace
metadata:
  name: ephemeral-ns-test
spec:
  expiry: 5d
```

```
oc create -f test-ephemeralnamespace.yaml
ephemeralnamespace.cleaning.ansible-operator.com/ephemeral-ns-test created
```

#### A namespace associated to the EphemeralNamespace resource is created with labels

```
cleaningOperator_protected: "false"
cleaningOperator_expiry: 5d
cleaningOperator_ephemeralnamespace: "true"
```

```
$ oc get namespace ephemeral-ns-test --show-labels
NAME                STATUS   AGE   LABELS
ephemeral-ns-test   Active   18s   cleaningOperator_ephemeralnamespace=true,cleaningOperator_expiry=5d,cleaningOperator_protected=false
```

#### A deletion cronjob associated to the EphemeralNamespace resource is created

```
$ oc get cronjobs.batch ephemeral-ns-test-cleaner
NAME                        SCHEDULE        SUSPEND   ACTIVE   LAST SCHEDULE   AGE
ephemeral-ns-test-cleaner   40 01 19 06 *   False     0        <none>          76s
```

After 5 days the namespace will be deleted.

```
cleaningOperator_protected: "true"
```

#### You can also attach an existing namespace to an ephemeralnamespace:
#### label your namespace

```
oc label namespace test-namespace cleaningOperator_ephemeralnamespace=true
```

#### create an ephemeralnamespace with the same namespace name

```
apiVersion: cleaning.ansible-operator.com/v1
kind: EphemeralNamespace
metadata:
  name: test-namespace
spec:
  expiry: 154d
```

## ansible based openshift operators documentation:

https://docs.openshift.com/container-platform/4.4/operators/operator_sdk/osdk-ansible.html
