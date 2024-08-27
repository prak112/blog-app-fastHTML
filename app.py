from fasthtml.common import *

app = FastHTML()

@app.route("/", methods=['GET'])
def home():
    page = Html(
        Head(Title('DevHub'), Meta(charset='utf-8')),
        Body(Div(H1('Welcome to DevHub!'), 
                 A('Sample Logo', href='https://example.com'),
                 Img(src='https://placehold.it/200x200', alt='Sample Logo'),))
    )
    return page

@app.route("/", methods=['POST'])
def post_home():
    return 'POST request recieved! Yaaay!'