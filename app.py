from flask import Flask, render_template, Response

import settings

from kafka import consumer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buses')
def get_messages():
    def events():
        for msg in consumer.get_messages():
            yield 'data:{0}\n\n'.format(msg.value.decode())
    return Response(events(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, host=settings.APP_HOST, port=settings.APP_PORT)
