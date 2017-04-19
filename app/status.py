import docker
from flask import abort
from flask import Flask


docker_client = docker.from_env()
app = Flask(__name__)


@app.route('/')
def status():
    state = docker_client.info().get("Swarm").get("LocalNodeState")
    print('LocalNodeState: {}'.format(state))

    if state == 'active':
        return state
    abort(403)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
