import db_functions as db_funcs

def get_status(username):
    query = f"""select online_status from users where username="{username}"; """
    res = db_funcs.execute(query, True)
    if res:
        return res[0][0]
    return -1

def user_exists(username):
    query = f"""select username from users where username="{username}"; """
    res = db_funcs.execute(query, True)
    if res:
        return True
    return False

def set_status(username, status):
    if not user_exists(username):
        add_user(username)
    query = f"""UPDATE users set online_status = {status} where username = "{username}";"""
    db_funcs.execute(query)

def add_user(username):
    query = f"""insert into users (username) values("{username}");"""
    db_funcs.execute(query)

def delete_user(username):
    query = f"""delete from users where username="{username}";"""
    db_funcs.execute(query)

def get_points(username):
    if not user_exists(username):
        add_user(username)
    query = f"""select points from users where username="{username}"; """
    res = db_funcs.execute(query, True)
    return res[0][0]

def add_points(username, points):
    if not user_exists(username):
        add_user(username)
    actual_points = get_points(username) + points
    query = f"""UPDATE users set points = {actual_points} where username = "{username}";"""
    db_funcs.execute(query)


def remove_points(username, points):
    if not user_exists(username):
        add_user(username)
    actual_points = get_points(username) - points
    if actual_points < 0:
        return False
    query = f"""UPDATE users set points = {actual_points} where username = "{username}";"""
    db_funcs.execute(query)
    return True

def set_points(username, points):
    if not user_exists(username):
        add_user(username)
    if points < 0:
        return -1
    query = f"""UPDATE users set points = {points} where username = "{username}";"""
    db_funcs.execute(query)

def get_online_users():
    query = """SELECT * from users where online_status = 1;"""
    ret = db_funcs.execute(query, True)
    return ret

def get_users():
    query = """SELECT * from users;"""
    ret = db_funcs.execute(query, True)
    return ret

def reset_online_status():
    query = """UPDATE users set online_status = 0;"""
    db_funcs.execute(query)

def add_command(command, response):
    query = f"""insert into commands (command, response) values("{command}", "{response}");"""
    db_funcs.execute(query)

def list_commands():
    query = """select command from commands;"""
    ret = db_funcs.execute(query, True)
    # turn it into a list of strings
    ret = [x[0] for x in ret]
    return ret

def get_command(command):
    query = f"""select response from commands where command="{command}";"""
    ret = db_funcs.execute(query, True)
    if ret:
        return ret[0][0]
    return ret

def remove_command(command):
    query = f"""delete from commands where command="{command}";"""
    db_funcs.execute(query)

def reset():
    db_funcs.create()

if __name__ == "__main__":
    reset()
    print(get_users())