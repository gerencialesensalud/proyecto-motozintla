from app import app

if __name__ == '__main__':
    # host='0.0.0.0' abre la aplicación para toda tu red local Wi-Fi
    # port=5000 asigna el puerto tradicional de Flask
    app.run(host='0.0.0.0', port=5000, debug=True)


