# Do not forget to pin down the version
FROM jupyterhub/jupyterhub:0.9.3

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .
RUN mkdir "ssl"
COPY ssl/server.crt ./ssl
COPY ssl/server.key ./ssl
COPY userlist .


# Download script to automatically stop idle single-user servers
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py
# COPY cull_idle_servers.py .

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0 \
    jupyter-client==7.1.0