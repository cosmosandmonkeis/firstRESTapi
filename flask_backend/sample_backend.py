from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'


users = {
    'users_list':
        [
            {
                'id': 'xyz789',
                'name': 'Charlie',
                'job': 'Janitor',
            },
            {
                'id': 'abc123',
                'name': 'Mac',
                'job': 'Bouncer',
            },
            {
                'id': 'ppp222',
                'name': 'Mac',
                'job': 'Professor',
            },
            {
                'id': 'yat999',
                'name': 'Dee',
                'job': 'Aspring actress',
            },
            {
                'id': 'zap555',
                'name': 'Dennis',
                'job': 'Bartender',
            }
        ]
}


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        # resp.status_code = 200 #optionally, you can always set a response code.
        # 200 is the default code for a normal response
        return resp


# this route will return the first user if it's a get request or it will delete if it's a delete request
@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                if request.method == 'GET':
                    return user
                if request.method == 'DELETE':
                    users['users_list'].remove(user)
                    return user
        return {}
    return users


# this route will return a user if there is a name and user that matches the uri params
@app.route('/users/<name>/<job>', methods=['GET'])
def get_user_given_nameandjob(name, job):
    if name and job:
        subdict = {}
        for user in users['users_list']:
            if user['name'] == name and user['job'] == job:
                subdict[user['id']] = user
        return subdict
    return users
