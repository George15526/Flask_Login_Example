from src import create_app

app = create_app()

@app.route('/')
def index():
    return (
    """
    <h1>Hello, this is index page<h1>
    <h3>Register: Click <a href="http://127.0.0.1:5000/user/register">here</a><h3>
    <h3>Login: Click <a href="http://127.0.0.1:5000/user/login">here</a><h3>
    """
    )

if __name__ == '__main__':
    app.run(debug=True)