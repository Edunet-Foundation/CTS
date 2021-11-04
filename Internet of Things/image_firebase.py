import pyrebase

# Your credentials after create a app web project.
config = {
    "apiKey": "your_apiKey",
    "authDomain": "your_authDomain",
    "databaseURL": "your_databaseURL",
    "projectId": "your_projectId",
    "storageBucket": "your_storageBucket",
    "messagingSenderId": "your_messagingSenderId",
    "appId": "your_appId",
    "measurementId": "your_measurementId"
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "<folder>/<file>"
path_local = "<file>"

# Upload
storage.child(path_on_cloud).put(path_local)

# Download
storage.child(path_on_cloud).download("<file_downloaded>")
