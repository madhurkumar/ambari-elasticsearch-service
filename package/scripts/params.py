#!/usr/bin/env python

"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from resource_management import *
import os

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()

java64_home = config['hostLevelParams']['java_home']

hostname = config['hostname']

elastic_user = config['configurations']['elastic-env']['elastic_user']
elastic_group = config['configurations']['elastic-env']['elastic_group']

elastic_base_dir = config['configurations']['elastic-env']['elastic_base_dir']
elastic_conf_dir = elastic_base_dir + "/config"
elastic_log_dir = elastic_base_dir + "/logs"
elastic_pid_dir = config['configurations']['elastic-env']['elastic_pid_dir']
elastic_pid_file = format("{elastic_pid_dir}/elasticsearch.pid")

elastic_install_log = elastic_base_dir + '/elasticsearch-install.log'
elastic_download = 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.tar.gz'
xpack_download = 'https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-5.2.2.zip'

hostname = config['hostname']
elastic_yml_template = config['configurations']['elastic-config']['elasticsearch_yml_template']
security_role_mapping_template = config['configurations']['elastic-config']['security_role_mapping_template']
security_roles_template = config['configurations']['elastic-config']['security_roles_template']
xpack_security_ssl_certs_template = config['configurations']['elastic-config']['xpack_security_ssl_certs_template']
