#!/usr/bin/env python

# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

def set_paths_based_on_ossec(o_path='/var/ossec'):
    """
    Set paths based on ossec location.
    :param o_path: OSSEC Path, by default it is '/var/ossec'.
    :return:
    """

    global ossec_path
    ossec_path = o_path

    global ossec_conf
    ossec_conf = "{0}/etc/ossec.conf".format(ossec_path)

    global ossec_log
    ossec_log = "{0}/logs/ossec.log".format(ossec_path)

    global client_keys
    client_keys = '{0}/etc/client.keys'.format(ossec_path)

    global stats_path
    stats_path = '{0}/stats'.format(ossec_path)

    global ruleset_path
    ruleset_path = '{0}/ruleset'.format(ossec_path)

    global groups_path
    groups_path = "{0}/queue/agent-groups".format(ossec_path)

    global shared_path
    shared_path = "{0}/etc/shared".format(ossec_path)

    global backup_path
    backup_path = "{0}/backup".format(ossec_path)

    global ruleset_rules_path
    ruleset_rules_path = '{0}/rules'.format(ruleset_path)

    global database_path
    database_path = ossec_path + '/var/db'

    global database_path_global
    database_path_global = database_path + '/global.db'

    global api_config_path
    api_config_path = "{0}/api/configuration/config.js".format(ossec_path)

    global database_path_agents
    database_path_agents = database_path + '/agents'

    # Queues
    global ARQUEUE
    ARQUEUE = "{0}/queue/alerts/ar".format(ossec_path)

    # Socket
    global AUTHD_SOCKET
    AUTHD_SOCKET = "{0}/queue/ossec/auth".format(ossec_path)

# Agent upgrading variables
wpk_repo_url = "https://packages.wazuh.com/wpk/"

wpk_read_size = 512

upgrade_result_retries = 60 # Retries until get upgrade_result ok message
upgrade_result_sleep = 5 # Seconds between retries

agent_info_retries = 100 # Retries to detect when agent_info file is updated
agent_info_sleep = 2 # Seconds between retries

# Common variables
database_limit = 500

# Common variables based on ossec path (/var/ossec by default)
set_paths_based_on_ossec()
