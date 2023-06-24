import flask
"""
Run a HTTP Flask Server with given content, path, host and port.
"""
def serverrun(content, path="/", host="127.0.0.1", port=80):
    if type(content) != str:
        raise TypeError("content must be a str")
    if type(path) != str:
        raise TypeError("path must be a str")
    if type(host) != str:
        raise TypeError("host must be a str")
    if type(port) != int:
        raise TypeError("port must be an int")
    app = flask.Flask(__name__)
    @app.route(path)
    def index():
        nonlocal content
        return content
    try:
        app.run(host=host, port=port, debug=False)
    except Exception as e:
        print("Error at running HTTP Flask server, error messsage:", e)
if __name__ == "__main__":
    print("EasyHTTPServer")
    host = input("Enter your host(default localhost):")
    port = int(input("Enter your port(default 80):"))
    if not host:
        host = "127.0.0.1"
    if not port:
        port = 80
    path = input("Enter index page's URL path(default /):")
    if not path:
        path = "/"
    content = ""
    print("Enter index page's content, end with an EOF:")
    while True:
        try:
            line = input()
            content += line
        except EOFError:
            break
    serverrun(content, path, host, port)
