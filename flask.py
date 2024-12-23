# pip install flask==2.3.3 (v==2.3.3)
# pip install auto-py-to-exe
# auto-py-to-exe
# pip install pyngrok


from flask import Flask, render_template, request, jsonify
import threading
import time
#from pyngrok import ngrok




counter = 0
data2 = ""




# Запуск ngrok и создание туннеля
#ngrok_tunnel = ngrok.connect(5000)
#print('Tunnel URL:', ngrok_tunnel.public_url)








def main_loop_1():
    global counter
    while True:
        counter += 1
        time.sleep(1)

thr1 = threading.Thread(target=main_loop_1)
thr1.start()

app = Flask(__name__)



# f = open('index.html', 'r', encoding="UTF-8")
# data2 = f.read()
# f.close()



@app.route('/')
def hello():
    #return data2
    return render_template('index.html')

@app.route('/dynData')
def dynData():
    global counter
    return str(counter)

@app.route('/stData')
def stData():
    return counter

@app.route('/btnClick', methods=['GET'])
def btn_click():
    #print(request.args.get('btnNumber'))
    global counter
    counter = request.args.get('btnNumber')
    return counter


@app.route('/inputData', methods=['GET'])
def inputData():
    print(request.args.get('value'))
    return ''



if __name__ == '__main__':
    app.run()
