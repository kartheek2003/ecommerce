from flask import Flask, render_template, request
import pandas as pd
from e_commerce.config.configuration import ConfigurationManager
from e_commerce.components.predictor import PredictionComponent

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def index():
    if request.method == 'POST':
        try:
            features = [float(request.form.get("recency")),
                        float(request.form.get("frequency")),
                        float(request.form.get("monetary"))]
            feature_columns = ['recency','frequency','monetary']

            input_data = pd.DataFrame([features],columns=feature_columns)

            pred_config = ConfigurationManager().prediction_config()
            predictor = PredictionComponent(config=pred_config)
            result = predictor.predict(input=input_data)

            return render_template('index.html',prediction = result)
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
