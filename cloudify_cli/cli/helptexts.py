########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############

VERBOSE = \
    "Show verbose output. You can supply this up to three times (i.e. -vvv)"
VERSION = (
    "Display the version and exit (if a manager is used, its version will "
    "also show)"
)

INPUTS_PARAMS_USAGE = (
    '(Can be provided as wildcard based paths '
    '(*.yaml, /my_inputs/, etc..) to YAML files, a JSON string or as '
    'key1=value1;key2=value2). This argument can be used multiple times'
)
WORKFLOW_TO_EXECUTE = "The workflow to execute [default: {0}]"

BLUEPRINT_PATH = "The path to the application's blueprint file"
BLUEPRINT_ID = "The unique identifier for the blueprint"
VALIDATE_BLUEPRINT = "Validate the blueprint first"

RESET_CONTEXT = "Reset the working environment"
HARD_RESET = "Hard reset the configuration, including coloring and loggers"
SHOW_ACTIVE_CONNECTION_INFORMATION = \
    "Show connection information for the active manager"
ENABLE_COLORS = "Enable colors in logger (use --hard when working with" \
                " an initialized environment) [default: False]"

OUTPUT_PATH = "The local path to download to"
BLUEPRINT_FILENAME = (
    "The name of the archive's main blueprint file. "
    "This is only relevant if uploading an archive")
INPUTS = "Inputs for the deployment {0}".format(INPUTS_PARAMS_USAGE)
PARAMETERS = "Parameters for the workflow {0}".format(INPUTS_PARAMS_USAGE)
ALLOW_CUSTOM_PARAMETERS = (
    "Allow passing custom parameters (which were not defined in the "
    "workflow's schema in the blueprint) to the execution"
)
INSTALL_PLUGINS = "Install the necessary plugins for the given blueprint"
TASK_RETRIES = \
    "How many times should a task be retried in case of failure [default: {0}]"
TASK_THREAD_POOL_SIZE = \
    "The size of the thread pool to execute tasks in [default: {0}]"

SSH_COMMAND = "Execute a command on the manager over SSH"
SSH_HOST_SESSION = "Host an SSH tmux session"
SSH_CONNECT_TO_SESSION = "Join an SSH tmux session"
SSH_LIST_SESSIONS = "List available SSH tmux sessions"

OPERATION_TIMEOUT = (
    "Operation timeout in seconds (The execution itself will keep going, but "
    "the CLI will stop waiting for it to terminate) [default: {0}]"
)
INCLUDE_LOGS = "Include logs in returned events [default: True]"
JSON_OUTPUT = "Output events in a consumable JSON format"

SKIP_INSTALL = "Skip install lifecycle operations"
SKIP_UNINSTALL = "Skip uninstall lifecycle operations"
FORCE_UPDATE = (
    "Force running update in case a previous update on this deployment has "
    "failed to finished successfully"
)

DEPLOYMENT_ID = "The unique identifier for the deployment"
EXECUTION_ID = "The unique identifier for the execution"
IGNORE_LIVE_NODES = (
    "Delete the deployment even if there are existing live nodes for it"
)

INCLUDE_SYSTEM_WORKFLOWS = "Include executions of system workflows"

FORCE_CONCURRENT_EXECUTION = (
    "Execute the workflow even if there is an ongoing execution for the given "
    "deployment"
)
FORCE_CANCEL_EXECUTION = (
    "Terminate the execution abruptly, rather than request an orderly "
    "termination"
)

INIT_LOCAL = "Initialize environment for local executions"
NODE_NAME = "The node's name"

FORCE_PURGE_LOGS = "Force purge. This flag is mandatory"
BACKUP_LOGS_FIRST = "Whether to backup before purging"

RESTORE_SNAPSHOT_EXCLUDE_EXISTING_DEPLOYMENTS = (
    "Restore without recreating the currently existing deployments"
)
FORCE_RESTORE_ON_DIRTY_MANAGER = (
    "Restore a snapshot on a manager where there are existing blueprints or "
    "deployments"
)
INCLUDE_METRICS_IN_SNAPSHOT = "Include metrics data in the snapshot"
EXCLUDE_CREDENTIALS_IN_SNAPSHOT = "Exclude credentials in the snapshot"
SNAPSHOT_ID = "The unique identifier for the snapshot"

KEEP_UP_ON_FAILURE = "Do not teardown the manager even if the bootstrap fails"
DONT_SAVE_PASSWORD_IN_PROFILE = "After the bootstrap is complete, don't " \
                                "save the password in the profile context. " \
                                "Regardless, the password will *always* be " \
                                "printed to the console [default: False]"
VALIDATE_ONLY = (
    "Only perform resource creation validation without actually bootstrapping"
)
SKIP_BOOTSTRAP_VALIDATIONS = (
    "Bootstrap without validating resource creation prior to bootstrapping "
    "the manager"
)
SKIP_BOOTSTRAP_SANITY = \
    "Bootstrap without performing the post-bootstrap sanity test"
DEV_TASK_ARGS = "Arguments for the fabric task"

MAINTENANCE_MODE_WAIT = (
    "Wait until there are no running executions and automatically activate "
    "maintenance-mode"
)

FORCE_DELETE_PLUGIN = (
    "Delete the plugin even if there are deployments which are currently "
    "using it"
)

FORCE_TEARDOWN = "This is mandatory for performing the teardown"

IGNORE_DEPLOYMENTS = \
    "Teardown even if there are existing deployments on the manager"

TAIL_OUTPUT = "Tail the events of the specified execution until it ends"


SET_MANAGEMENT_CREDS = (
    'You can use the `-s` and `-k` flags to set the ssh user and '
    'key-file path respectively. '
    '(e.g. `cfy profiles use -s my_user -k ~/my/key/path`)'
)

DEFAULT_MUTUALITY_MESSAGE = 'Cannot be used simultaneously'

MANAGEMENT_IP = 'The IP of the host machine on which you bootstrapped'
SSH_USER = 'The SSH user on the host machine with which you bootstrapped'
SSH_KEY = 'The path to the ssh key-file to use when connecting'
SSH_PORT = 'The SSH port to use when connecting to the manager'
MANAGER_USERNAME = 'Manager username used to run commands on the manager'
MANAGER_PASSWORD = 'Manager password used to run commands on the manager'
MANAGER_TENANT = 'The tenant associated with the current user operating the ' \
                 'manager'
REST_PORT = "The REST server's port"

EXPORT_SSH_KEYS = 'Include ssh key files in archive'
IMPORT_SSH_KEYS = 'WARNING: Import exported keys to their original locations'

SORT_BY = "Key for sorting the list"
DESCENDING = "Sort list in descending order [default: False]"

INSTALL_SCRIPT_LOCATION = \
    'Alternative location of the `install_agents.py` script'
TENANT = 'The name of the tenant'
TENANT_TEMPLATE = 'The name of the tenant of the {0}'
TENANT_LIST_TEMPLATE = 'The name of the tenant to list {0}s from'
ALL_TENANTS = 'Include resources from all tenants associated with the user. ' \
              'This option is mutually exclusive with the argument ' \
              '`tenant_name` and cannot be used simultaneously'
GROUP = 'The name of the user group'
GROUP_DN = 'The ldap group\'s distinguished name. This option is required ' \
           'when using ldap'

SECURITY_ROLE = "A role to determine the user's permissions on the manager " \
                "(default: user)"
PASSWORD = 'Cloudify manager password'

CLUSTER_HOST_IP = \
    'The IP of this machine to use for advertising to the cluster'
CLUSTER_JOIN = 'Address of one of the cluster members to join'
CLUSTER_NODE_NAME = \
    'Name of this manager machine to be used internally in the cluster'
CLUSTER_JOIN_PROFILE = (
    'After joining the cluster, add the current manager to this profile '
    '(use when you have a profile containing the cluster master)'
)

PRIVATE_RESOURCE = 'If set to True the uploaded resource will only be ' \
                   'accessible by its creator. Otherwise, the resource is ' \
                   'accessible by all users that belong to the same tenant. ' \
                   '(default: False)'

SKIP_PLUGINS_VALIDATION = 'Determines whether to validate if the' \
                          ' required deployment plugins exist on the manager.'\
                          ' If validation is skipped, plugins containing' \
                          ' source URL will be installed from source.' \

USER = 'Username of user to whom the permissions apply. ' \
       'This argument can be used multiple times'
PERMISSION = 'The permission applicable to a resource [viewer|owner] ' \
             '(default:viewer)'
RESTORE_SNAPSHOT_TENANT_NAME = 'The name of the tenant into which the ' \
                               'snapshot should be restored. ' \
                               'Important - this option is required when ' \
                               'restoring snapshots from managers of ' \
                               'versions prior to 4.0.0. If passed when ' \
                               'restoring newer snapshots, an error ' \
                               'will be raised. ' \
                               'The given tenant will be created ' \
                               'automatically. If the tenant name passed ' \
                               'already exists on the manager, an error ' \
                               'will be raised'
SKIP_CREDENTIALS_VALIDATION = 'Do not check that the passed credentials are ' \
                              'correct (default:False)'
LDAP_SERVER = 'The LDAP server address to authenticate against'
LDAP_USERNAME = 'The LDAP admin username to be set on the Cloudify manager'
LDAP_PASSWORD = 'The LDAP admin password to be set on the Cloudify manager'
LDAP_DOMAIN = 'The LDAP domain to be used by the server'
LDAP_IS_ACTIVE_DIRECTORY = 'Specify whether the LDAP used for authentication' \
                           ' is Active-Directory.'
LDAP_DN_EXTRA = 'Extra LDAP DN options.'

GET_DATA = 'When set to True, displays the full list of connected resources ' \
           '(users/tenants/user-groups), for each listed resource. When set ' \
           'to False displays the total number of connected resources. ' \
           '(default:False)'
PROFILE_NAME = 'Name of the profile to use'
SECRET_VALUE = "The secret's value to be set"
SECRET_STRING = "The string to use as the secret's value"
SECRET_FILE = "The secret's file to use its content as value to be set"
