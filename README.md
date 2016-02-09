FI-Ware Validator
======================

**Table of Contents**

- [Description](#description)
- [Features Implemented](#features-implemented)
- [Installation Manual](#installation-manual)
- [Installation Verification](#installation-verification)
- [User Manual](#user-manual)
- [API Documentation](#api-documentation)
- [License](#license)
- [Getting Started](#getting-started)
- [Installing Dependencies](#installing-dependencies)
- [Executing the listener API](#executing-the-listener-api)
- [External Dependencies](#external-dependencies)
- [Validation Process](#validation-process)
- [Example Client](#example-client)
- [Image generation](#image-generation)

Description
-----------
This project is part of [FIWARE] (http://fiware.org).

A FIWARE validator for testing deployment artifacts implemented as
a service with an OpenStack-native Rest API

Features Implemented
--------------------
A RESTful API for deployment artifacts validation

Installation Manual
-------------------
The installation manual is provided in rst format in the [Installation and Administration manual](doc/source/adminmanual.rst)

Installation Verification
-------------------------
The sanity check procedures are detailed in the [Installation and Administration manual](doc/source/adminmanual.rst)

User Manual
-----------
The user manual is provided in rst format in the [User and Programmers manual](doc/source/usermanual.rst)

API Documentation
-----------------

The API definition can be found at <http://docs.validatorapi2.apiary.io/#>

License
-------

Apache License Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>

Getting Started
---------------

To run the code you can clone the git repo with:

    git clone git@github.com:ging/fiware-validator.git

Installing Dependencies
-----------------------

To install package dependencies you must run:

    pip install -r requirements.txt

Executing the listener API
--------------------------

The listener api can be manually launched with the following command:

    validator/command/validator-api.py --config-dir etc/validator


External Dependencies
---------------------

The system deployment depends on several external services for
successful completion. The dependency list reads as follows:

- **OpenStack Keystone server**: Used for issuing user tokens for several OpenStack services
- **Docker Server**: Used for managing the chef server image
- **OpenStack Glance server**: Used for listing the available virtual machine images
- **OpenStack Nova server**: Used for deploying the selected virtual machine


Validation Process
------------------

The cookbook validation process consists on the following steps:

1. The **Client** sends a POST request to the service API, containing:
    - The name of the cookbook to be tested
    - The *chef supermarket* repository from which to obtain the cookbook
    - The virtual machine name for deployment

2. The **Server** receives the request and takes the following steps:
    - Checks the user permissions to take the next steps by validating against Keystone
    - Downloads the needed *cookbook*
    - Deploys the selected *Virtual Machine* image
    - Instructs the **Chef Server** to deploy the *cookbook* in the given *Virtual Machine*
    - Responds to the **Client** request informing of the status of the validation process

Example Client
---------------
An example client is provided in command/validator-client. It can be run with the following command:

    validator/command/validator-client.py --validator_url=${url_of_the_validator_api} --username=${username} --password=${password} --image=${author/image_name} --cookbook=${cookbook_name}

Image generation
---------------------
A default chef-solo image can be automatically generated and uploaded to the glance server with the following command:

    validator/command/generate_image.py --username=${username} --password=${password} --auth_url={$auth_url} --tag=${author/image_tag} --config-dir {configuration_dir}

Identically, a default puppet-standalone image can be automatically generated and uploaded to the glance server with the following command:

    validator/command/generate_image.py --username=${username} --password=${password} --auth_url={$auth_url} --tag=${author/image_tag} --config-dir {configuration_dir}