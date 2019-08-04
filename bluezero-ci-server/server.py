from flask import Flask, jsonify, request
from uuid import uuid4


class BluezeroServer:

    def run_lint(self):
        pass

    def run_check(self):
        pass


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

bz_ci = BluezeroServer()


@app.route('/payload', methods=['POST'])
def payload():
    values = request.get_json()
    # print(values)
    if 'zen' in values:
        return ''
    elif 'pull_request' in values:
        print('Pull Request')
    elif 'check_runs' in values:
        print('Check runs')
    elif 'check_suite' in values:
        print('Check suite')
    elif 'commits' in values:
        print('pushes')
        # sha = values['head']['sha']
        # branch_name = values["head"]["ref"]
        # repo_name = values["head"]["repo"]
        # print(f'sha = {sha}, branch_name = {branch_name} repo_name = {repo_name}')
    return ''


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int,
                        help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
