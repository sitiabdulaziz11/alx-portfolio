"""
Main backe end module or routes script.
"""
from portfolio import app


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')