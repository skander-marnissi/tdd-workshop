from partners.broker_partner import create_app

app = create_app()

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5002, debug=True)