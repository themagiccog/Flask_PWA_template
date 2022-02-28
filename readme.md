# PWA in Flask

## This is showing how to convert Flask to PWA app (loadable from Google Chrome or Edge)

Note the following files:

 sw.js : This is located in /static/sw.js

 app.js : This is located in /static/js/app.js

 manifest.json: This is needed to set up PWA with icons, etc. Located in /static/manifest.json (<https://manifest-gen.netlify.app/>)

 add manifest.json to [head] of index.html `<link rel="manifest" href="{{ url_for('static', filename='manifest.json') }">`

 In Index.html, add the following to body:

```html
    <script type="text/javascript" src="{{ url_for('static', filename='js/app.js') }}"></script>
    <script type="text/javascript">
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register("../sw.js").then(function(registration) {
                    // Registration was successful
                    console.log('ServiceWorker registration successful with scope: ', registration.scope);
                }, function(err) {
                    // registration failed :(
                    console.log('ServiceWorker registration failed: ', err);
                });
            });
        }
    </script>
```

In app.py, add the following routes:

```python
@app.route('/sw.js')
def service_worker():
    response = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/manifest.json')
def manifest():
    return app.send_from_directory('static', 'manifest.json')
  
@app.route('/favicon.ico')
def favicon():
    return app.send_from_directory('static', 'favicon.ico')
```
