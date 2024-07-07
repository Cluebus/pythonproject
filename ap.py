from flask import Flask, request, jsonify
import easy_scpi as scpi
app = Flask(__name__)

ip = "192.168.200.100"
port = "30000"

inst = scpi.Instrument(read_termination='\n', write_termination='\n', timeout=5000) # include a timeout for reading the power level (obtained by trial-and-error)
inst.rid=f"TCPIP::{ip}::{port}::SOCKET" # define IP PORT
inst.connect()

@app.route("/query", methods =["POST"])
def queryscpi():
    try:
        data = request.json
        query = str(data.get("query"))
        result = str(inst.query(query))
        return jsonify({"result":result})
    
    except Exception as e:
        # if str(e) == "VI_ERROR_TMO (-1073807339): Timeout expired before operation completed.":
        #     return jsonify({"error": "Operation expired"})
        return jsonify({"error": str(e)})
    
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/calculator",methods=['POST'])
# def calculator():
#     try:
#         data = request.json
#         x = int(data.get("num1"))
#         y = int(data.get("num2"))
#         z = x + y
#         return jsonify({"answer":z})
#     except Exception as e:
#         return jsonify({"error": str(e)})


# @app.route("/person",methods=['POST'])
# def person():
#     try:
#         data = request.json
#         name = str(data.get("name"))
#         age = int(data.get("age"))
#         height = int(data.get("height"))
#         sentence = name + " is" + " age" + " years old"
#         inchpyear = height / age
#         return jsonify({"msg": sentence, "inchpyear": inchpyear})
#     except Exception as e:
#         return jsonify({"error": str(e)})

# # Write an API that takes two numbers and a symbol (+ or -) and returns num1 (+ or - ) num2.
# # Bonus: have the result multiplied by a random number before returning the json (this you will need to do some research for)
# @app.route("/equation",methods=['POST'])
# def equation():
#     try:
#         data = request.json
#         num1 = int(data.get("num1"))
#         num2 = int(data.get("num2"))
#         symbol = str(data.get("symbol"))
#         if symbol == "+":
#             result = num1 + num2
#         else:
#             result = num1 - num2
#         return jsonify({"msg": result})
#     except Exception as e:
#         return jsonify({"error": str(e)})

# @app.route("/e", methods = ['POST'])
# def e():
#     try:
#         data = request.json
#         s = str(data.get("number"))
#         return jsonify({"msg": s})
#     except Exception as e:
#         return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

