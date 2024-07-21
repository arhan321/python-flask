# belajar bikin rest api crud python-flask tanpa db
```
datanya di simpan di memory
```
# informasi ROUTE : 
```
@app.route('/create', methods=['POST'])
@app.route('/users', methods=['GET'])
@app.route('/users/<int:user_id>', methods=['GET'])
@app.route('/users/<int:user_id>', methods=['PUT'])
@app.route('/users/<int:user_id>', methods=['DELETE'])
```
# webserver
```
NGINX
```