from .wsgi import application

if __name__ == '__main__':
    import wfastcgi
    wfastcgi.activate()
