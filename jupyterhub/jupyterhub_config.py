# Configure single user spawner
import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

## Configure authentication (delagated to GitLab)
from oauthenticator.gitlab import GitLabOAuthenticator

c.JupyterHub.authenticator_class = GitLabOAuthenticator