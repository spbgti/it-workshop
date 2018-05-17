from eve import Eve
import settings
app = Eve()

app.run(port=5001, debug=True)