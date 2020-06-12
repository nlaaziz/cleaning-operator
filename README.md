![Docker Image CI](https://github.com/nlaaziz/cleaning-operator/workflows/Docker%20Image%20CI/badge.svg)


# cleaning-operator

DockerHub cleaning-operator image url:

https://hub.docker.com/repository/docker/nlaaziz/cleaning-operator


## IDEA

This operator ensures that your openshift cluster is cleaned when resources are no longer used or needed.
An expiry date is set by the creator of the resource at creation time ( or a default value is set in the Custom Resource Definition), then the operator deletes 'out of date' objects.

This operator is in the developement process

## USAGE

By default, namespaces will be labeled as protected

```cleaningOperator_protected: "true"```

##### create a namespace:

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    cleaningOperator_protected: "false"
    cleaningOperator_expiry: 5d
  name: test
```

##### to unprotect your namespace

```cleaningOperator_protected: "false"```

##### define expiry in days

```cleaningOperator_expiry: 5d```


## ansible based openshift operators documentation:

https://docs.openshift.com/container-platform/4.4/operators/operator_sdk/osdk-ansible.html
