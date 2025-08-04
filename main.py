from app import app, db # Importamos la aplicación creada en app/__init__.py

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Crea las tablas en la base de datos
    app.run(debug=True) # Ejecuta la app en modo debug (muestra errores, recarga automática)


